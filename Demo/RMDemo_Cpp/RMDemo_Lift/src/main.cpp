#include <stdio.h>
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

    //Switch the current working coordinate system "Base"
    result = robotic_arm.rm_change_work_frame(robot_handle, "Base");
    if (check_result(result, "Failed to change work frame") != 0) {
        return -1;
    }
    //Set End Tool Power Supply OutPut
    result = robotic_arm.rm_set_tool_voltage(robot_handle, 3);
    if (check_result(result, "Failed to set tool voltage") != 0) {
        return -1;
    }

    //Lift up
    result = robotic_arm.rm_set_lift_height(robot_handle, 20, 500, true);
    if (check_result(result, "Failed to lift up") != 0) {
        return -1;
    }
    //Move the robot arm to the initial position
    rm_pose_t pose_movej_p = {{0.1f, 0.0f, 0.7f}, {0.0f, 0.0f, 0.0f, 0.0f}, {0.0f, 0.0f, 3.141f}};
    result = robotic_arm.rm_movej_p(robot_handle, pose_movej_p, 20, 0, 0, 1);
    if (check_result(result, "Failed to move to initial position") != 0) {
        return -1;
    }

    //Move the robot arm to the gripping position
    rm_pose_t pose_movel = {{0.1f, 0.0f, 0.8f}, {0.0f, 0.0f, 0.0f, 0.0f}, {0.0f, 0.0f, 3.141f}};
    result = robotic_arm.rm_movel(robot_handle, pose_movel, 10, 0, 0, 1);
    if (check_result(result, "Failed to move to gripping position") != 0) {
        return -1;
    }
    //Perform continuous force-controlled gripping
    result = robotic_arm.rm_set_gripper_pick_on(robot_handle, 500, 200, true, 10);
    if (check_result(result, "Failed to perform force-controlled gripping") != 0) {
        return -1;
    }
    //Move the robot arm back to the initial position
    result = robotic_arm.rm_movel(robot_handle, pose_movej_p, 10, 0, 0, 1);
    if (check_result(result, "Failed to move back to initial position") != 0) {
        return -1;
    }
    // Lift down
    result = robotic_arm.rm_set_lift_height(robot_handle, 10, 200, true);
    if (check_result(result, "Failed to lift down") != 0) {
        return -1;
    }
    //Move the robot arm to the placing position
    result = robotic_arm.rm_movel(robot_handle, pose_movel, 10, 0, 0, 1);
    if (check_result(result, "Failed to move to placing position") != 0) {
        return -1;
    }
    //Release the gripper
    result = robotic_arm.rm_set_gripper_release(robot_handle, 500, true, 30);
    if (check_result(result, "Failed to release the gripper") != 0) {
        return -1;
    }

   // Move the robot arm back to the initial position
    result = robotic_arm.rm_movel(robot_handle, pose_movej_p, 20, 0, 0, 1);
    if (check_result(result, "Failed to move back to initial position") != 0) {
        return -1;
    }

    // Disconnect the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }
}
