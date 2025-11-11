
from .rm_robot_interface import *

class RoboticArmInternal(RoboticArm):
    def rm_get_current_canfd_enable(self) -> tuple[int, bool]:
        """
        获取电流环控制功能使能状态

        Returns:
            tuple[int,bool]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -bool 获取电流环是否使能，true为使能，false为禁使能
        """
        enable = c_bool()
        tag = rm_get_current_canfd_enable(self.handle, byref(enable))
        return tag, enable.value
    
    def rm_set_current_canfd_enable(self, enable: bool) -> int:
        """
        设置电流环控制功能使能状态
        Args:
            enable (bool): 设置电流环是否使能，true为使能，false为禁使能
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_set_current_canfd_enable(self.handle, enable)
        return tag
    
    def rm_current_canfd(self, current: list[float]) -> int:
        """
        电流环开放控制，使用前请设置电流环控制功能使能
        Args:
            current (list[float]): 关节电流，单位：mA。输入值最多保留三位小数，多余位数将被截断。
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        arr = (c_float * len(current))(*current)
        tag = rm_current_canfd(self.handle, arr)
        return tag
    
    def rm_algo_dyn_Nm_to_A(self, joint_torque: list[float]) -> tuple[int, list[float]]:
        """
        将关节扭矩转换成关节电流
        Args:
            joint_torque (list[float]): 关节扭矩，单位：Nm
        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            -int: 函数执行的状态码。
                - 0：成功。
                - 1: 控制器返回false，传递参数错误或机械臂状态发生错误。
                - 1：当前机型没有动力学辨识参数
                - 2: 数据发送失败，通信过程中出现问题。
                - 3: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            -list: 关节电流，单位：A
        """
        arr1 = (c_float * len(joint_torque))(*joint_torque)
        if self.arm_dof != 0:
            joint_current = (c_float * self.arm_dof)()
        else:
            joint_current = (c_float * ARM_DOF)()
        tag = rm_algo_dyn_Nm_to_A(self.handle, arr1, joint_current)
        return tag,list(joint_current)

    def rm_algo_dyn_calculate_base_friction(self, joint_speed: list[float]) -> tuple[int, list[float]]:
        """
        计算关节基本摩擦力
        Args:
            joint_speed (list[float]): 关节速度，单位: °/s
        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            -int: 函数执行的状态码。
                - 0：成功。
                - 1: 控制器返回false，传递参数错误或机械臂状态发生错误。
                - 1：当前机型没有动力学辨识参数
                - 2: 数据发送失败，通信过程中出现问题。
                - 3: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            -list: 关节基本摩擦力，单位: Nm
        """
        arr1 = (c_float * len(joint_speed))(*joint_speed)
        if self.arm_dof != 0:
            joint_base_friction = (c_float * self.arm_dof)()
        else:
            joint_base_friction = (c_float * ARM_DOF)()
        tag = rm_algo_dyn_calculate_base_friction(self.handle, arr1, joint_base_friction)
        return tag,list(joint_base_friction)