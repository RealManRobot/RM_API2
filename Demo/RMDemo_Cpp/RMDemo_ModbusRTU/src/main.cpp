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

    // Set ModbusRTU mode
    result = robotic_arm.rm_set_modbus_mode(robot_handle, 0, 115200, 10);
    if (check_result(result, "Failed to set ModbusRTU mode") != 0) {
        return -1;
    }

    // Write single coil data
    rm_peripheral_read_write_params_t write_params = {0, 0, 2, 1};
    result = robotic_arm.rm_write_single_coil(robot_handle, write_params, 1);
    if (check_result(result, "Failed to write single coil data") != 0) {
        return -1;
    }

    // Read coils
    rm_peripheral_read_write_params_t read_params = {0, 0, 2, 1};
    int coil_data;
    result = robotic_arm.rm_read_coils(robot_handle, read_params, &coil_data);
    if (check_result(result, "Failed to read coils data") != 0) {
        return -1;
    }

    // Reset single coil data
    rm_peripheral_read_write_params_t write_single_coil_params = { 0, 0, 2, 1};
    result = robotic_arm.rm_write_single_coil(robot_handle, write_single_coil_params, 1);
    if (check_result(result, "Failed to reset single coil data") != 0) {
        return -1;
    }

    // Write single register
    rm_peripheral_read_write_params_t write_single_register_params = { 0, 0, 2, 1};
    result = robotic_arm.rm_write_single_register(robot_handle, write_single_register_params, 180);
    if (check_result(result, "Failed to write single register") != 0) {
        return -1;
    }
    
    // Read holding registers
    rm_peripheral_read_write_params_t holding_registers_params = {0, 0, 2, 1};
    int holding_register_data;
    result = robotic_arm.rm_read_holding_registers(robot_handle, holding_registers_params, &holding_register_data);
    if (check_result(result, "Failed to read holding registers") != 0) {
        return -1;
    }

    // Close Modbus mode
    result = robotic_arm.rm_close_modbus_mode(robot_handle, 0);
    if (check_result(result, "Failed to close Modbus mode") != 0) {
        return -1;
    }

    // Disconnect from the robot arm
    result = robotic_arm.rm_delete_robot_arm(robot_handle);
    if (check_result(result, "Failed to disconnect the robot arm") != 0) {
        return -1;
    }
}
