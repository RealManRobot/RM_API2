#include <stdio.h>
#include "rm_interface.h"
#include "string.h"
#include <stdarg.h>
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

    // 给夹爪上电
    result = rm_set_tool_voltage(robot_handle, 3);
    if(result != 0)
    {
        return -1;
    }

    // 初始位置，第一支试管的位置
    rm_pose_t pose;
    pose.position.x = -0.35f;
    pose.position.y = -0.03f;
    pose.position.z = 0.3f;
    pose.euler.rx = 3.14f;
    pose.euler.ry = 0.0f;
    pose.euler.rz = 0.0f;
    pose.quaternion = (rm_quat_t){0.0f, 0.0f, 0.0f, 0.0f};
    result = rm_movej_p(robot_handle, pose, 20, 0, 0, 1);
    if(result != 0)
    {
        return -1;
    }
    
    float x_step = 0.025f; // 当前工作坐标系x轴方向，试管距离为0.025m
    float y_step = 0.03f; // 当前工作坐标系y轴方向，试管距离为0.03m

    // 试管架为6*4
    // 使用机械臂步进运动功能，模拟将试管移动到试管架各孔位
    for(int i=0; i<4; i++)
    {
        result = rm_set_gripper_pick_on(robot_handle, 500, 200, 0, 0);
        if(result != 0)
        {
            return -1;
        }
        SLEEP_S(1);

        for(int j=0;j<6;j++)
        {
            result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, 0.05f, 20, 1);
            if(result != 0)
            {
                return -1;
            }  
            if(i%2 == 0)
            {
                result = rm_set_pos_step(robot_handle, RM_Y_DIR_E, y_step, 20, 1);
                if(result != 0)
                {
                    return -1;
                }
            }
            else{               
                result = rm_set_pos_step(robot_handle, RM_Y_DIR_E, 0-y_step, 20, 1);
                if(result != 0)
                {
                    return -1;
                }                
            }
            result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, -0.05f, 20, 1);
            if(result != 0)
            {
                return -1;
            }
            result = rm_set_gripper_release(robot_handle, 500, 0, 0);
            if(result != 0)
            {
                return -1;
            }
            SLEEP_S(1);
            result = rm_set_gripper_pick_on(robot_handle, 500, 200, 0, 0);
            if(result != 0)
            {
                return -1;
            }
            SLEEP_S(1);
            
        }
        result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, 0.05f, 20, 1);
        if(result != 0)
        {
            return -1;
        }   
        result = rm_set_pos_step(robot_handle, RM_X_DIR_E, x_step, 20, 1);
        if(result != 0)
        {
            return -1;
        }   
        if(i!=3)
        {
            result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, -0.05f, 20, 1);
            if(result != 0)
            {
                return -1;
            }   
        }
    }

    
    // 机械臂当前位置为试管架第四行第一列，使用机械臂直线运动功能，将试管放置到试管架第一个位置
    rm_current_arm_state_t cur_state;
    result = rm_get_current_arm_state(robot_handle, &cur_state);
    if(result != 0)
    {
        return -1;
    }
    cur_state.pose.position.x -= 4*x_step;
    // cur_state.pose.position.y += y_step;
    result = rm_movel(robot_handle, cur_state.pose, 20, 0, 0, 1);
    if(result != 0)
    {
        return -1;
    }
    result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, -0.05f, 20, 1);
    if(result != 0)
    {
        return -1;
    } 
    result = rm_set_gripper_release(robot_handle, 500, 0, 0);
    if(result != 0)
    {
        return -1;
    }
    SLEEP_S(1);
    result = rm_set_gripper_pick_on(robot_handle, 500, 200, 0, 0);
    if(result != 0)
    {
        return -1;
    }
    SLEEP_S(1);
    result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, 0.05f, 20, 1);
    if(result != 0)
    {
        return -1;
    } 

    // 使用机械臂直线运动规划功能，将试管放置到第三行第三列
    cur_state.pose.position.x += 2*x_step;
    cur_state.pose.position.y += 2*y_step;
    result = rm_movel(robot_handle, cur_state.pose, 20, 0, 0, 1);
    if(result != 0)
    {
        return -1;
    }
    result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, -0.05f, 20, 1);
    if(result != 0)
    {
        return -1;
    } 
    result = rm_set_gripper_release(robot_handle, 500, 0, 0);
    if(result != 0)
    {
        return -1;
    }
    SLEEP_S(1);
    result = rm_set_pos_step(robot_handle, RM_Z_DIR_E, 0.05f, 20, 1);
    if(result != 0)
    {
        return -1;
    } 
    // Disconnect the robotic arm
    result = rm_delete_robot_arm(robot_handle);
    if(result != 0) {
        return -1;
    }

    printf("RMDemo_TubePickingSimulation run finished!\n");
}
