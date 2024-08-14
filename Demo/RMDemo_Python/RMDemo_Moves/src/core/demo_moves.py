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

    def movej(self, joint, v=20, connect=0, block=1, r=0):
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
        movej_result = self.robot.rm_movej(joint, v, connect, block, r)
        if movej_result == 0:
            print("\nmovej motion succeeded\n")
        else:
            print("\nmovej motion failed, Error code: ", movej_result, "\n")

    def movej_p(self, pose, v=20, connect=0, block=1, r=0):
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
        movej_p_result = self.robot.rm_movej_p(pose, v, connect, block, r)
        if movej_p_result == 0:
            print("\nmovej_p motion succeeded\n")
        else:
            print("\nmovej_p motion failed, Error code: ", movej_p_result, "\n")

    def moves(self, move_positions=None, speed=20, block=1, blending_radius=0):
        """
        Perform a sequence of move operations.

        Args:
            move_positions (list of float, optional): List of positions to move to, each position is [x, y, z, rx, ry, rz].
            speed (int, optional): Speed of the movement. Defaults to 20.
            block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
            blending_radius (float, optional): Blending radius for the movement. Defaults to 0.

        Returns:
            None
        """
        if move_positions is None:
            move_positions = [
                [-0.3, 0, 0.3, 3.14, 0, 0],
                [-0.27, -0.22, 0.3, 3.14, 0, 0],
                [-0.314, -0.25, 0.2, 3.14, 0, 0],
                [-0.239, 0.166, 0.276, 3.14, 0, 0],
                [-0.239, 0.264, 0.126, 3.14, 0, 0]
            ]

        for i, pos in enumerate(move_positions):
            current_connect = 1 if i < len(move_positions) - 1 else 0
            moves_result = self.robot.rm_moves(pos, speed, current_connect, block, blending_radius)
            if moves_result != 0:
                print(f"\nmoves operation failed, error code: {moves_result}, at position: {pos}\n")
                return

        print("\nmoves operation succeeded\n")


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Perform movej_p motion
    robot_controller.movej([0, 0, 0, 0, 0, 0])

    # Perform movej_p motion
    robot_controller.movej_p([-0.3, 0, 0.3, 3.14, 0, 0])

    # Define custom move positions
    custom_positions = [
        [-0.3, 0, 0.3, 3.14, 0, 0],
        [-0.27, -0.22, 0.3, 3.14, 0, 0],
        [-0.314, -0.25, 0.2, 3.14, 0, 0],
        [-0.239, 0.166, 0.276, 3.14, 0, 0],
        [-0.239, 0.264, 0.126, 3.14, 0, 0]
    ]

    # Perform move operations
    robot_controller.moves(custom_positions)

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
