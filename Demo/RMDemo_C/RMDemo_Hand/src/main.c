#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include "rm_interface.h"

static volatile sig_atomic_t stop_requested;

static void request_stop(int signal_number) {
    stop_requested = signal_number;
}

#ifdef _WIN32
#include <windows.h>

static inline void msleep(float milliseconds) {
    Sleep(milliseconds);
}

#else
#include <unistd.h>
#include <time.h>
#include <math.h>   // fmod函数依赖此头文件
#include <errno.h>

// 支持浮点毫秒传值（比如500.0ms、1500.5ms）
static inline void msleep(float milliseconds) {
    struct timespec ts;
    struct timespec rem; // 处理nanosleep被信号中断的情况

    // 1. 拆分秒和纳秒：核心修复%运算符的问题
    ts.tv_sec = (time_t)(milliseconds / 1000.0);          // 提取整数秒
    float frac_ms = fmod(milliseconds, 1000.0);           // 浮点取模，获取不足1秒的毫秒
    ts.tv_nsec = (long)(frac_ms * 1000000.0);             // 转换为纳秒

    // 2. 安全检查：保证tv_nsec在0~999999999范围内（nanosleep的硬性要求）
    if (ts.tv_nsec < 0) {
        ts.tv_nsec = 0;
    }
    if (ts.tv_nsec >= 1000000000) {
        ts.tv_sec += 1;
        ts.tv_nsec -= 1000000000;
    }

    // 3. 处理nanosleep被信号中断的情况（保证休眠时间精准）
    while (nanosleep(&ts, &rem) == -1 && errno == EINTR) {
        ts = rem;
    }
}
#endif

static int wait_seconds(float seconds) {
    float remaining = seconds * 1000.0f;
    while (remaining > 0 && !stop_requested) {
        float interval = remaining > 100.0f ? 100.0f : remaining;
        msleep(interval);
        remaining -= interval;
    }
    return stop_requested ? EXIT_FAILURE : EXIT_SUCCESS;
}

#define CHECK(call, message) do { \
    if (stop_requested) { goto cleanup; } \
    if (check_result((call), (message)) != 0 || stop_requested) { goto cleanup; } \
} while (0)

#define WAIT(seconds) CHECK(wait_seconds(seconds), "Demo wait interrupted")

void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n",  buffer);
}

static int check_result(int result, const char *error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
    }
    return result;
}

static int finger_init(rm_robot_handle* robot_handle, const int pos[6], int *position_changed) {
    if (wait_seconds(2) != 0) { return EXIT_FAILURE; }
    *position_changed = 1;
    int ret = rm_set_hand_follow_pos(robot_handle, pos, true);
    if (ret != 0) { return ret; }
    return wait_seconds(2);
}

static int restore_position(rm_robot_handle *robot_handle, const int original_pos[6]) {
    if (check_result(rm_set_hand_follow_pos(robot_handle, original_pos, true),
                     "Failed to restore hand position") != 0) {
        return EXIT_FAILURE;
    }
    // Follow-mode acknowledgement does not confirm that the fingers have arrived.
    for (int attempt = 0; attempt < 50; ++attempt) {
        rm_plus_state_info_t state = {0};
        state.sys_state = -1;
        for (int i = 0; i < 6; ++i) { state.pos[i] = -1; }
        if (check_result(rm_get_rm_plus_state_info(robot_handle, &state),
                         "Failed to verify restored hand position") != 0) {
            return EXIT_FAILURE;
        }
        int matches = state.sys_state == 0;
        for (int i = 0; i < 6; ++i) {
            if (state.pos[i] != original_pos[i] || state.dof_err[i] != 0) { matches = 0; }
        }
        if (matches) { return EXIT_SUCCESS; }
        msleep(100);
    }
    fprintf(stderr, "Hand position restoration was not confirmed.\n");
    return EXIT_FAILURE;
}

int main(void) {
    int result = EXIT_FAILURE;
    int api_initialized = 0;
    int voltage = -1, mode = -1;
    int rs485_mode = -1, baudrate = -1, timeout = -1;
    rm_robot_info_t robot_info = {0};
    int voltage_changed = 0, mode_changed = 0, position_changed = 0;
    int original_pos[6] = {0};
    rm_robot_handle *robot_handle = NULL;

    if (signal(SIGINT, request_stop) == SIG_ERR || signal(SIGTERM, request_stop) == SIG_ERR) {
        fprintf(stderr, "Failed to install exit signal handlers.\n");
        return EXIT_FAILURE;
    }

    rm_set_log_call_back(custom_api_log, 3);
    int init_result = rm_init(RM_TRIPLE_MODE_E);
    api_initialized = init_result == 0;
    CHECK(init_result, "Initialization failed");
    printf("API Version: %s.\n", rm_api_version());

    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    if (robot_handle == NULL || robot_handle->id <= 0) {
        printf("Failed to create robot handle.\n");
        robot_handle = NULL;
        goto cleanup;
    }
    printf("Robot handle created successfully: %d\n", robot_handle->id);

    // Configure the tool before reading the hand's calibration registers.
    CHECK(rm_get_robot_info(robot_handle, &robot_info), "Failed to get controller type");
    CHECK(rm_get_tool_voltage(robot_handle, &voltage), "Failed to get tool voltage!\n");
    CHECK(rm_get_rm_plus_mode(robot_handle, &mode), "Failed to get plus mode!\n");
    if (robot_info.robot_controller_version == 3) {
        CHECK(rm_get_tool_RS485_mode(robot_handle, &rs485_mode, &baudrate, &timeout), "Failed to save tool RS485 mode");
    } else if (robot_info.robot_controller_version == 4) {
        CHECK(rm_get_tool_rs485_mode_v4(robot_handle, &rs485_mode, &baudrate), "Failed to save tool RS485 mode");
    } else {
        fprintf(stderr, "Unsupported controller type.\n");
        goto cleanup;
    }
    if ((voltage != 0 && voltage != 2 && voltage != 3) ||
        (mode != 0 && mode != 9600 && mode != 115200 && mode != 256000 && mode != 460800) ||
        rs485_mode < 0 || rs485_mode > (robot_info.robot_controller_version == 3 ? 1 : 2) ||
        (rs485_mode == (robot_info.robot_controller_version == 3 ? 1 : 0) &&
         ((baudrate != 9600 && baudrate != 115200 && baudrate != 460800) ||
          (robot_info.robot_controller_version == 3 && timeout <= 0)))) {
        fprintf(stderr, "Original tool configuration cannot be restored safely.\n");
        goto cleanup;
    }
    if (voltage != 3) {
        voltage_changed = 1;
        CHECK(rm_set_tool_voltage(robot_handle, 3), "Failed to set tool voltage!\n");
    }
    if (mode != 115200) {
        mode_changed = 1;
        CHECK(rm_set_rm_plus_mode(robot_handle, 115200), "Failed to set plus mode!\n");
    }
    WAIT(15);

    rm_plus_state_info_t original_state = {0};
    original_state.sys_state = -1;
    for (int i = 0; i < 6; ++i) { original_state.pos[i] = -1; }
    CHECK(rm_get_rm_plus_state_info(robot_handle, &original_state), "Failed to save hand position");
    for (int i = 0; i < 6; ++i) {
        if (original_state.sys_state != 0 || original_state.dof_err[i] != 0 ||
            original_state.pos[i] < 0 || original_state.pos[i] > 65535) {
            fprintf(stderr, "Cannot save valid original position for finger %d.\n", i + 1);
            goto cleanup;
        }
        original_pos[i] = original_state.pos[i];
    }
    // Follow control does not need the legacy speed/force setters, which have no matching getters.

    int arr[6] = { 0,0,0,0,0,0 }, Init[6] = { 0 }, High_pos[6] = { 0 }, Low_pos[6] = { 0 }, High_angle[6] = { 0 }, Low_angle[6] = { 0 };
    CHECK(rm_get_rm_plus_reg(robot_handle, 1100, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { High_pos[i] = arr[i]; printf("High_pos[%d] is %d\n", i, High_pos[i]);}

    CHECK(rm_get_rm_plus_reg(robot_handle, 1120, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { Low_pos[i] = arr[i]; Init[i] = arr[i]; printf("Low_pos[%d] is %d\n", i, Low_pos[i]);}

    CHECK(rm_get_rm_plus_reg(robot_handle, 1140, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { High_angle[i] = arr[i]; printf("High_angle[%d] is %d\n", i, High_angle[i]);}

    CHECK(rm_get_rm_plus_reg(robot_handle, 1160, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { Low_angle[i] = arr[i]; printf("Low_angle[%d] is %d\n", i, Low_angle[i]);}
    for (int i = 0; i < 6; i++) {
        if (Low_pos[i] < 0 || High_pos[i] > 65535 || Low_pos[i] > High_pos[i] ||
            Low_angle[i] < -32768 || Low_angle[i] > 32767 ||
            High_angle[i] < -32768 || High_angle[i] > 32767 || Low_angle[i] > High_angle[i]) {
            fprintf(stderr, "Invalid hand calibration range for finger %d: position=[%d,%d], angle=[%d,%d].\n",
                    i + 1, Low_pos[i], High_pos[i], Low_angle[i], High_angle[i]);
            CHECK(1, "Invalid hand calibration range");
        }
    }

    //set hand follow pos
    CHECK(finger_init(robot_handle, Init, &position_changed), "Failed to initialize fingers");
    WAIT(2);
    for (int i = 1; i < 6; i++) {
        WAIT(1);
        while (Low_pos[i] < High_pos[i]) {
            Low_pos[i] += 1000;
            if (Low_pos[i] > High_pos[i]) {Low_pos[i] = High_pos[i];}
            Low_pos[i - 1] = Init[i - 1];
            CHECK(rm_set_hand_follow_pos(robot_handle, Low_pos, true), "setting hand follow pos unseccessfully!\n");
            msleep(20);
        }
    }

    //yeah pose of the hand
    CHECK(finger_init(robot_handle, Init, &position_changed), "Failed to initialize fingers");
    int yeah_angle[6] = { Low_angle[0], High_angle[1], High_angle[2], Low_angle[3], Low_angle[4], Low_angle [5]};
    CHECK(rm_set_hand_follow_angle(robot_handle, yeah_angle, true), "set hand follow angle yeah unseccessfully!\n");

    //ok pose of the hand
    CHECK(finger_init(robot_handle, Init, &position_changed), "Failed to initialize fingers");
    int ok_angle[6] = { High_angle[0], Low_angle[1], High_angle[2], High_angle[3], High_angle[4], High_angle[5]};
    CHECK(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok unseccessfully!\n");
    WAIT(2);
    ok_angle[0] = Low_angle[0];
    CHECK(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok  2 unseccessfully!\n");
    WAIT(1);
    ok_angle[0] = High_angle[0];
    CHECK(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok  3 unseccessfully!\n");

    //six pose of the hand
    CHECK(finger_init(robot_handle, Init, &position_changed), "Failed to initialize fingers");
    int six_angle[6] = { High_angle[0], Low_angle[1], Low_angle[2], Low_angle[3], High_angle[4], High_angle [5]};
    CHECK(rm_set_hand_follow_angle(robot_handle, six_angle, true), "set hand follow angle six unseccessfully!\n");
    WAIT(1);
    six_angle[5] = Low_angle[5];
    CHECK(rm_set_hand_follow_angle(robot_handle, six_angle, true), "set hand follow angle six 2 unseccessfully!\n");
    WAIT(0.5);

    result = EXIT_SUCCESS;

cleanup:
    if (stop_requested) {
        fprintf(stderr, "Demo interrupted by signal %d; restoring original state.\n", (int)stop_requested);
        result = EXIT_FAILURE;
    }
    if (robot_handle != NULL) {
        if (position_changed && restore_position(robot_handle, original_pos) != 0) {
            result = EXIT_FAILURE;
        }
        if (mode_changed) {
            int restored_mode = -1;
            if (check_result(rm_set_rm_plus_mode(robot_handle, mode), "Failed to restore plus mode") != 0 ||
                check_result(rm_get_rm_plus_mode(robot_handle, &restored_mode), "Failed to verify plus mode") != 0 ||
                restored_mode != mode) {
                fprintf(stderr, "Plus mode restoration was not confirmed (expected %d, read %d).\n", mode, restored_mode);
                result = EXIT_FAILURE;
            }
            // Enabling the ecological protocol also changes the tool's RS485 mode.
            int restore_ret = 0, read_ret;
            int restored_rs485_mode = -1, restored_baudrate = -1, restored_timeout = -1;
            if (robot_info.robot_controller_version == 3) {
                if (rs485_mode == 1) {
                    restore_ret = rm_set_modbus_mode(robot_handle, 1, baudrate, timeout);
                }
                read_ret = rm_get_tool_RS485_mode(robot_handle, &restored_rs485_mode, &restored_baudrate, &restored_timeout);
            } else {
                restore_ret = rm_set_tool_rs485_mode(robot_handle, rs485_mode, baudrate);
                read_ret = rm_get_tool_rs485_mode_v4(robot_handle, &restored_rs485_mode, &restored_baudrate);
            }
            if (check_result(restore_ret, "Failed to restore tool RS485 mode") != 0 ||
                check_result(read_ret, "Failed to verify tool RS485 mode") != 0 ||
                restored_rs485_mode != rs485_mode || restored_baudrate != baudrate ||
                (robot_info.robot_controller_version == 3 && rs485_mode == 1 && restored_timeout != timeout)) {
                fprintf(stderr, "Tool RS485 restoration was not confirmed.\n");
                result = EXIT_FAILURE;
            }
        }
        if (voltage_changed) {
            int restored_voltage = -1;
            if (check_result(rm_set_tool_voltage(robot_handle, voltage), "Failed to restore tool voltage") != 0 ||
                check_result(rm_get_tool_voltage(robot_handle, &restored_voltage), "Failed to verify tool voltage") != 0 ||
                restored_voltage != voltage) {
                fprintf(stderr, "Tool voltage restoration was not confirmed (expected %d, read %d).\n", voltage, restored_voltage);
                result = EXIT_FAILURE;
            }
        }
        if (check_result(rm_delete_robot_arm(robot_handle), "Failed to disconnect the robot arm") != 0) {
            result = EXIT_FAILURE;
        }
    }
    if (api_initialized && check_result(rm_destroy(), "Failed to destroy API") != 0) {
        result = EXIT_FAILURE;
    }
    if (stop_requested) { result = EXIT_FAILURE; }
    return result;
}
