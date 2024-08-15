#include <stdio.h>
#include "rm_service.h"
#ifdef _WIN32
#include <windows.h>
#include <sys/types.h>

#define SLEEP_MS(ms) Sleep(ms)
#define SLEEP_S(s) Sleep((s) * 1000)
#define usleep(us) Sleep((us) / 1000)

#else
#include <unistd.h>
#include <sys/time.h>
#define SLEEP_MS(ms) usleep((ms) * 1000)
#define SLEEP_S(s) sleep(s)

#endif

void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n",  buffer);
}

int check_result(int result, const char *error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
        return -1;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    RM_Service robotic_arm;
    int result = -1;
    robotic_arm.rm_set_log_call_back(custom_api_log, 3);
    result = robotic_arm.rm_init(RM_TRIPLE_MODE_E);
    if (result != 0) {
        printf("Initialization failed with error code: %d.\n", result);
        return -1;
    }

    char *api_version = robotic_arm.rm_api_version();
    printf("API Version: %s.\n", api_version);

    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = robotic_arm.rm_create_robot_arm(robot_ip_address, robot_port);
    if (robot_handle == NULL) {
        printf("Failed to create robot handle.\n");
        return -1;
    } else {
        printf("Robot handle created successfully: %d\n", robot_handle->id);
    }

    // Get the current state of the robot arm
    rm_current_arm_state_t current_state;
    result = robotic_arm.rm_get_current_arm_state(robot_handle, &current_state);
    if (check_result(result, "Failed to get current arm state") != 0) {
        return -1;
    }

    /*
     * Enable force position control mode, perform Cartesian space motion, and disable force position control mode after the motion ends.
     * Move to the starting position
     */
    float joint_angles_start[ARM_DOF] = {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f};
    result = robotic_arm.rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
    if (check_result(result, "Failed to perform rm_movej motion (start)") != 0) {
        return -1;
    }

    SLEEP_S(1);
    rm_pose_t start_pose = { {0.3f, 0.0f, 0.4f},{0.0f, 0.0f, 0.0f,0.0f}, {3.141f, 0.0f, 0.0f} };
    result = robotic_arm.rm_movej_p(robot_handle, start_pose, 20, 0, 0, 1);
    if (check_result(result, "Failed to perform rm_movej_p motion") != 0) {
        return -1;
    }
    SLEEP_S(2);

    for (int i = 0; i < 3; ++i) {
        // Set force control mode
        result = robotic_arm.rm_set_force_position(robot_handle, 1, 0, 2, -5);
        if (check_result(result, "Failed to set force position control mode") != 0) {
            return -1;
        }
        // Move to the target position
        rm_pose_t target_pose = { {0.2f, 0.0f, 0.4f},{0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };

        result = robotic_arm.rm_movel(robot_handle, target_pose, 60, 0, 0, 1);
        if (check_result(result, "Failed to perform rm_movel motion to target") != 0) {
            return -1;
        }
        SLEEP_S(2);

        // Move back to the starting position
        robotic_arm.rm_movel(robot_handle, start_pose, 50, 0, 0, 1);

        SLEEP_S(2);

        // Stop force control mode
        result = robotic_arm.rm_stop_force_position(robot_handle);
        if (check_result(result, "Failed to stop force position control mode") != 0) {
            return -1;
        }
    }

    // Disconnect the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }

}
