#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#ifdef _WIN32
#include <windows.h> 
#define SLEEP(ms) Sleep(ms)
#include <io.h>
#define F_OK 0
#define access _access
#define localtime_r(timep, result) localtime_s(result, timep)  // Use localtime_s as a replacement
#else
#include <unistd.h>
#define SLEEP(ms) usleep((ms) * 1000)
#endif

#include "rm_service.h"
RM_Service robotic_arm;

// Custom log function
void custom_api_log(const char* message, va_list args) {
    if (!message) {
        fprintf(stderr, "Error: message is a null pointer\n");
        return;
    }

    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), message, args);
    printf("%s\n", buffer);
}

// Start drag teach
void start_drag_teach(rm_robot_handle *handle, int trajectory_record, int *save_id) {
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

// Save trajectory
int save_trajectory(rm_robot_handle *handle, const char *file_path, int wait_time) {
    int num_points;
    int result;
    time_t start_time = time(NULL);

    while (1) {
        result = robotic_arm.rm_save_trajectory(handle, (char *)file_path, &num_points);
        if (result == 0) {
            printf("Trajectory saved successfully, total number of points: %d\n", num_points);
            return num_points;
        }

        if (difftime(time(NULL), start_time) >= wait_time) {
            printf("Failed to save trajectory within the timeout period\n");
            return -1;
        }

        SLEEP(1000); // Check once per second
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

    // Construct lines with \r\n line endings
    snprintf(line1, sizeof(line1), "{\"file\":%d}\r\n", file_value);
    snprintf(line2, sizeof(line2), "{\"name\":\"Folder\",\"num\":1,\"type\":%d,\"enabled\":true,\"parent_number\":0}\r\n", type_value);

    // Open the original file for reading
    fp_read = fopen(file_path, "r");  
    if (fp_read == NULL) {  
        printf("Failed to open file: %s\n", file_path);  
        return;  
    }  

    // Open the new file for writing  
    fp_write = fopen(project_path, "w");  
    if (fp_write == NULL) {  
        fclose(fp_read);  
        perror("Error opening file");  
        return;  
    }  

    // Write the new lines to the file
    fprintf(fp_write, "%s", line1);  
    fprintf(fp_write, "%s", line2);  
    
    // Set the file pointer to the beginning
    fseek(fp_read, 0, SEEK_SET);  
    
    // Write the original content to the new file, ensuring each line ends with \r\n
    while (fgets(buffer, sizeof(buffer), fp_read) != NULL) {  
        // Replace \n with \r\n if found
        char *pos;
        if ((pos = strchr(buffer, '\n')) != NULL) {
            *pos = '\0'; // Remove \n
            fprintf(fp_write, "%s\r\n", buffer); // Write \r\n
        } else {
            fputs(buffer, fp_write); // Write the line as is if no \n found
        }
    }  

    // Close the files
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
        if (errline == -1) {
            printf("Project sent and run successfully\n");
        } else if (errline == 0) {
            printf("Project sent successfully but not run, data length verification failed\n");
        } else {
            printf("Project sent successfully but run failed, problematic project lines: %d\n", errline);
        }
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

    // Set log callback
    robotic_arm.rm_set_log_call_back(custom_api_log, 3);

    // Initialize
    result = robotic_arm.rm_init(RM_TRIPLE_MODE_E);
    if (result != 0) {
        printf("Initialization failed with error code: %d.\n", result);
        return -1;
    }

    char *api_version = robotic_arm.rm_api_version();
    printf("API Version: %s.\n", api_version);

    // Create robot handle
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = robotic_arm.rm_create_robot_arm(robot_ip_address, robot_port);
    if (robot_handle == NULL) {
        printf("Failed to create robot handle.\n");
        return -1;
    } else {
        printf("Robot handle created successfully: %d\n", robot_handle->id);
    }

    // Drag teach
    int save_id;
    start_drag_teach(robot_handle, 1, &save_id);

    // Save trajectory
    int timeout = 20;  // Wait for 20 seconds
    int lines = save_trajectory(robot_handle, TRAJECTORY_FILE_PATH, timeout);

    // Add lines to file
    add_lines_to_file(robot_handle, TRAJECTORY_FILE_PATH, PROJECT_FILE_PATH, lines);

    // Send file and query running status
    send_project(robot_handle, PROJECT_FILE_PATH, 20, 0, save_id, 0, 0, 0);

    // Query program running status
    get_program_run_state(robot_handle, 1, 5);

    // Pause the robotic arm
    robotic_arm.rm_set_arm_pause(robot_handle);
    SLEEP(3000); // Pause for 3 seconds

    // Query program running status
    get_program_run_state(robot_handle, 1, 5);

    // Continue the robotic arm
    robotic_arm.rm_set_arm_continue(robot_handle);

    // Query program running status
    get_program_run_state(robot_handle, 1, 5);

    // Disconnect the robotic arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if(result != 0) {
        return -1;
    }

    return 0;
}
