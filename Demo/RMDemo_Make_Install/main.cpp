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

#define POINT_NUM 5

typedef struct
{
    float joint_angles[ARM_DOF];
    rm_pose_t pose;
    rm_pose_t point_list[POINT_NUM];
}ArmModelData;

ArmModelData arm_data[9] = {
    {
        .joint_angles = {0, 0, 0, 0, 0, 0}, 
        .pose = { .position = {-0.3, 0, 0.3}, .euler = {3.14, 0, 0}},
        .point_list = { {.position = {-0.3, 0, 0.3}, .euler = {3.14, 0, 0}},
                        {.position = {-0.27, -0.22,0.3}, .euler = {3.14, 0, 0}},
                        {.position = {-0.314, -0.25, 0.2}, .euler = {3.14, 0, 0}},
                        {.position = {-0.239, 0.166, 0.276}, .euler = {3.14, 0, 0}},
                        {.position = {-0.239, 0.264, 0.126}, .euler = {3.14, 0, 0}},}
    },
    {
        .joint_angles = {0, 20, 0, 70, 0, 90, 0},  
        .pose = { .position = {0.297557, 0, 0.337061}, .euler = {3.142, 0, 3.142} } ,
        .point_list = { {.position = {0.3, 0.1, 0.337061}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.2, 0.3, 0.237061}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.2, 0.25, 0.037061}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.1, 0.3, 0.137061}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.2, 0.25, 0.337061}, .euler = {3.142, 0, 3.142}}, }
    
    }, 
    {0},
    {  
        .joint_angles = {0, 20, 70, 0, 90, 0},
        .pose = { .position = {0.448968, 0, 0.345083}, .euler = {3.14, 0, 3.142} },
        .point_list = { {.position = {0.3, 0.3, 0.345083}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.3, 0.4, 0.145083}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.3, 0.2, 0.045083}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.4, 0.1, 0.145083}, .euler = {3.142, 0, 3.142}},
                        {.position = {0.5, 0, 0.345083}, .euler = {3.142, 0, 3.142}}, }
    
    },
    {0},
    {  
        .joint_angles = {0, 20, 70, 0, -90, 0},
        .pose = { .position = {0.352925, -0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
        .point_list = { {.position = {0.3, 0.3, 0.327320}, .euler = {3.141, 0, -1.57}},
                        {.position = {0.2, 0.4, 0.127320}, .euler = {3.141, 0, -1.57}},
                        {.position = {0.2, 0.2, 0.027320}, .euler = {3.141, 0, -1.57}},
                        {.position = {0.3, 0.1, 0.227320}, .euler = {3.141, 0, -1.57}},
                        {.position = {0.4, 0, 0.327320}, .euler = {3.141, 0, -1.57}}, }
    
    },
    {
        0
    },
    {  
        .joint_angles = {0, 0, 0, -90, 0, 0, 0},
        .pose = { .position = {0.359500, 0, 0.426500}, .euler = {3.142, 0, 0} } ,
        .point_list = { {.position = {0.359500, 0, 0.426500}, .euler = {3.142, 0, 0}},
                        {.position = {0.2, 0.3, 0.426500}, .euler = {3.142, 0, 0}},
                        {.position = {0.2, 0.3, 0.3}, .euler = {3.142, 0, 0}},
                        {.position = {0.3, 0.3, 0.3}, .euler = {3.142, 0, 0}},
                        {.position = {0.3, -0.1, 0.4}, .euler = {3.142, 0, 0}} }
    
    },
    {  
        .joint_angles = {0, 20, 70, 0, -90, 0},
        .pose = { .position = {0.544228, -0.058900, 0.468274}, .euler = {3.142, 0, -1.571} },
        .point_list = { {.position = {0.3, 0.3, 0.468274}, .euler = {3.142, 0, -1.571}},
                        {.position = {0.3, 0.4, 0.168274}, .euler = {3.142, 0, -1.571}},
                        {.position = {0.3, 0.2, 0.268274}, .euler = {3.142, 0, -1.571}},
                        {.position = {0.4, 0.1, 0.368274}, .euler = {3.142, 0, -1.571}},
                        {.position = {0.5, 0, 0.468274}, .euler = {3.142, 0, -1.571}} }
    
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

class My_RM_Service: public RM_Service
{
    public:
        My_RM_Service(){
        };

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

                int result = rm_moves(handle, rm_pose, speed, 0, trajectory_connect, block );
                if(result != 0)
                {
                    printf("Trajectory Connect Value at Step %d: %d\n", i, trajectory_connect);
                    return;
                }
            }
            printf("moves operation succeeded\n");
        }
};


int main(int argc, char *argv[]) {
    My_RM_Service robotic_arm;
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

    robotic_arm.rm_movej_p(robot_handle, arm_data[arm_info.arm_model].pose, 20, 0, 0, 1);

    robotic_arm.execute_moves(robot_handle, arm_data[arm_info.arm_model].point_list, POINT_NUM, 20, 1);
    
}
