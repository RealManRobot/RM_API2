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

    @staticmethod
    def arm_state_callback(data):
        """
        Callback function for arm state.

        Args:
            data: The data containing the arm state information.
        """
        try:
            print("Joint positions:")
            if len(data.joint_status.joint_position) < 6:
                raise ValueError("Invalid joint positions data length")

            joint_positions = [data.joint_status.joint_position[i] for i in range(6)]

            # Ensure all positions are numeric
            if not all(isinstance(pos, (int, float)) for pos in joint_positions):
                raise ValueError("Non-numeric value found in joint positions")

            rounded_positions = [round(pos, 2) for pos in joint_positions]  # Round to two decimal places
            print(rounded_positions)
        except Exception as e:
            print(f"Error in arm_state_callback: {e}")

    def demo_movej_canfd(self):
        """
        Demonstrates Canfd_movej pass-through.

        This function reads a list of points from a file and moves the robotic arm
        through these points using the CAN FD protocol. The points in the file are
        obtained through drag teaching. The function handles both 6 DOF and 7 DOF
        robotic arms by checking the degree of freedom of the arm and validating
        the points accordingly. It also registers a callback function to monitor
        the arm state in real time.

        Steps:
        1. Read the file contents and convert them into a list of floating-point numbers.
        2. Check the degree of freedom (DOF) of the robotic arm.
        3. Validate the points based on the DOF.
        4. Move the arm to the first point.
        5. Register a callback function for real-time arm state monitoring.
        6. Move the arm through the list of points using CAN FD protocol.
        7. After completing the pass-through, move the arm to the home position.

        Args:
            None

        Raises:
            ValueError: If the points data in the file is invalid or if the degree
                        of freedom is not 6 or 7.
            IndexError: If an index is out of range while accessing the points list.
        """
        try:
            info_result = self.robot.rm_get_robot_info()
            if info_result[1]['arm_model'] == 'RM_65' or info_result[1]["arm_model"] == 'RM_63':
                # Read file contents, the points in the file are obtained by drag teaching
                with open('../data/RM65&RM63_canfd_data.txt', 'r') as f:
                    lines = f.readlines()
            elif info_result[1]['arm_model'] == 'RM_75':
                # Read file contents, the points in the file are obtained by drag teaching
                with open('../data/RM75_canfd_data.txt', 'r') as f:
                    lines = f.readlines()
            elif info_result[1]['arm_model'] == 'ECO_65':
                # Read file contents, the points in the file are obtained by drag teaching
                with open('../data/ECO65_canfd_data.txt', 'r') as f:
                    lines = f.readlines()
            else:
                raise ValueError('Unsupported arm model')

            # Convert to a list of floating-point numbers
            points = []
            for line in lines:
                nums = line.strip().split(',')
                points.append([float(num) for num in nums])

            # Get the degree of freedom (DOF) of the robotic arm
            robot_info = self.robot.rm_get_robot_info()
            if robot_info[1]['arm_dof'] == 6:
                dof = 6
            elif robot_info[1]['arm_dof'] == 7:
                dof = 7
            else:
                raise ValueError("Invalid degree of freedom, must be 6 or 7")

            # Check if points are valid
            if not points or not all(len(point) == dof for point in points):
                raise ValueError("Invalid points data in file")

            # Move to the first point in the pass-through
            num_lines = len(points)
            print(f"Total points: {num_lines}")
            self.robot.rm_movej(points[0], 20, 0, rm_trajectory_connect_config_e.RM_TRAJECTORY_DISCONNECT_E, RM_MOVE_MULTI_BLOCK)

            # Register the callback function once
            arm_state = rm_realtime_arm_state_callback_ptr(RobotArmController.arm_state_callback)
            self.robot.rm_realtime_arm_state_call_back(arm_state)

            # Low follow pass-through
            for i in range(num_lines):
                try:
                    if i >= len(points):
                        raise IndexError("Index out of range for points list")
                    print(f"Moving to point {i}: {points[i]}")
                    self.robot.rm_movej_canfd(points[i], False)
                    time.sleep(0.01)
                except Exception as e:
                    print(f"Error at point {i}: {e}")
            print("Pass-through completed")

            time.sleep(2)
            if info_result[1]['arm_dof'] == 6:
                movej_result = self.robot.rm_movej([0, 0, 0, 0, 0, 0], 50, 0, rm_trajectory_connect_config_e.RM_TRAJECTORY_DISCONNECT_E, RM_MOVE_MULTI_BLOCK)
            elif info_result[1]['arm_dof'] == 7:
                movej_result = self.robot.rm_movej([0, 0, 0, 0, 0, 0, 0], 50, 0, rm_trajectory_connect_config_e.RM_TRAJECTORY_DISCONNECT_E, RM_MOVE_MULTI_BLOCK)
            else:
                raise ValueError("Invalid arm_dof value")
            print(f"movej_cmd joint movement 1: {movej_result}")
            time.sleep(2)
        except Exception as e:
            print(f"Error in demo_movej_canfd: {e}")


def main():
    try:
        # Create a robot arm controller instance and connect to the robot arm
        robot_controller = RobotArmController("192.168.1.18", 8080, 3)

        # Get API version
        print("\nAPI Version: ", rm_api_version(), "\n")

        time.sleep(3)
        config = rm_realtime_push_config_t(1, True, 8098, 0, '192.168.1.79')
        robot_controller.robot.rm_set_realtime_push(config)

        robot_controller.demo_movej_canfd()

        # Disconnect the robot arm
        robot_controller.disconnect()
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
