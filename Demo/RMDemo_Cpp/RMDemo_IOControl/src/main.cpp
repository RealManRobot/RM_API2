#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#ifdef _WIN32
#include <windows.h>  // Include for Sleep function
#define SLEEP(ms) Sleep(ms)
#include <io.h>
#define F_OK 0
#define access _access
#define localtime_r(timep, result) localtime_s(result, timep)  // Use localtime_s as a replacement
#else
#include <limits.h>  
#include <unistd.h>
#define SLEEP(ms) usleep((ms) * 1000)
#endif

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
int check_result(int result, const char *error_message) {
    if (result != 0) {
        printf("%s Error code: %d.\n", error_message, result);
        return -1;
    }
    return 0;
}

// Drag teach
void Drag_teach(rm_robot_handle *handle, int trajectory_record, int *save_id) {
    int result = robotic_arm.rm_start_drag_teach(handle, trajectory_record);
    if (result == 0) {
        printf("Drag teaching started\n");
    } else {
        printf("Failed to start drag teaching\n");
    }

    printf("Drag teaching has started, complete the drag operation and press Enter to continue...\n");
    getchar();

    // Get user input for save_id
    printf("Please enter a Save ID for this teaching session: ");
    scanf("%d", save_id);
    printf("Save ID { %d } for this teaching session saved to the controller\n", *save_id);

    result = robotic_arm.rm_stop_drag_teach(handle);
    if (result == 0) {
        printf("Drag teaching stopped\n");
    } else {
        printf("Failed to stop drag teaching\n");
    }
}

// Add lines to file
void add_lines_to_file(rm_robot_handle *handle, const char *file_path, const char *project_path, int type_value) {
    rm_robot_info_t robot_info;
    int result = robotic_arm.rm_get_robot_info(handle, &robot_info);
    if (result != 0) {
        printf("Failed to get robot info\n");
        return;
    }
    int file_value = 0;
    if (robot_info.arm_dof == 6) {
        file_value = 6;
    } else if (robot_info.arm_dof == 7) {
        file_value = 7;
    } else {
        printf("Invalid degree of freedom, must be 6 or 7\n");
        return;
    }
    FILE *fp_read, *fp_write;  
    char buffer[1024];
    char line1[50];
    char line2[100];

    snprintf(line1, sizeof(line1), "{\"file\":%d}\n", file_value);
    snprintf(line2, sizeof(line2), "{\"name\":\"Folder\",\"num\":1,\"type\":%d,\"enabled\":true,\"parent_number\":0}\n", type_value);

    fp_read = fopen(file_path, "r");  
    if (fp_read == NULL) {  
        printf("Failed to open file: %s\n", file_path);  
        return;  
    }  

    // 打开新文件用于写入  
    fp_write = fopen(project_path, "w");  
    if (fp_write == NULL) {  
        fclose(fp_read);  
        perror("Error opening file");  
        return;  
    }  

    fprintf(fp_write, "%s", line1);  
    fprintf(fp_write, "%s", line2);  
    
    fseek(fp_read, 0, SEEK_END);  
    long original_content_size = ftell(fp_read);  
    int real_len = 0;
    fseek(fp_read, 0, SEEK_SET);  
    
    while (fgets(buffer, 1024, fp_read) != NULL) {  
        fputs(buffer, fp_write);  
    }  

    fclose(fp_read);  
    fclose(fp_write);  
}

// Send project file
void send_project(rm_robot_handle *handle, const char *file_path, int plan_speed, int only_save, int save_id, int step_flag, int auto_start, int project_type) {
    if (access(file_path, F_OK) == -1) {
        printf("File path does not exist: %s\n", file_path);
        return;
    }

    rm_send_project_t send_project = {
            "",
            (int)strlen(file_path),  // Cast to int
            plan_speed,
            only_save,
            save_id,
            step_flag,
            auto_start,
            project_type
    };
    strncpy(send_project.project_path, file_path, sizeof(send_project.project_path) - 1);
    send_project.project_path[sizeof(send_project.project_path) - 1] = '\0';

    int errline;
    int result = robotic_arm.rm_send_project(handle, send_project, &errline);
    if (result == 0) {
        printf("Project sent and run successfully\n");
    } else {
        printf("Failed to send project, error code: %d\n", result);
    }
}

// Get program run state
void get_program_run_state(rm_robot_handle *handle, int time_sleep, int max_retries) {
    int retries = 0;
    while (retries < max_retries) {
        SLEEP(time_sleep * 1000);
        rm_program_run_state_t run_state;
        int result = robotic_arm.rm_get_program_run_state(handle, &run_state);

        if (result == 0) {
            printf("Program running state: %d\n", run_state.run_state);
            if (run_state.run_state == 0) {
                printf("Program has ended\n");
                break;
            }
        } else {
            printf("Failed to query, error code: %d\n", result);
        }

        retries++;
    }

    if (retries == max_retries) {
        printf("Reached maximum query attempts, exiting\n");
    }
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

    int save_id;
    Drag_teach(robot_handle, 1, &save_id);

    // Save trajectory
    int lines;
    result = robotic_arm.rm_save_trajectory(robot_handle, TRAJECTORY_FILE_PATH, &lines);
    if (result == 0) {
        printf("Trajectory saved successfully, total number of points: %d\n", lines);
    } else {
        printf("Failed to save drag teaching\n");
    }

    // Add lines to file
    add_lines_to_file(robot_handle, TRAJECTORY_FILE_PATH, PROJECT_FILE_PATH, lines);

    // Send file and query running status
    send_project(robot_handle, PROJECT_FILE_PATH, 20, 1, 20, 0, 0, 0);

    // Set the default run program
    result = robotic_arm.rm_set_default_run_program(robot_handle, 20);
    if (check_result(result, "Failed to set default run program") != 0) {
        return -1;
    }

    // Set IO modes
    int io_mode = 2;
    result = robotic_arm.rm_set_IO_mode(robot_handle, 1, io_mode);  // Set IO mode to input start function multiplexing mode
    if (check_result(result, "Failed to set IO mode for input start function") != 0) {
        return -1;
    }
    io_mode = 3;
    result = robotic_arm.rm_set_IO_mode(robot_handle, 2, io_mode);  // Set IO mode to input pause function multiplexing mode
    if (check_result(result, "Failed to set IO mode for input pause function") != 0) {
        return -1;
    }
    io_mode = 4;
    result = robotic_arm.rm_set_IO_mode(robot_handle, 3, io_mode);  // Set IO mode to input continue function multiplexing mode
    if (check_result(result, "Failed to set IO mode for input continue function") != 0) {
        return -1;
    }
    io_mode = 5;
    result = robotic_arm.rm_set_IO_mode(robot_handle, 4, io_mode);  // Set IO mode to input emergency stop function multiplexing mode
    if (check_result(result, "Failed to set IO mode for input emergency stop function") != 0) {
        return -1;
    }

    // Disconnect the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }
}
