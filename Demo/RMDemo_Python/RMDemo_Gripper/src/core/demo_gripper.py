import sys
import os
import time

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

    def movej(self, joint, v=20, r=0, connect=0, block=1):
        """
        Perform movej motion.

        Args:
            joint (list of float): Joint positions.
            v (float, optional): Speed of the motion. Defaults to 20.
            connect (int, optional): Trajectory connection flag. Defaults to 0.
            block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
            r (float, optional): Blending radius. Defaults to 0.

        Returns:
            None
        """
        movej_result = self.robot.rm_movej(joint, v, r, connect, block)
        if movej_result == 0:
            print("\nmovej motion succeeded\n")
        else:
            print("\nmovej motion failed, Error code: ", movej_result, "\n")

    def set_gripper_pick_on(self, speed, force, block=True, timeout=30):
        """
        Perform continuous force-controlled gripping with the gripper.

        Args:
            speed (int): Speed of the gripper.
            force (int): Force applied by the gripper.
            block (bool, optional): Whether the function is blocking. Defaults to True.
            timeout (int, optional): Timeout duration. Defaults to 30.

        Returns:
            None
        """
        gripper_result = self.robot.rm_set_gripper_pick_on(speed, force, block, timeout)
        if gripper_result == 0:
            print("\nGripper continuous force control gripping succeeded\n")
        else:
            print("\nGripper continuous force control gripping failed, Error code: ", gripper_result, "\n")
        time.sleep(2)

    def set_gripper_release(self, speed, block=True, timeout=30):
        """
        Release the gripper.

        Args:
            speed (int): Speed of the gripper release.
            block (bool, optional): Whether the function is blocking. Defaults to True.
            timeout (int, optional): Timeout duration. Defaults to 30.

        Returns:
            None
        """
        gripper_result = self.robot.rm_set_gripper_release(speed, block, timeout)
        if gripper_result == 0:
            print("\nGripper release succeeded\n")
        else:
            print("\nGripper release failed, Error code: ", gripper_result, "\n")
        time.sleep(2)


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Perform movej motion
    robot_controller.movej([90, 90, 30, 0, 60, 0])

    # Perform continuous force-controlled gripping with the gripper
    robot_controller.set_gripper_pick_on(500, 200)

    # Perform movej motion
    robot_controller.movej([0, 90, 30, 0, 60, 0])

    # Release the gripper
    robot_controller.set_gripper_release(500)

    # Perform movej motion
    robot_controller.movej([90, 90, 30, 0, 60, 0])

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
