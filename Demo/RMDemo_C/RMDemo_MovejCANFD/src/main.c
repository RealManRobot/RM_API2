#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "rm_interface.h"
#define MAX_POINTS 5000
#define arm_dof_angle 6
#ifdef _WIN32
// Windows-specific headers and definitions
#include <windows.h>
#include <sys/types.h>
#define SLEEP_MS(ms) Sleep(ms)
#define SLEEP_S(s) Sleep((s) * 1000)
#define usleep(us) Sleep((us) / 1000)
#else
// Linux-specific headers and definitions
#include <unistd.h>
#include <sys/stat.h>
#include <sys/time.h>
#define SLEEP_MS(ms) usleep((ms) * 1000)
#define SLEEP_S(s) sleep(s)
#endif
#ifndef DATA_FILE_PATH
#error "DATA_FILE_PATH is not defined"
#endif


void event_callback(rm_event_push_data_t data) {
    printf("The motion is complete, the arm is in place.\n");
    if (data.event_type == RM_CURRENT_TRAJECTORY_STATE_E) {
        printf("Motion result: %d\n", data.trajectory_state);
        printf("Current device: %d\n", data.device);
        printf("Is the next trajectory connected: %d\n", data.trajectory_connect);
    } else if (data.event_type == RM_PROGRAM_RUN_FINISH_E) {
        printf("Online programming file ended id: %d\n", data.program_id);
    }
}
// Define the function arm_state_return
void arm_state_return(rm_realtime_arm_joint_state_t data) {
    printf("Joint positions:\n");
    for (int i = 0; i < arm_dof_angle; ++i) {
        printf("%.2f ", data.joint_status.joint_position[i]);
    }
    printf("\n");
}
void register_arm_state_return() {
    rm_realtime_arm_state_callback_ptr arm_state = arm_state_return;
    rm_realtime_arm_state_call_back(arm_state);
}
void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n",  buffer);
}


void callback_rm_realtime_arm_joint_state(rm_realtime_arm_joint_state_t data) {
    printf("Current state: %.3f\n", data.joint_status.joint_current[0]);
    printf("Current angles: %.3f %.3f %.3f %.3f %.3f %.3f\n", data.joint_status.joint_position[0], data.joint_status.joint_position[1],
           data.joint_status.joint_position[2], data.joint_status.joint_position[3], data.joint_status.joint_position[4], data.joint_status.joint_position[5]);

    printf("Current state: %u\n", data.joint_status.joint_err_code[0]);
    // Handle received data
    printf("Error Code: %d\n", data.errCode);
    printf("Arm IP: %s\n", data.arm_ip);
    printf("Error:");
    for (int i = 0; i < data.err.err_len; i++) {
        printf("0x%04X ", data.err.err[i]);
    }
    printf("\n");

    // Handle joint state
    printf("Joint Position:\n");
    for (int i = 0; i < 6; i++) {
        printf(" %.3f \n", data.joint_status.joint_position[i]);
    }

    // Handle force data
    printf("Force Sensor:\n");
    printf("  Coordinate: %u\n", data.force_sensor.coordinate);

    // Handle waypoint information
    printf("Waypoint:\n");
    printf("  Euler: [%.3f, %.3f, %.3f]\n", data.waypoint.euler.rx, data.waypoint.euler.ry, data.waypoint.euler.rz);
    printf("  Position: [%.3f, %.3f, %.3f]\n", data.waypoint.position.x, data.waypoint.position.y, data.waypoint.position.z);
    printf("  Quat: [%.3f, %.3f, %.3f, %.3f]\n", data.waypoint.quaternion.w, data.waypoint.quaternion.x, data.waypoint.quaternion.y, data.waypoint.quaternion.z);
}

void demo_movej_canfd(rm_robot_handle* handle) {
    printf("Trying to open file: %s\n", DATA_FILE_PATH);

    FILE* file = fopen(DATA_FILE_PATH, "r");
    if (!file) {
        perror("Failed to open file");
        return;
    }

    float points[MAX_POINTS][arm_dof_angle];
    int point_count = 0;
    while (fscanf(file, "%f,%f,%f,%f,%f,%f,%f",
                  &points[point_count][0], &points[point_count][1], &points[point_count][2],
                  &points[point_count][3], &points[point_count][4], &points[point_count][5],
                  &points[point_count][6]) == arm_dof_angle) {
        point_count++;
    }
    fclose(file);
    if (point_count == 0) {
        printf("No valid points data found in file\n");
        return;
    }
    rm_robot_info_t robot_info;
    int info_result = rm_get_robot_info(handle, &robot_info);
    if (info_result != 0) {
        printf("Failed to get robot info\n");
        return;
    }

    int dof = robot_info.arm_dof;
    if (dof != 6 && dof != 7) {
        printf("Invalid degree of freedom, must be 6 or 7\n");
        return;
    }

    if (point_count == 0 || (point_count > 0 && dof != arm_dof_angle)) {
        printf("Invalid points data in file\n");
        return;
    }

    printf("Total points: %d\n", point_count);
    int movej_result = rm_movej(handle, points[0], 20, 0, RM_TRAJECTORY_DISCONNECT_E, RM_MOVE_MULTI_BLOCK);
    if (movej_result != 0) {
        printf("movej failed with error code: %d\n", movej_result);
    }

    rm_realtime_arm_state_callback_ptr arm_state = arm_state_return;
    rm_realtime_arm_state_call_back(arm_state);

    rm_movej_canfd_mode_t param = {0};
    param.follow = false;
    param.expand = 0;
    for (int i = 0; i < point_count; ++i) {
        printf("Moving to point %d\n", i);
        param.joint = points[i];
        int result = rm_movej_canfd(handle, param);
        if (result != 0) {
            printf("Error at point %d: %d\n", i, result);
        }
        SLEEP_MS(10);
    }

    printf("Pass-through completed\n");
    SLEEP_S(2);

    float *home_position = (float *)malloc(dof * sizeof(float));

    for (int i = 0; i < dof; ++i) {
        home_position[i] = 0.0f;
    }
    int movej_ret = rm_movej(handle, home_position, 25, 0, RM_TRAJECTORY_DISCONNECT_E, RM_MOVE_MULTI_BLOCK);
    printf("movej_cmd joint movement 1: %d\n", movej_ret);
    SLEEP_S(2);
}


void register_event_callback(rm_robot_handle* handle) {
    rm_event_callback_ptr callback_ptr = event_callback;
    rm_get_arm_event_call_back(callback_ptr);
}


int main(int argc, char *argv[]) {
    int result = -1;

    rm_set_log_call_back(custom_api_log, 3);
    result = rm_init(RM_TRIPLE_MODE_E);
    if (result != 0) {
        printf("Initialization failed with error code: %d.\n", result);
        return -1;
    }

    char *api_version = rm_api_version();
    printf("API Version: %s.\n", api_version);

    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    if (robot_handle == NULL) {
        printf("Failed to create robot handle.\n");
        return -1;
    } else {
        printf("Robot handle created successfully: %d\n", robot_handle->id);
    }

    register_event_callback(robot_handle);
    register_arm_state_return(robot_handle);

    rm_realtime_push_config_t config = {5, true, 8089, 0, "192.168.1.88"};
    result = rm_set_realtime_push(robot_handle, config);
    if (result != 0) {
        printf("Failed to set realtime push configuration, error code: %d\n", result);
    } else {
        printf("Successfully set realtime push configuration.\n");
    }

    register_arm_state_return();
    rm_realtime_arm_state_call_back(callback_rm_realtime_arm_joint_state);
    SLEEP_S(3);
    demo_movej_canfd(robot_handle);
    // Disconnect the robot arm
    result = rm_delete_robot_arm(robot_handle);
    if(result != 0)
    {
        return -1;
    }

}
