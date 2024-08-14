import sys
import os
import time

# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Robotic_Arm.rm_robot_interface import *


class AlgoController:
    def __init__(self, arm_model, force_type):
        """
        Initialize the algorithm without connecting to the robotic arm.

        Args:
            arm_model (rm_robot_arm_model_e): Set the robotic arm model.
            force_type (rm_force_type_e): Set the end-effector type.
        """
        self.robot = Algo(arm_model, force_type)
        print("Algorithm initialized, handle ID: ", self.robot.handle.id)

    def set_angle(self, x, y, z):
        """
        Set the installation pose using the algorithm.

        Args:
            x (float): Installation angle of X-axis, unit: °.
            y (float): Installation angle of Y-axis, unit: °.
            z (float): Installation angle of Z-axis, unit: °.

        Returns:
            None
        """
        self.robot.rm_algo_set_angle(x, y, z)
        print("\ninstallation pose set successfully\n")

    def set_workframe(self, pose):
        """
        Set the work frame using the algorithm.

        Returns:
            None
        """
        frame = rm_frame_t(pose=pose)
        self.robot.rm_algo_set_workframe(frame)
        print("\nWork frame set successfully\n")

    def set_toolframe(self, pose, payload, x, y, z):
        """
        Set the tool frame using the algorithm.

        Returns:
            None
        """
        frame = rm_frame_t(None, pose, payload, x, y, z)
        self.robot.rm_algo_set_toolframe(frame)
        print("\nTool frame set successfully\n")

    def forward_kinematics(self, joint_angles, flag):
        """
        Perform forward kinematics.

        Args:
            joint_angles (list): Joint angles for the kinematics calculation.
            flag (int): Flag to determine the output format (1 for Euler angles, 0 for Quaternion).

        Returns:
            None
        """
        pose = self.robot.rm_algo_forward_kinematics(joint_angles, flag)
        print("\nForward Kinematics (flag={}): {}\n".format(flag, pose))

    def inverse_kinematics(self, q_in, q_pose, flag):
        """
        Perform inverse kinematics.

        Args:
            q_in (list): Initial joint angles.
            q_pose (list): Target pose as (x, y, z, rx, ry, rz).
            flag (int): Flag to determine the output format (0 for Euler angles, 1 for Quaternion).

        Returns:
            None
        """
        params = rm_inverse_kinematics_params_t(q_in, q_pose, flag)
        joint_angle = self.robot.rm_algo_inverse_kinematics(params)
        if joint_angle[0] == 0:
            print("\nInverse Kinematics: {}\n".format(joint_angle[1]))
        else:
            print("\nInverse Kinematics failed, error code: ", joint_angle[0], "\n")

    def euler2quaternion(self, euler_angle):
        """
        Convert Euler angles to Quaternion.

        Args:
            euler_angle (list): Euler angles as (rx, ry, rz).

        Returns:
            None
        """
        quaternion = self.robot.rm_algo_euler2quaternion(euler_angle)
        print("\nEuler to Quaternion: {}\n".format(quaternion))

    def quaternion2euler(self, quaternion):
        """
        Convert Quaternion to Euler angles.

        Args:
            quaternion (list): Quaternion as (x, y, z, w).

        Returns:
            None
        """
        euler_angle = self.robot.rm_algo_quaternion2euler(quaternion)
        print("\nQuaternion to Euler: {}\n".format(euler_angle))


def main():
    # Initialize the algorithm controller without connecting to the robotic arm
    arm_model = rm_robot_arm_model_e.RM_MODEL_RM_65_E  # Set the robotic arm model
    force_type = rm_force_type_e.RM_MODEL_RM_B_E  # Set the end-effector type
    algo_controller = AlgoController(arm_model, force_type)

    # Get API version
    print("\nAPI Version: ", rm_api_version(), "\n")

    # Set the installation pose
    algo_controller.set_angle(0, 0, 0)
    # Set the work frame
    algo_controller.set_workframe((0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    # Set the tool frame
    algo_controller.set_toolframe((0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 0, 0, 0, 0)

    # Perform forward kinematics
    joint = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    flag_eul = 1
    flag_qua = 0
    algo_controller.forward_kinematics(joint, flag_eul)  # Euler angles
    algo_controller.forward_kinematics(joint, flag_qua)  # Quaternion

    # Perform inverse kinematics
    q_in_joint = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    q_in_pose = [0.3, 0.0, 0.3, 3.14, 0.0, 0.0]
    flag_eul = 1
    algo_controller.inverse_kinematics(q_in_joint, q_in_pose, flag_eul)

    # Convert Euler angles to Quaternion
    eul = [3.141, 0.0, 0.0]
    algo_controller.euler2quaternion(eul)

    # Convert Quaternion to Euler angles
    qua = [0.0, 0.0, 0.0, 1.0]
    algo_controller.quaternion2euler(qua)

    time.sleep(1)


if __name__ == "__main__":
    main()
