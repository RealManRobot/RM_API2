import sys
import os

# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Robotic_Arm.rm_robot_interface import *


class RobotArmController:
    def __init__(self, ip, port, level=3, mode=2):
        """
        Initialize and connect to the robotic arm.

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
        """
        Disconnect from the robot arm.

        Returns:
            None
        """
        handle = self.robot.rm_delete_robot_arm()
        if handle == 0:
            print("\nSuccessfully disconnected from the robot arm\n")
        else:
            print("\nFailed to disconnect from the robot arm\n")

    def set_manual_work_frame(self, name=None, pose=None):
        """
        Manually set the work frame.

        Args:
            name (str, optional): Name of the work frame. Defaults to None.
            pose (list or tuple, optional): Position and Euler angles as [x, y, z, rx, ry, rz]. Defaults to None.

        Returns:
            None
        """
        result = self.robot.rm_set_manual_work_frame(name, pose)
        if result == 0:
            print("\nManually set work frame succeeded\n")
        else:
            print("\nManually set work frame failed, error code: ", result, "\n")

    def delete_work_frame(self, name=None):
        """
        Delete the work frame.

        Args:
            name (str, optional): Name of the work frame. Defaults to None.

        Returns:
            None
        """
        result = self.robot.rm_delete_work_frame(name)
        if result == 0:
            print("\nDelete work frame succeeded\n")
        else:
            print("\nDelete work frame failed, error code: ", result, "\n")

    def update_work_frame(self, name=None, pose=None):
        """
        Update the work frame.

        Args:
            name (str, optional): Name of the work frame. Defaults to None.
            pose (list or tuple, optional): Position and Euler angles as [x, y, z, rx, ry, rz]. Defaults to None.

        Returns:
            None
        """

        result = self.robot.rm_update_work_frame(name, pose)
        if result == 0:
            print("\nUpdate work frame succeeded\n")
        else:
            print("\nUpdate work frame failed, error code: ", result, "\n")

    def get_given_work_frame(self, name=None):
        """
        Get the given work frame.

        Args:
            name (str, optional): Name of the work frame. Defaults to None.

        Returns:
            None
        """
        result = self.robot.rm_get_given_work_frame(name)
        if result[0] == 0:
            print("\nGet work frame succeeded: ", result[1], "\n")
        else:
            print("\nGet work frame failed, error code: ", result[0], "\n")


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Set manual work frame
    robot_controller.set_manual_work_frame("test", [0, 0, 0, 0, 0, 0])

    # Update work frame
    robot_controller.update_work_frame("test", [0.3, 0, 0.3, 3.142, 0, 0])

    # Get given work frame
    robot_controller.get_given_work_frame("test")

    # Delete work frame
    robot_controller.delete_work_frame("test")

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
