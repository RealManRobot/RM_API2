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
    int result = -1;
    RM_Service robotic_arm;

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

    float joint_angles_start[ARM_DOF] = {90.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
    float joint_angles_end[ARM_DOF] = {0.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
    // Perform movej motion Start
    result = robotic_arm.rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
    if (check_result(result, "Failed to perform movej motion (start)") != 0) {
        return -1;
    }

    robotic_arm.rm_set_gripper_release(robot_handle, 500, true, 5);
    //Perform continuous force-controlled gripping
    result = robotic_arm.rm_set_gripper_pick_on(robot_handle, 500, 200, true, 30);
    if (check_result(result, "Failed to perform continuous force-controlled gripping") != 0) {
        return -1;
    }
    // Perform rm_movej motion End
    result = robotic_arm.rm_movej(robot_handle, joint_angles_end, 20, 0, 0, 1);
    if (check_result(result, "Failed to perform movej motion (end)") != 0) {
        return -1;
    }
    //Release the gripper
    result = robotic_arm.rm_set_gripper_release(robot_handle, 500, true, 30);
    if (check_result(result, "Failed to release the gripper") != 0) {
        return -1;
    }
    // Perform rm_movej motion Start
    result = robotic_arm.rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
    if (check_result(result, "Failed to perform movej motion (start again)") != 0) {
        return -1;
    }

    // Disconnect the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }

}