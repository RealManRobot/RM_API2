#include <stdio.h>
#include "rm_service.h"
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

typedef struct
{
    float joint_angles[ARM_DOF];
    rm_pose_t movej_pose1;
    rm_pose_t movel_pose;
    rm_pose_t movej_pose2;
    rm_pose_t movec_pose_via;
    rm_pose_t movec_pose_to;
}ArmModelData;
ArmModelData arm_data[9] = {
    {
        {0, 20, 70, 0, 90, 0},
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
        {{0.2, 0.05, 0.3}, {0,0,0,0},{3.14, 0, 0} },
        {{0.2, -0.05, 0.3}, {0,0,0,0},{3.14, 0, 0} }
    },
    {
        {0, 20, 0, 70, 0, 90, 0},  
        {{0.297557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
        {{0.097557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
        {{0.297557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
        {{0.257557, -0.08, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
        {{0.257557, 0.08, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } 
    }, 
    {0},
    {  
        {0, 20, 70, 0, 90, 0},  
        {{0.448968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
        {{0.248968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
        {{0.448968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
        {{0.408968, -0.1, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
        {{0.408968, 0.1, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} }
    },
    {0},
    {  
        {0, 20, 70, 0, -90, 0},  
        {{0.352925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
        {{0.152925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
        {{0.352925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
        {{0.302925, -0.158880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
        {{0.302925, 0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } 
    },
    {

    },
    {  
        {0, 0, 0, -90, 0, 0, 0},  
        {{0.1, 0, 0.4},{0,0,0,0}, {3.14, 0, 0} } ,
        {{0.3, 0, 0.4},{0,0,0,0}, {3.14, 0, 0} } ,
        {{0.3595, 0, 0.4265},{0,0,0,0}, {3.14, 0, 0} } ,
        {{0.3595, 0.03, 0.4265},{0,0,0,0}, {3.14, 0, 0} } ,
        {{0.3595, 0.03, 0.4665},{0,0,0,0}, {3.14, 0, 0} } 
    },
    {  
        {0, 20, 70, 0, -90, 0},  
        {{0.544228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
        {{0.344228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
        {{0.544228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
        {{0.504228, -0.108900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
        {{0.504228, -0.008900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} }
    }
};

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
    rm_arm_software_version_t software_info;
    result = robotic_arm.rm_get_arm_software_info(robot_handle, &software_info);
    if (result == 0) {
        printf("================== Arm Software Information ==================\n");
        printf("Arm Model:  %s\n", software_info.product_version);
        printf("Algorithm Library Version:  %s\n", software_info.algorithm_info.version);
        printf("Control Layer Software Version:  %s\n", software_info.ctrl_info.version);
        printf("Dynamics Version:  %s\n", software_info.dynamic_info.model_version);
        printf("Planning Layer Software Version:  %s\n", software_info.plan_info.version);
        printf("==============================================================\n");
    }
    
    rm_robot_info_t arm_info;
    result = rm_get_robot_info(robot_handle, &arm_info);
    if(result != 0)
    {
        return -1;
    }

    robotic_arm.rm_movej(robot_handle, arm_data[arm_info.arm_model].joint_angles, 20, 0, 0, 1);

    robotic_arm.rm_movej_p(robot_handle, arm_data[arm_info.arm_model].movej_pose1, 20, 0, 0, 1);

    robotic_arm.rm_movel(robot_handle, arm_data[arm_info.arm_model].movel_pose, 20, 0, 0, 1);

    robotic_arm.rm_movej_p(robot_handle, arm_data[arm_info.arm_model].movej_pose2, 20, 0, 0, 1);

    robotic_arm.rm_movec(robot_handle, arm_data[arm_info.arm_model].movec_pose_via, arm_data[arm_info.arm_model].movec_pose_to, 20, 2, 0, 0, 1);


}
