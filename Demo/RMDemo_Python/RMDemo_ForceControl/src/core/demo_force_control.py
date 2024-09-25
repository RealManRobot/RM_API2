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

    def set_force_position(self, sensor=1, mode=0, direction=2, force=-1):
        """
        Set force control mode.

        Args:
            sensor (int, optional): 0 for one-dimensional force, 1 for six-dimensional force. Defaults to 1.
            mode (int, optional): Force control mode, 0 for base coordinate system force control, 1 for tool coordinate system force control. Defaults to 0.
            direction (int, optional): Force control direction, 0 for X-axis, 1 for Y-axis, 2 for Z-axis, 3 for RX direction, 4 for RY direction, 5 for RZ direction. Defaults to 2.
            force (float, optional): Magnitude of the force in N. Defaults to -1.

        Returns:
            None
        """
        result = self.robot.rm_set_force_position(sensor, mode, direction, force)
        if result == 0:
            print("Set force control mode succeeded")
        else:
            print("Set force control mode failed: ", result)

    def stop_force_position(self):
        """
        Stop force control mode.

        Returns:
            None
        """
        result = self.robot.rm_stop_force_position()
        if result == 0:
            print("Stop force control mode succeeded")
        else:
            print("Stop force control mode failed: ", result)

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


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Movej to the starting joint
    robot_controller.movej([0, 0, 0, 0, 0, 0])
    time.sleep(2)

    # Movej_p to the starting position
    robot_controller.movej_p([0.3, 0, 0.4, 3.141, 0, 0])
    time.sleep(2)

    for i in range(3):
        # Set force control mode
        robot_controller.set_force_position(sensor=1, mode=0, direction=2, force=-5)

        # Move to target position
        robot_controller.movel([0.2, 0, 0.4, 3.141, 0, 0], v=50)
        time.sleep(0.5)

        # Move back to starting position
        robot_controller.movel([0.3, 0, 0.4, 3.141, 0, 0], v=50)
        time.sleep(0.5)

        # Stop force control mode
        robot_controller.stop_force_position()

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
