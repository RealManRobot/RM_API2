#include <stdio.h>
#include "rm_service.h"

RM_Service robotic_arm;

void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf(" %s\n",  buffer);
}

/**
 * @brief Execute a sequence of moves to the given positions
 *
 * @param handle Robot arm control handle
 * @param positions Array of target positions  (list of float, optional): List of positions to move to, each position is [x, y, z, rx, ry, rz].
 * @param num_positions Number of positions in the array
 * @param speed Speed ratio 1~100, representing the percentage of the planned speed and acceleration to the maximum linear speed and acceleration of the robot arm end
 * @param block Blocking setting
 *        - 0: Non-blocking mode, return immediately after sending the command.
 *        - 1: Blocking mode, wait until the robot arm reaches the target position or the planning fails.
 */
void execute_moves(rm_robot_handle *handle, rm_pose_t *positions, int num_positions, int speed, int block) {
    rm_pose_t rm_pose;

    for (int i = 0; i < num_positions; ++i) {
        rm_pose.position.x = positions[i].position.x;
        rm_pose.position.y = positions[i].position.y;
        rm_pose.position.z = positions[i].position.z;

        rm_pose.quaternion.w = 0.0f;
        rm_pose.quaternion.x = 0.0f;
        rm_pose.quaternion.y = 0.0f;
        rm_pose.quaternion.z = 0.0f;

        rm_pose.euler.rx = positions[i].euler.rx;
        rm_pose.euler.ry = positions[i].euler.ry;
        rm_pose.euler.rz = positions[i].euler.rz;

        int trajectory_connect = (i < num_positions - 1) ? 1 : 0;
        printf("Trajectory Connect Value at Step %d: %d\n", i, trajectory_connect);

        int result = robotic_arm.rm_moves(handle, rm_pose, speed, 0, trajectory_connect, block );
        if(result != 0)
        {
            printf("Trajectory Connect Value at Step %d: %d\n", i, trajectory_connect);
            return;

        }


    }
    printf("moves operation succeeded\n");
}


int main(int argc, char *argv[]) {

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

    float joint_angles_start[ARM_DOF] = {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f};
    result = robotic_arm.rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
    if(result != 0)
    {
        return -1;
    }
    rm_pose_t pose;
    pose.position.x = -0.3f;
    pose.position.y = 0.0f;
    pose.position.z = 0.3f;
    pose.euler.rx = 3.14f;
    pose.euler.ry = 0.0f;
    pose.euler.rz = 0.0f;
    pose.quaternion = {0.0f, 0.0f, 0.0f, 0.0f};
    result = robotic_arm.rm_movej_p(robot_handle, pose, 20, 0, 0, 1);
    if(result != 0)
    {
        return -1;
    }

    rm_pose_t move_positions[] = {
            {{-0.3f, 0.0f, 0.3f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.14f, 0.0f, 0.0f}},  // 默认四元数
            {{-0.27f, -0.22f, 0.3f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.14f, 0.0f, 0.0f}},
            {{-0.314f, -0.25f, 0.2f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.14f, 0.0f, 0.0f}},
            {{-0.239f, 0.166f, 0.276f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.14f, 0.0f, 0.0f}},
            {{-0.239f, 0.264f, 0.126f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.14f, 0.0f, 0.0f}}
    };
    int num_positions = sizeof(move_positions) / sizeof(move_positions[0]);

    execute_moves(robot_handle, move_positions, num_positions, 20, 1);

    // Disconnect from the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if(result != 0)
    {
        return -1;
    }
}
