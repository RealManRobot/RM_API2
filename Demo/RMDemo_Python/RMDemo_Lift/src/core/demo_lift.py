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

    def movel(self, pose, v=20, r=0, connect=0, block=1):
        """
        Perform movel motion.

        Args:
            pose (list of float): End position [x, y, z, rx, ry, rz].
            v (float, optional): Speed of the motion. Defaults to 20.
            connect (int, optional): Trajectory connection flag. Defaults to 0.
            block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
            r (float, optional): Blending radius. Defaults to 0.

        Returns:
            None
        """
        movel_result = self.robot.rm_movel(pose, v, r, connect, block)
        if movel_result == 0:
            print("\nmovel motion succeeded\n")
        else:
            print("\nmovel motion failed, Error code: ", movel_result, "\n")

    def movej_p(self, pose, v=20, r=0, connect=0, block=1):
        """
        Perform movej_p motion.

        Args:
            pose (list of float): Position [x, y, z, rx, ry, rz].
            v (float, optional): Speed of the motion. Defaults to 20.
            connect (int, optional): Trajectory connection flag. Defaults to 0.
            block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
            r (float, optional): Blending radius. Defaults to 0.

        Returns:
            None
        """
        movej_p_result = self.robot.rm_movej_p(pose, v, r, connect, block)
        if movej_p_result == 0:
            print("\nmovej_p motion succeeded\n")
        else:
            print("\nmovej_p motion failed, Error code: ", movej_p_result, "\n")

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

    def set_lift_height(self, speed, height, block=True):
        """
        Set the lift height of the robot.

        Args:
            speed (int): Speed of the lift.
            height (int): Target height of the lift.
            block (bool, optional): Whether the function is blocking. Defaults to True.

        Returns:
            None
        """
        lift_result = self.robot.rm_set_lift_height(speed, height, block)
        if lift_result == 0:
            print("\nLift motion succeeded\n")
        else:
            print("\nLift motion failed, Error code: ", lift_result, "\n")


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    ret = robot_controller.robot.rm_change_work_frame("Base")
    print("\nChange work frame: ", ret, "\n")

    # Lift up
    robot_controller.set_lift_height(20, 500, False)

    # Move the robot arm to the initial position
    robot_controller.movej_p([0.1, 0, 0.7, 0, 0, 3.141])

    # Move the robot arm to the gripping position
    robot_controller.movel([0.1, 0, 0.8, 0, 0, 3.141])

    # Perform continuous force-controlled gripping
    robot_controller.set_gripper_pick_on(500, 200)

    # Move the robot arm back to the initial position
    robot_controller.movel([0.1, 0, 0.7, 0, 0, 3.141])

    # Lift down
    robot_controller.set_lift_height(20, 200)

    # Move the robot arm to the placing position
    robot_controller.movel([0.1, 0, 0.8, 0, 0, 3.141])

    # Release the gripper
    robot_controller.set_gripper_release(500)

    # Move the robot arm back to the initial position
    robot_controller.movel([0.1, 0, 0.7, 0, 0, 3.141])

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
