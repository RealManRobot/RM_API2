#include <stdio.h>
#include "rm_interface.h"

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

// 支持浮点秒传值（比如WAIT(0.5) → 休眠500毫秒）
#define WAIT(seconds)   msleep((seconds) * 1000.0);printf("wait for setting successfully!\n");

void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n",  buffer);
}

void check_result(int result, const char *error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
        return;
    }
    return;
}

void finger_init(rm_robot_handle* robot_handle, const int pos[6]) {
    WAIT(2);
    check_result(rm_set_hand_follow_pos(robot_handle, pos, true), "rm_set_hand_follow_pos unseccessfully!\n");
    WAIT(2);
    return;
}


int main(int argc, char *argv[]) {

    rm_set_log_call_back(custom_api_log, 3);
    check_result(rm_init(RM_TRIPLE_MODE_E), "Initialization failed with error code: %d.\n");
    printf("API Version: %s.\n", rm_api_version());

    rm_robot_handle *robot_handle = rm_create_robot_arm("192.168.1.18", 8080);
    robot_handle == NULL ? printf("Failed to create robot handle.\n"):printf("Robot handle created successfully: %d\n", robot_handle->id);

    int arr[6] = { 0,0,0,0,0,0 }, Init[6] = { 0 }, High_pos[6] = { 0 }, Low_pos[6] = { 0 }, High_angle[6] = { 0 }, Low_angle[6] = { 0 };
    check_result(rm_get_rm_plus_reg(robot_handle, 1100, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { High_pos[i] = arr[i]; printf("High_pos[%d] is %d\n", i, High_pos[i]);}

    check_result(rm_get_rm_plus_reg(robot_handle, 1120, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { Low_pos[i] = arr[i]; Init[i] = arr[i]; printf("Low_pos[%d] is %d\n", i, Low_pos[i]);}

    check_result(rm_get_rm_plus_reg(robot_handle, 1140, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { High_angle[i] = arr[i]; printf("High_angle[%d] is %d\n", i, High_angle[i]);}

    check_result(rm_get_rm_plus_reg(robot_handle, 1160, 6, arr), "Failed to get puls base date!\n");
    for (int i = 0; i < 6; i++) { Low_angle[i] = arr[i]; printf("Low_angle[%d] is %d\n", i, Low_angle[i]);}
   
    //Set End Tool Power Supply OutPut && Set plus mode && Set hand speed and force
     int voltage = -1, mode = -1;
    check_result(rm_get_tool_voltage(robot_handle, &voltage), "Failed to get tool voltage!\n");
    if (voltage != 3) {check_result(rm_set_tool_voltage(robot_handle, 3), "Failed to set tool voltage!\n");}
    check_result(rm_get_rm_plus_mode(robot_handle, &mode), "Failed to get plus mode!\n");
    if (mode != 115200) { check_result(rm_set_rm_plus_mode(robot_handle, 115200), "Failed to set plus mode!\n"); }

    check_result(rm_set_hand_speed(robot_handle, 500) && rm_set_hand_force(robot_handle, 500), "Failed to set hand speed or force!\n");

    //Wait setting 
    WAIT(15);

    //set hand follow pos
    finger_init(robot_handle, Init);
    WAIT(2);
    for (int i = 1; i < 6; i++) {
        WAIT(1);
        while (Low_pos[i] <= High_pos[i]) {
            Low_pos[i] += 1000;
            Low_pos[i - 1] = 0;
            check_result(rm_set_hand_follow_pos(robot_handle, Low_pos, true), "setting hand follow pos unseccessfully!\n");
        }
    }

    //yeah pose of the hand
    finger_init(robot_handle, Init);
    int yeah_angle[6] = { Low_angle[0], High_angle[1], High_angle[2], Low_angle[3], Low_angle[4], Low_angle [5]};
    check_result(rm_set_hand_follow_angle(robot_handle, yeah_angle, true), "set hand follow angle yeah unseccessfully!\n");

    //ok pose of the hand
    finger_init(robot_handle, Init);
    int ok_angle[6] = { High_angle[0], Low_angle[1], High_angle[2], High_angle[3], High_angle[4], High_angle[5]};
    check_result(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok unseccessfully!\n");
    WAIT(2);
    ok_angle[0] = Low_angle[0];
    check_result(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok  2 unseccessfully!\n");
    WAIT(1);
    ok_angle[0] = High_angle[0];
    check_result(rm_set_hand_follow_angle(robot_handle, ok_angle, true), "set hand follow angle ok  3 unseccessfully!\n");

    //six pose of the hand 
    finger_init(robot_handle, Init);
    int six_angle[6] = { High_angle[0], Low_angle[1], Low_angle[2], Low_angle[3], High_angle[4], High_angle [5]};
    check_result(rm_set_hand_follow_angle(robot_handle, six_angle, true), "set hand follow angle six unseccessfully!\n");
    WAIT(1);
    six_angle[5] = Low_angle[5];
    check_result(rm_set_hand_follow_angle(robot_handle, six_angle, true), "set hand follow angle six 2 unseccessfully!\n");
    WAIT(0.5);

    // Disconnect the robot arm
    check_result(rm_delete_robot_arm(robot_handle), "Failed to disconnect the robot arm");
    return 0;
}
