import sys
import os

# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Robotic_Arm.rm_robot_interface import *


class RobotArmController:
    def __init__(self, ip, port=0, level=3, mode=2):
        """Initialize and connect to the robotic arm.

        Args:
            ip (str): IP address of the robot arm.
            port (int): Port number.
            level (int, optional): Connection level. Defaults to 3.
            mode (int, optional): Thread mode (0: single, 1: dual, 2: triple). Defaults to 2.
        """
        self.thread_mode = rm_thread_mode_e(mode)
        self.robot = RoboticArm(self.thread_mode)
        self.handle = self.robot.rm_create_robot_arm(ip, port, level)

        if self.handle.id == -1:
            print("\nFailed to connect to the robot arm\n")
            exit(1)
        else:
            print(f"\nSuccessfully connected to the robot arm: {self.handle.id}\n")

    def disconnect(self):
        """Disconnect from the robot arm.

        Returns:
            None
        """
        handle = self.robot.rm_delete_robot_arm()
        if handle == 0:
            print("\nSuccessfully disconnected from the robot arm\n")
        else:
            print("\nFailed to disconnect from the robot arm\n")

    def set_modbus_mode(self, port=0, baudrate=115200, timeout=1):
        """Set the Modbus RTU mode.

        Args:
            port (int): Communication port. 0 for controller RS485 port as RTU master, 1 for end interface board RS485 port as RTU master, 2 for controller RS485 port as RTU slave.
            baudrate (int): Baud rate. Supports 9600, 115200, 460800.
            timeout (int): Timeout duration in hundred milliseconds. For all read and write commands to Modbus devices, if no response data is returned within the specified timeout period, a timeout error is returned. The timeout cannot be 0; if set to 0, the robot arm will configure it as 1.

        Returns:
            None
        """
        set_result = self.robot.rm_set_modbus_mode(port, baudrate, timeout)
        if set_result == 0:
            print("\nSuccessfully set the Modbus mode\n")
        else:
            print("\nFailed to set the Modbus mode\n")

    def close_modbus_mode(self, port=0):
        """Close the Modbus RTU mode.

        Args:
            port (int): Communication port. 0 for controller RS485 port, 1 for end interface board RS485 port, 3 for controller ModbusTCP device.

        Returns:
            None
        """
        close_result = self.robot.rm_close_modbus_mode(port)
        if close_result == 0:
            print("\nSuccessfully closed the Modbus mode\n")
        else:
            print("\nFailed to close the Modbus mode\n")

    def read_coils(self, port=0, address=0, device=2, num=1):
        """Read the coils from the Modbus device.

        Args:
            port (int): Communication port. 0 for controller RS485 port, 1 for end interface board RS485 port, 3 for controller ModbusTCP device.
            address (int): Starting address of the data. Defaults to 0.
            device (int): Peripheral device address. Defaults to 2.
            num (int): Number of data points to read. Defaults to 1.

        Returns:
            None
        """
        read_params = rm_peripheral_read_write_params_t(port, address, device, num)
        tag = self.robot.rm_read_coils(read_params)
        if tag[0] == 0:
            print(f"\nSuccessfully read the coils, data: {tag[1]}\n")
        else:
            print("\nFailed to read the coils\n")

    def write_single_coil(self, data, port=0, address=0, device=2, num=1):
        """Write a single coil to the Modbus device.

        Args:
            data (int): Data to write to the coil.
            port (int): Communication port. 0 for controller RS485 port, 1 for end interface board RS485 port, 3 for controller ModbusTCP device.
            address (int): Starting address of the data. Defaults to 0.
            device (int): Peripheral device address. Defaults to 2.
            num (int): Number of data points to write. Defaults to 1.

        Returns:
            None
        """
        write_params = rm_peripheral_read_write_params_t(port, address, device, num)
        tag = self.robot.rm_write_single_coil(write_params, data)
        if tag == 0:
            print("\nSuccessfully wrote the single coil\n")
        else:
            print("\nFailed to write the single coil\n")

    def write_single_register(self, data, port=0, address=0, device=2):
        """Write a single register to the Modbus device.

        Args:
            data (int): Data to write to the register.
            port (int): Communication port. 0 for controller RS485 port, 1 for end interface board RS485 port, 3 for controller ModbusTCP device.
            address (int): Starting address of the data. Defaults to 0.
            device (int): Peripheral device address. Defaults to 2.

        Returns:
            None
        """
        write_params = rm_peripheral_read_write_params_t(port, address, device)
        tag = self.robot.rm_write_single_register(write_params, data)
        if tag == 0:
            print("\nSuccessfully wrote the single register\n")
        else:
            print("\nFailed to write the single register\n")

    def read_holding_registers(self, port=0, address=0, device=2):
        """Read the holding registers from the Modbus device.

        Args:
            port (int): Communication port. 0 for controller RS485 port, 1 for end interface board RS485 port, 3 for controller ModbusTCP device.
            address (int): Starting address of the data. Defaults to 0.
            device (int): Peripheral device address. Defaults to 2.

        Returns:
            None
        """
        read_params = rm_peripheral_read_write_params_t(port, address, device)
        tag = self.robot.rm_read_holding_registers(read_params)
        if tag[0] == 0:
            print(f"\nSuccessfully read the holding registers, data: {tag[1]}\n")
        else:
            print("\nFailed to read the holding registers\n")


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Set Modbus mode
    robot_controller.set_modbus_mode()

    # Write a single coil
    robot_controller.write_single_coil(1)

    # Read coils
    robot_controller.read_coils()

    # Write a single register
    robot_controller.write_single_register(180)

    # Read holding registers
    robot_controller.read_holding_registers()

    # Close Modbus mode
    robot_controller.close_modbus_mode()

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
