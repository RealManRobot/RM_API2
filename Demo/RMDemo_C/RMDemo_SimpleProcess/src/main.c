#include <stdio.h>
#include "rm_interface.h"
// Windows-specific headers and definitions
#ifdef _WIN32
#define SLEEP_MS(ms) Sleep(ms)
#define SLEEP_S(s) Sleep((s) * 1000)
#define usleep(us) Sleep((us) / 1000)  // No usleep, use Sleep instead
// Linux-specific headers and definitions
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
    rm_arm_software_version_t software_info;
    result = rm_get_arm_software_info(robot_handle, &software_info);
    if (result == 0) {
        printf("================== Arm Software Information ==================\n");
        printf("Arm Model:  %s\n", software_info.product_version);
        printf("Algorithm Library Version:  %s\n", software_info.algorithm_info.version);
        printf("Control Layer Software Version:  %s\n", software_info.ctrl_info.version);
        printf("Dynamics Version:  %s\n", software_info.dynamic_info.model_version);
        printf("Planning Layer Software Version:  %s\n", software_info.plan_info.version);
        printf("==============================================================\n");
    }

    float joint_angles_start[6] = {0.0, 20, 70.0, 0.0, 90.0, 0.0};
    rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);

    rm_pose_t pose_movej_p = {{0.3, 0, 0.3}, {0, 0, 0, 0}, {3.14, 0, 0}};
    rm_movej_p(robot_handle, pose_movej_p, 20, 0, 0, 1);

    rm_pose_t pose = {{0.2, 0, 0.3}, {0, 0, 0, 0}, {3.14, 0, 0}};
    rm_movel(robot_handle, pose, 20, 0, 0, 1);

    rm_pose_t pose_movej_p2 = {{0.3, 0, 0.3}, {0, 0, 0, 0}, {3.14, 0, 0}};
    rm_movej_p(robot_handle, pose_movej_p2, 20, 0, 0, 1);

    rm_pose_t pose_via = {{0.2, 0.05, 0.3}, {0, 0, 0, 0}, {3.14, 0, 0}};
    rm_pose_t pose_to = {{0.2, -0.05, 0.3}, {0, 0, 0, 0}, {3.14, 0, 0}};
    rm_movec(robot_handle, pose_via, pose_to, 20, 2, 0, 0, 1);


}
