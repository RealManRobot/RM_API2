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

// ��־�ص�����
void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }
    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n", buffer);
}

// ���������
int check_result(int result, const char* error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
        return -1;
    }
    return 0;
}

// �ϲ���Ļ�е����������ͨ��task_id�������׶�����
int arm_task(const char* ip, int port, int task_id) {
    RM_Service arm_service;
    int result = -1;

    // ��ʼ������
    arm_service.rm_set_log_call_back(custom_api_log, 3);
    result = arm_service.rm_init(RM_TRIPLE_MODE_E);
    if (check_result(result, "Service initialization failed") != 0) {
        return -1;
    }

    // ��ӡAPI�汾
    char* api_version = arm_service.rm_api_version();
    printf("API Version for %s:%d: %s.\n", ip, port, api_version);

    // ���ӻ�е��
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

    // ��ȡ��ǰ״̬
    rm_current_arm_state_t current_state;
    result = arm_service.rm_get_current_arm_state(robot_handle, &current_state);
    if (check_result(result, "Failed to get current arm state") != 0) {
        result = arm_service.rm_delete_robot_arm(robot_handle);
        check_result(result, "Failed to disconnect robot during state error");
        return -1;
    }

    // �������׶����Ĳ���������task_idѡ��
    float joint_angles[ARM_DOF];
    rm_pose_t start_pose, target_pose;
    int loop_count;  // ѭ������
    int move_speed;  // �˶��ٶ�

    if (task_id == 1) {
        // ��һ�׶�������
        float temp_joint1[ARM_DOF] = { 0.0f, 0.5f, 0.3f, 0.0f, 0.2f, 0.0f, 0.1f };
        memcpy(joint_angles, temp_joint1, sizeof(temp_joint1));
        start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        target_pose = { {0.2f, 0.1f, 0.3f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        loop_count = 2;
        move_speed = 20;
    }
    else {
        // �ڶ��׶���������task_id=2��
        float temp_joint2[ARM_DOF] = { 0.2f, -0.3f, 0.1f, 0.5f, -0.2f, 0.3f, 0.0f };
        memcpy(joint_angles, temp_joint2, sizeof(temp_joint2));
        start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        target_pose = { {0.25f, -0.1f, 0.35f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
        loop_count = 3;
        move_speed = 15;
    }

    // ִ�ж���������task_idѡ���˶���ʽ��
    for (int i = 0; i < loop_count; ++i) {
        // �ƶ����ؽڽǶ�
        result = arm_service.rm_movej(robot_handle, joint_angles, move_speed, 0, 0, 1);
        if (check_result(result, "Failed to move to joint angles") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(1);

        // �ƶ�����ʼλ��
        result = arm_service.rm_movej_p(robot_handle, start_pose, move_speed, 0, 0, 1);
        if (check_result(result, "Failed to move to start pose") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(2);

        // ��������ѡ��ͬ���˶��������޸�������ƥ�����⣩
        if (task_id == 1) {
            // ��һ�׶�����ʹ��rm_movel��7�������ֲ��䣩
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
        else {
            // �ڶ��׶�����ʹ��rm_movec������Ϊ6����ƥ�亯��������
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
        if (check_result(result, "Failed to move to target pose") != 0) {
            arm_service.rm_delete_robot_arm(robot_handle);
            return -1;
        }
        SLEEP_S(2);
    }

    // �Ͽ�����
    result = arm_service.rm_delete_robot_arm(robot_handle);
    check_result(result, "Failed to disconnect the robot arm");
    printf("Task %d completed for %s:%d\n", task_id, ip, port);
    return 0;
}

int main(int argc, char* argv[]) {
    // ��е�۵�ַ
    const char* ip1 = "192.168.1.18";
    int port1 = 8080;
    const char* ip2 = "192.168.1.21";
    int port2 = 8080;

    // �����̣߳��ֱ���task_id=1��task_id=2��
    std::thread arm1_thread(arm_task, ip1, port1, 1);  // ��е��1ִ�е�һ�׶���
    std::thread arm2_thread(arm_task, ip2, port2, 2);  // ��е��2ִ�еڶ��׶���

    // �ȴ��߳����
    arm1_thread.join();
    arm2_thread.join();

    printf("All robot tasks completed\n");
    return 0;
}
