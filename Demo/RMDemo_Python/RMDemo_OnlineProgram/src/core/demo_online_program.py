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

    def demo_drag_teach(self, trajectory_record):
        """
        Start drag teaching mode.

        Args:
            trajectory_record (int): 0 to not record the trajectory, 1 to record the trajectory.

        Returns:
            None
        """
        result = self.robot.rm_start_drag_teach(trajectory_record)
        if result == 0:
            print("Drag teaching started")
        else:
            print("Failed to start drag teaching")

        input("Drag teaching has started, complete the drag operation and press Enter to continue...")

        result = self.robot.rm_stop_drag_teach()
        if result == 0:
            print("Drag teaching stopped")
        else:
            print("Failed to stop drag teaching")

    def demo_save_trajectory(self, file_path='../data/trajectory.txt'):
        """
        Save the recorded trajectory.

        Args:
            file_path (str, optional): Path to save the trajectory file. Defaults to '../data/trajectory.txt'.

        Returns:
            int: Total number of trajectory points if successful, None otherwise.
        """
        result = self.robot.rm_save_trajectory(file_path)
        if result[0] == 0:
            print("Trajectory saved successfully, total number of points:", result[1])
            return result[1]
        else:
            print("Failed to save trajectory")
            return None

    def add_lines_to_file(self, file_path, type_value):
        """
        Add specific lines to the trajectory file.

        Args:
            file_path (str): Path to the trajectory file.
            type_value (int): Type value to be added to the file.

        Returns:
            None
        """
        # Set file_value based on degree of freedom
        robot_info = self.robot.rm_get_robot_info()
        if robot_info[1]['arm_dof'] == 6:
            file_value = 6
        elif robot_info[1]['arm_dof'] == 7:
            file_value = 7
        else:
            raise ValueError("Invalid degree of freedom, must be 6 or 7")

        # Define lines to be added, using parameterized values
        lines_to_add = [f'{{"file":{file_value}}}\n',
                        f'{{"name":"Folder","num":1,"type":{type_value},"enabled":true,"parent_number":0}}\n']

        # Read original file content
        with open(file_path, 'r+', encoding='utf-8') as file:
            original_content = file.read()

            # Move file pointer to the beginning
            file.seek(0)

            # Write new lines and original content
            file.writelines(lines_to_add)
            file.write(original_content)

    def demo_send_project(self, file_path, plan_speed=20, only_save=0, save_id=100, step_flag=0, auto_start=0, project_type=0):
        """
        Send a project to the robot arm.

        Args:
            file_path (str): Path to the file to be sent.
            plan_speed (int, optional): Planning speed ratio. Defaults to 20.
            only_save (int, optional): 0 to run the file, 1 to only save the file without running. Defaults to 0.
            save_id (int, optional): ID to save in the controller. Defaults to 1.
            step_flag (int, optional): Set step mode, 1 to set step mode, 0 to set normal mode. Defaults to 0.
            auto_start (int, optional): Set default online programming file, 1 to set as default, 0 to set as non-default.
            Defaults to 0.
            project_type (int, optional): Set project file type, 1 to set as drag trajectory, 0 to set as online programming file.
            Defaults to 0.

        Returns:
            None
        """
        # Check if file path exists
        if not os.path.exists(file_path):
            print("File path does not exist:", file_path)
            return

        send_project = rm_send_project_t(file_path, plan_speed, only_save, save_id, step_flag, auto_start, project_type)
        result = self.robot.rm_send_project(send_project)

        if result[0] == 0:
            if result[1] == -1:
                print("Project sent and run successfully")
            elif result[1] == 0:
                print("Project sent successfully but not run, data length verification failed")
            else:
                print("Project sent successfully but run failed, problematic project lines:", result[1])
        else:
            print("Failed to send project, error code:", result[0])

    def demo_get_program_run_state(self, time_sleep, max_retries=10):
        """
        Get the running state of the program.

        Args:
            time_sleep (int): Time to sleep between retries.
            max_retries (int, optional): Maximum number of retries. Defaults to 10.

        Returns:
            None
        """
        retries = 0
        while retries < max_retries:
            time.sleep(time_sleep)
            result = self.robot.rm_get_program_run_state()

            if result[0] == 0:
                print("Program running state:", result[1])
                if result[1] == 0:
                    print("Program has ended")
                    break
            else:
                print("Failed to query, error code:", result[0])

            retries += 1

        if retries == max_retries:
            print("Reached maximum query attempts, exiting")

    def demo_set_arm_pause(self):
        """
        Pause the robot arm.

        Args:
            None

        Returns:
            None
        """
        result = self.robot.rm_set_arm_pause()
        if result == 0:
            print("Robot arm paused successfully")
        else:
            print("Failed to pause the robot arm")

    def demo_set_arm_continue(self):
        """
        Continue the robot arm.

        Args:
            None

        Returns:
            None
        """
        result = self.robot.rm_set_arm_continue()
        if result == 0:
            print("Robot arm continued successfully")
        else:
            print("Failed to continue the robot arm")

    def demo_set_arm_stop(self):
        """
        Stop the robot arm immediately.

        Args:
            None

        Returns:
            None
        """
        result = self.robot.rm_set_arm_stop()
        if result == 0:
            print("Robot arm stopped immediately")
        else:
            print("Failed to stop the robot arm immediately")

    def demo_set_arm_slow_stop(self):
        """
        Perform a slow stop of the robot arm's trajectory.

        Args:
            None

        Returns:
            None
        """
        result = self.robot.rm_set_arm_slow_stop()
        if result == 0:
            print("Robot arm trajectory stopped slowly successfully")
        else:
            print("Failed to perform a slow stop of the robot arm's trajectory")


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080)

    # Get API version
    print("\nAPI Version:", rm_api_version(), "\n")

    file_path_test = os.path.join(sys.path[0], "../../data/test.txt")

    # Drag teaching
    robot_controller.demo_drag_teach(1)

    # Save trajectory
    lines = robot_controller.demo_save_trajectory(file_path_test)

    # Add lines to file
    robot_controller.add_lines_to_file(file_path_test, lines)

    # Send project and query running state
    robot_controller.demo_send_project(file_path_test)

    # Check program run state
    robot_controller.demo_get_program_run_state(1, max_retries=5)

    # Pause the robot arm
    robot_controller.demo_set_arm_pause()

    time.sleep(3)

    # Check program run state
    robot_controller.demo_get_program_run_state(1, max_retries=5)

    # Continue the robot arm
    robot_controller.demo_set_arm_continue()

    # Check program run state
    robot_controller.demo_get_program_run_state(1, max_retries=5)

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
