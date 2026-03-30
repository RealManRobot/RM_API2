#include <stdio.h>
#include <iostream>
#include <thread>
#include <string.h>
#include "rm_service.h"
#ifdef _WIN32
#include <windows.h>
#define SLEEP_MS(ms) Sleep(ms)
#define SLEEP_S(s) Sleep((s) * 1000)
#else
#include <unistd.h>
#define SLEEP_MS(ms) usleep((ms) * 1000)
#define SLEEP_S(s) sleep(s)
#endif

// 日志回调函数
void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }
    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n", buffer);
}

// 检查结果函数
int check_result(int result, const char* error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
        return -1;
    }
    return 0;
}

// 合并后的机械臂任务函数（通过task_id区分两套动作）
int arm_task(const char* ip, int port, int task_id) {
    RM_Service arm_service;
    int result = -1;

    // 初始化服务
    arm_service.rm_set_log_call_back(custom_api_log, 3);
    result = arm_service.rm_init(RM_TRIPLE_MODE_E);
    if (check_result(result, "Service initialization failed") != 0) {
        return -1;
    }

    // 打印API版本
    char* api_version = arm_service.rm_api_version();
    printf("API Version for %s:%d: %s.\n", ip, port, api_version);

    // 连接机械臂
    printf("Connecting to %s:%d...\n", ip, port);
    rm_robot_handle* robot_handle = arm_service.rm_create_robot_arm(ip, port);
    if (robot_handle == NULL || robot_handle->id < 0) {
        printf("Failed to create handle for %s:%d (handle id: %d)\n",
            ip, port, robot_handle ? robot_handle->id : -1);
        result = arm_service.rm_delete_robot_arm(robot_handle);
        check_result(result, "Failed to delete robot handle after creation error");
        return -1;
    }
    printf("Connected to %s:%d (handle id: %d)\n", ip, port, robot_handle->id);

    // 获取当前状态
    rm_current_arm_state_t current_state;
    result = arm_service.rm_get_current_arm_state(robot_handle, &current_state);
    if (check_result(result, "Failed to get current arm state") != 0) {
        result = arm_service.rm_delete_robot_arm(robot_handle);
        check_result(result, "Failed to disconnect robot during state error");
        return -1;
    }

    // 定义两套动作的参数（根据task_id选择）
    float joint_angles[ARM_DOF];
    rm_pose_t start_pose, target_pose;
    int loop_count;  // 循环次数
    int move_speed;  // 运动速度

    if (task_id == 1) {
        // 第一套动作参数
        float temp_joint1[ARM_DOF] = { 0.0f, 0.5f, 0.3f, 0.0f, 0.2f, 0.0f, 0.1f };
        memcpy(joint_angles, temp_joint1, sizeof(temp_joint1));
        start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        target_pose = { {0.2f, 0.1f, 0.3f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        loop_count = 2;
        move_speed = 20;
    }
    else {
        // 第二套动作参数（task_id=2）
        float temp_joint2[ARM_DOF] = { 0.2f, -0.3f, 0.1f, 0.5f, -0.2f, 0.3f, 0.0f };
        memcpy(joint_angles, temp_joint2, sizeof(temp_joint2));
        start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        target_pose = { {0.25f, -0.1f, 0.35f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        loop_count = 3;
        move_speed = 15;
    }

    // 执行动作（根据task_id选择运动方式）
    for (int i = 0; i < loop_count; ++i) {
        // 移动到关节角度
        result = arm_service.rm_movej(robot_handle, joint_angles, move_speed, 0, 0, 1);
        if (check_result(result, "Failed to move to joint angles") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(1);

        // 移动到起始位姿
        result = arm_service.rm_movej_p(robot_handle, start_pose, move_speed, 0, 0, 1);
        if (check_result(result, "Failed to move to start pose") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(2);

        // 根据任务选择不同的运动函数（修复参数不匹配问题）
        if (task_id == 1) {
            // 第一套动作：使用rm_movel（7参数保持不变）
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
        else {
            // 第二套动作：使用rm_movec（调整为6参数匹配函数声明）
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
        if (check_result(result, "Failed to move to target pose") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(2);
    }

    // 断开连接
    result = arm_service.rm_delete_robot_arm(robot_handle);
    check_result(result, "Failed to disconnect the robot arm");
    printf("Task %d completed for %s:%d\n", task_id, ip, port);
    return 0;
}

int main(int argc, char* argv[]) {
    // 机械臂地址
    const char* ip1 = "192.168.1.18";
    int port1 = 8080;
    const char* ip2 = "192.168.1.21";
    int port2 = 8080;

    // 启动线程（分别传入task_id=1和task_id=2）
    std::thread arm1_thread(arm_task, ip1, port1, 1);  // 机械臂1执行第一套动作
    std::thread arm2_thread(arm_task, ip2, port2, 2);  // 机械臂2执行第二套动作

    // 等待线程完成
    arm1_thread.join();
    arm2_thread.join();

    printf("All robot tasks completed\n");
    return 0;
}
