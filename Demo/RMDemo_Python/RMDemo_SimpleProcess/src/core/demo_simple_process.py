import sys
import os

# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Robotic_Arm.rm_robot_interface import *

# 定义机械臂型号到点位的映射  
arm_models_to_points = {  
    "RM_65": [  
        [0, 20, 70, 0, 90, 0],
        [0.3, 0, 0.3, 3.14, 0, 0],
        [0.2, 0, 0.3, 3.14, 0, 0],
        [0.3, 0, 0.3, 3.14, 0, 0],
        [0.2, 0.05, 0.3, 3.14, 0, 0],
        [0.2, -0.05, 0.3, 3.14, 0, 0] ,
    ],  
    "RM_75": [  
        [0, 20, 0, 70, 0, 90, 0],
        [0.297557, 0, 0.337061, 3.142, 0, 3.142],
        [0.097557, 0, 0.337061, 3.142, 0, 3.142],
        [0.297557, 0, 0.337061, 3.142, 0, 3.142],
        [0.257557, -0.08, 0.337061, 3.142, 0, 3.142],
        [0.257557, 0.08, 0.337061, 3.142, 0, 3.142],
    ], 
    "RML_63": [  
        [0, 20, 70, 0, 90, 0],
        [0.448968, 0, 0.345083, 3.142, 0, 3.142],
        [0.248968, 0, 0.345083, 3.142, 0, 3.142],
        [0.448968, 0, 0.345083, 3.142, 0, 3.142],
        [0.408968, -0.1, 0.345083, 3.142, 0, 3.142],
        [0.408968, 0.1, 0.345083, 3.142, 0, 3.142]  ,
    ], 
    "ECO_65": [  
        [0, 20, 70, 0, -90, 0],
        [0.352925, -0.058880, 0.327320, 3.141, 0, -1.57],
        [0.152925, -0.058880, 0.327320, 3.141, 0, -1.57],
        [0.352925, -0.058880, 0.327320, 3.141, 0, -1.57],
        [0.302925, -0.158880, 0.327320, 3.141, 0, -1.57],
        [0.302925, 0.058880, 0.327320, 3.141, 0, -1.57],
    ],
    "GEN_72": [  
        [0, 0, 0, -90, 0, 0, 0],
        [0.1, 0, 0.4, 3.14, 0, 0],
        [0.3, 0, 0.4, 3.14, 0, 0],
        [0.3595, 0, 0.4265, 3.142, 0, 0],
        [0.3595, 0.03, 0.4265, 3.142, 0, 0],
        [0.3595, 0.03, 0.4665, 3.142, 0, 0],
    ],
    "ECO_63": [  
        [0, 20, 70, 0, -90, 0],
        [0.544228, -0.058900, 0.468274, 3.142, 0, -1.571],
        [0.344228, -0.058900, 0.468274, 3.142, 0, -1.571],
        [0.544228, -0.058900, 0.468274, 3.142, 0, -1.571],
        [0.504228, -0.108900, 0.468274, 3.142, 0, -1.571],
        [0.504228, -0.008900, 0.468274, 3.142, 0, -1.571],
    ],
} 


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

    def get_arm_model(self):
        """Get robotic arm mode.
        """
        res, model = self.robot.rm_get_robot_info()
        if res == 0:
            return model["arm_model"]
        else:
            print("\nFailed to get robot arm model\n")

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

    def get_arm_software_info(self):
        """
        Get the software information of the robotic arm.

        Returns:
            None
        """
        software_info = self.robot.rm_get_arm_software_info()
        if software_info[0] == 0:
            print("\n================== Arm Software Information ==================")
            print("Arm Model: ", software_info[1]['product_version'])
            print("Algorithm Library Version: ", software_info[1]['algorithm_info']['version'])
            print("Control Layer Software Version: ", software_info[1]['ctrl_info']['version'])
            print("Dynamics Version: ", software_info[1]['dynamic_info']['model_version'])
            print("Planning Layer Software Version: ", software_info[1]['plan_info']['version'])
            print("==============================================================\n")
        else:
            print("\nFailed to get arm software information, Error code: ", software_info[0], "\n")

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

    def movec(self, pose_via, pose_to, v=20, r=0, loop=0, connect=0, block=1):
        """
        Perform movec motion.

        Args:
            pose_via (list of float): Via position [x, y, z, rx, ry, rz].
            pose_to (list of float): End position for the circular path [x, y, z, rx, ry, rz].
            v (float, optional): Speed of the motion. Defaults to 20.
            loop (int, optional): Number of loops. Defaults to 0.
            connect (int, optional): Trajectory connection flag. Defaults to 0.
            block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
            r (float, optional): Blending radius. Defaults to 0.

        Returns:
            None
        """
        movec_result = self.robot.rm_movec(pose_via, pose_to, v, r, loop, connect, block)
        if movec_result == 0:
            print("\nmovec motion succeeded\n")
        else:
            print("\nmovec motion failed, Error code: ", movec_result, "\n")

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


def main():
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Get basic arm information
    robot_controller.get_arm_software_info()

    arm_model = robot_controller.get_arm_model()
    points = arm_models_to_points.get(arm_model, [])

    # Define joint positions for 6 DOF
    joint_6dof = points[0]

    # Perform movej motion for 6 DOF robot arm
    robot_controller.movej(joint_6dof)

    # Perform movej_p motion
    robot_controller.movej_p(points[1])

    # Perform movel motion
    robot_controller.movel(points[2])

    # Perform movej_p motion again
    robot_controller.movej_p(points[3])

    # Perform movec motion
    robot_controller.movec(points[4], points[5], loop=2)

    # Disconnect the robot arm
    robot_controller.disconnect()


if __name__ == "__main__":
    main()
