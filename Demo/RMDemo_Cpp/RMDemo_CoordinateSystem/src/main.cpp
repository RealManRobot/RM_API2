#include <stdio.h>
#include <time.h>
#include <sys/stat.h>

#include "rm_service.h"

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
    
    const char *workFrameName = "WorkTest";
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

    // Set manual work frame
    rm_pose_t initial_pose = {{0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0}};
    result = robotic_arm.rm_set_manual_work_frame(robot_handle, workFrameName, initial_pose);
    if (check_result(result, "Failed to set manual work frame") != 0) {
        return -1;
    }

    // Update work frame
    rm_pose_t updated_pose = {{0.3f, 0.0f, 0.3f},{0, 0, 0, 0},{3.142f, 0.0f, 0.0f}};
    result = robotic_arm.rm_update_work_frame(robot_handle, workFrameName, updated_pose);
    if (check_result(result, "Failed to update work frame") != 0) {
        return -1;
    }

    // Get specified work frame
    rm_pose_t pose;
    result = robotic_arm.rm_get_given_work_frame(robot_handle, workFrameName, &pose);
    if (check_result(result, "Failed to get specified work frame") != 0) {
        return -1;
    }

    // Delete work frame
    result = robotic_arm.rm_delete_work_frame(robot_handle, workFrameName);
    if (check_result(result, "Failed to delete work frame") != 0) {
        return -1;
    }

    // Disconnect from the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }

}
