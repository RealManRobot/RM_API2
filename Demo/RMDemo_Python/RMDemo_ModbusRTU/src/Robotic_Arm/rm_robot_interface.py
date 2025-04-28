"""
@brief 机械臂Python接口
@author Realman-Aisha
@date 2024-04-28

@details
此模块为机械臂提供了一个高易用性的Python接口，通过封装rm_ctypes_wrap模块中导入的C库接口实现。
关键类：RoboticArm类，所有对机械臂的操作均通过此类进行。 

**注意**
- 在使用前，请确保已经根据环境正确配置了c版本的API库。
- 对于可能发生的异常，建议进行适当的错误处理。
- 本模块依赖于rm_ctypes_wrap.py模块，该模块提供了对C语言API的封装。

**更新日志**:
-
"""

from .rm_ctypes_wrap import *
import ctypes
from typing import Callable


class JointConfigSettings:
    """
    关节配置
    """

    def rm_set_joint_max_speed(self, joint_num: int, speed: float) -> int:
        """
        设置指定关节的最大速度。

        Args:
            joint_num (int): 关节的序号，取值范围为1到7，表示机械臂上不同关节的编号。
            speed (float): 关节的最大转速，单位为度每秒(°/s)，定义了关节在运动时所能达到的最大速度。

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_max_speed(self.handle, joint_num, speed)
        return tag

    def rm_set_joint_max_acc(self, joint_num: int, acc: float) -> int:
        """
        设置关节最大加速度

        Args:
            joint_num (int): 关节序号，1~7
            acc (float): 关节最大加速度，单位：°/s²

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """

        tag = rm_set_joint_max_acc(self.handle, joint_num, acc)
        return tag

    def rm_set_joint_min_pos(self, joint_num: int, min_pos: float) -> int:
        """
        设置关节最小限位

        Args:
            joint_num (int): 关节序号，1~7
            min_pos (float): 关节最小位置，单位：°

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_min_pos(self.handle, joint_num, min_pos)
        return tag

    def rm_set_joint_max_pos(self, joint_num: int, max_pos: float) -> int:
        """
        设置关节最大限位

        Args:
            joint_num (int): 关节序号，1~7
            max_pos (float): 关节最大位置，单位：°

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_max_pos(self.handle, joint_num, max_pos)
        return tag

    def rm_set_joint_drive_max_speed(self, joint_num: int, speed: float) -> int:
        """
        设置指定关节(驱动器)的最大速度。

        Args:
            joint_num (int): 关节的序号，取值范围为1到7，表示机械臂上不同关节的编号。
            speed (float): 关节的最大转速，单位为度每秒(°/s)，定义了关节在运动时所能达到的最大速度。

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_drive_max_speed(self.handle, joint_num, speed)
        return tag

    def rm_set_joint_drive_max_acc(self, joint_num: int, acc: float) -> int:
        """
        设置关节(驱动器)最大加速度

        Args:
            joint_num (int): 关节序号，1~7
            acc (float): 关节最大加速度，单位：°/s²

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """

        tag = rm_set_joint_drive_max_acc(self.handle, joint_num, acc)
        return tag

    def rm_set_joint_drive_min_pos(self, joint_num: int, min_pos: float) -> int:
        """
        设置关节(驱动器)最小限位

        Args:
            joint_num (int): 关节序号，1~7
            min_pos (float): 关节最小位置，单位：°

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_drive_min_pos(self.handle, joint_num, min_pos)
        return tag

    def rm_set_joint_drive_max_pos(self, joint_num: int, max_pos: float) -> int:
        """
        设置关节(驱动器)最大限位

        Args:
            joint_num (int): 关节序号，1~7
            max_pos (float): 关节最大位置，单位：°

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_joint_drive_max_pos(self.handle, joint_num, max_pos)
        return tag

    def rm_set_joint_en_state(self, joint_num: int, en_state: int) -> int:
        """
        设置关节使能状态

        Args:
            joint_num (int): 关节序号
            en_state (int): 1：上使能 0：掉使能

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_joint_en_state(self.handle, joint_num, en_state)
        return tag

    def rm_set_joint_zero_pos(self, joint_num: int) -> int:
        """
        设置关节零位

        Args:
            joint_num (int): 关节序号

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_joint_zero_pos(self.handle, joint_num)
        return tag

    def rm_set_joint_clear_err(self, joint_num: int) -> int:
        """
        清除关节错误代码

        Args:
            joint_num (int): 关节序号

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_joint_clear_err(self.handle, joint_num)
        return tag

    def rm_auto_set_joint_limit(self, mode: int) -> int:
        """
        一键设置关节限位

        Args:
            mode (int): 1-正式模式，各关节限位为规格参数中的软限位和硬件限位

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_auto_set_joint_limit(self.handle, mode)
        return tag


class JointConfigReader:
    """
    关节配置查询
    """

    def rm_get_joint_max_speed(self) -> tuple[int, list]:
        """
        查询关节最大速度
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最大速度值。
        """
        if self.arm_dof != 0:
            speed = (c_float * self.arm_dof)()
        else:
            speed = (c_float * ARM_DOF)()

        ret = rm_get_joint_max_speed(self.handle, speed)
        return ret, list(speed)

    def rm_get_joint_max_acc(self) -> tuple[int, list]:
        """
        查询关节最大加速度
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 各关节最大加速度值。
        """
        if self.arm_dof != 0:
            acc = (c_float * self.arm_dof)()
        else:
            acc = (c_float * ARM_DOF)()

        ret = rm_get_joint_max_acc(self.handle, acc)
        return ret, list(acc)

    def rm_get_joint_min_pos(self) -> tuple[int, list]:
        """
        查询关节最小限位
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最小位置数组，长度与机械臂的关节数，单位：°。
        """
        if self.arm_dof != 0:
            min_pos = (c_float * self.arm_dof)()
        else:
            min_pos = (c_float * ARM_DOF)()

        ret = rm_get_joint_min_pos(self.handle, min_pos)
        return ret, list(min_pos)

    def rm_get_joint_max_pos(self) -> tuple[int, list]:
        """
        查询关节最大限位
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最大位置数组，长度机械臂的关节数，单位：°。
        """
        if (self.arm_dof != 0):
            max_pos = (c_float * self.arm_dof)()
        else:
            max_pos = (c_float * ARM_DOF)()

        ret = rm_get_joint_max_pos(self.handle, max_pos)
        return ret, list(max_pos)

    def rm_get_joint_drive_max_speed(self) -> tuple[int, list]:
        """
        查询关节(驱动器)最大速度
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最大速度值。
        """
        if (self.arm_dof != 0):
            speed = (c_float * self.arm_dof)()
        else:
            speed = (c_float * ARM_DOF)()

        ret = rm_get_joint_drive_max_speed(self.handle, speed)
        return ret, list(speed)

    def rm_get_joint_drive_max_acc(self) -> tuple[int, list]:
        """
        查询关节(驱动器)最大加速度
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 各关节最大加速度值。
        """
        if (self.arm_dof != 0):
            acc = (c_float * self.arm_dof)()
        else:
            acc = (c_float * ARM_DOF)()

        ret = rm_get_joint_drive_max_acc(self.handle, acc)
        return ret, list(acc)

    def rm_get_joint_drive_min_pos(self) -> tuple[int, list]:
        """
        查询关节(驱动器)最小限位
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最小位置数组，长度与机械臂的关节数，单位：°。
        """
        if (self.arm_dof != 0):
            min_pos = (c_float * self.arm_dof)()
        else:
            min_pos = (c_float * ARM_DOF)()

        ret = rm_get_joint_drive_min_pos(self.handle, min_pos)
        return ret, list(min_pos)

    def rm_get_joint_drive_max_pos(self) -> tuple[int, list]:
        """
        查询关节(驱动器)最大限位
        Args:
            无。
        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节最大位置数组，长度机械臂的关节数，单位：°。
        """
        if (self.arm_dof != 0):
            max_pos = (c_float * self.arm_dof)()
        else:
            max_pos = (c_float * ARM_DOF)()

        ret = rm_get_joint_drive_max_pos(self.handle, max_pos)
        return ret, list(max_pos)

    def rm_get_joint_en_state(self) -> tuple[int, list]:
        """
        获取关节使能状态

        Returns:
            tuple[int, list]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 每个关节的使能状态数组，长度为机械臂的关节数，单位：°。
        """
        if (self.arm_dof != 0):
            en_state = (uint8_t * self.arm_dof)()
        else:
            en_state = (uint8_t * ARM_DOF)()

        ret = rm_get_joint_en_state(self.handle, en_state)
        return ret, list(en_state)

    def rm_get_joint_err_flag(self) -> dict[str, any]:
        """
        获取关节错误代码

        Returns:
            dict: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - 'err_flag' (list[int]): 整数列表，表示每个关节的错误标志。
              如果arm_dof不为0，则列表长度为arm_dof；否则，使用默认的ARM_DOF长度。
            - 'brake_state' (list[int]): 整数列表，表示每个关节的抱闸状态。
              如果arm_dof不为0，则列表长度为arm_dof；否则，使用默认的ARM_DOF长度。
        """
        if (self.arm_dof != 0):
            err_flag = (uint16_t * self.arm_dof)()
            brake_state = (uint16_t * self.arm_dof)()
        else:
            err_flag = (uint16_t * ARM_DOF)()
            brake_state = (uint16_t * ARM_DOF)()

        ret = rm_get_joint_err_flag(self.handle, err_flag, brake_state)

        result_dict = {
            'return_code': ret,
            'err_flag': list(err_flag),
            'brake_state': list(brake_state),
        }

        return result_dict


class ArmTipVelocityParameters:
    """
    机械臂运动参数
    """

    def rm_set_arm_max_line_speed(self, speed: float) -> int:
        """
        设置机械臂末端最大线速度

        Args:
            speed (float): 末端最大线速度，单位m/s

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_arm_max_line_speed(self.handle, speed)
        return tag

    def rm_set_arm_max_line_acc(self, acc: float) -> int:
        """
        设置机械臂末端最大线加速度

        Args:
            acc (float): 末端最大线加速度，单位m/s^2

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_arm_max_line_acc(self.handle, acc)
        return tag

    def rm_set_arm_max_angular_speed(self, speed: float) -> int:
        """
        设置机械臂末端最大角速度

        Args:
            speed (float): 末端最大角速度，单位rad/s

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_arm_max_angular_speed(self.handle, speed)
        return tag

    def rm_set_arm_max_angular_acc(self, acc: float) -> int:
        """
        设置机械臂末端最大角加速度

        Args:
            acc (float): 末端最大角加速度，单位rad/s^2

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据格式不正确或无法识别。
        """
        tag = rm_set_arm_max_angular_acc(self.handle, acc)
        return tag

    def rm_set_arm_tcp_init(self) -> int:
        """
        设置机械臂末端参数为默认值

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_tcp_init(self.handle)
        return tag

    def rm_set_collision_state(self, stage: int) -> int:
        """
        设置机械臂动力学碰撞检测等级

        Args:
            stage (int): 等级：0~8，0-无碰撞，8-碰撞最灵敏

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_collision_state(self.handle, stage)
        return tag

    def rm_get_collision_stage(self) -> tuple[int, int]:
        """
        查询碰撞防护等级

        Returns:
            tuple[int,int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 等级，范围：0~8.
        """
        stage = c_int()
        ret = rm_get_collision_stage(self.handle, byref(stage))
        return ret, stage.value

    def rm_get_arm_max_line_speed(self) -> tuple[int, float]:
        """
        获取机械臂末端最大线速度

        Returns:
            tuple[int,float]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - float: 末端最大线速度，单位m/s.
        """
        speed = c_float()
        ret = rm_get_arm_max_line_speed(self.handle, byref(speed))
        return ret, speed.value

    def rm_get_arm_max_line_acc(self) -> tuple[int, float]:
        """
        获取机械臂末端最大线加速度

        Returns:
            tuple[int,float]: 包含两个元素的元组。

            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - float: 末端最大线加速度，单位m/s^2.
        """
        acc = c_float()
        ret = rm_get_arm_max_line_acc(self.handle, byref(acc))
        return ret, acc.value

    def rm_get_arm_max_angular_speed(self) -> tuple[int, float]:
        """
        获取机械臂末端最大角速度

        Returns:
            tuple[int,float]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - float: 末端最大角速度，单位rad/s.
        """
        speed = c_float()
        ret = rm_get_arm_max_angular_speed(self.handle, byref(speed))
        return ret, speed.value

    def rm_get_arm_max_angular_acc(self) -> tuple[int, float]:
        """
        获取机械臂末端最大角加速度

        Returns:
            tuple[int,float]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - float: 末端最大角加速度，单位rad/s^2.
        """
        acc = c_float()
        ret = rm_get_arm_max_angular_acc(self.handle, byref(acc))
        return ret, acc.value
    
    def rm_set_DH_data_default(self) -> int:
        """
        恢复机械臂默认 DH 参数

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_DH_data_default(self.handle)
        return tag
    
    def rm_set_DH_data(self, DH_data: rm_dh_t) -> int:
        """
        设置DH参数

        Args:
            DH_data (rm_dh_t): DH参数

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_DH_data(self.handle, DH_data)
        return tag

    def rm_get_DH_data(self) -> tuple[int, rm_dh_t]:
        """
        获取DH参数
        Returns:
            tuple[int,rm_dh_t]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - rm_dh_t: DH参数。
        """
        DH_data = rm_dh_t()
        ret = rm_get_DH_data(self.handle, DH_data)
        return ret, DH_data.to_dict()

class ToolCoordinateConfig:
    """
    工具坐标系
    """

    def rm_set_auto_tool_frame(self, point_num: int) -> int:
        """
        六点法自动设置工具坐标系 标记点位

        Args:
            point_num (int): 1~6代表6个标定点

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_auto_tool_frame(self.handle, point_num)
        return tag

    def rm_generate_auto_tool_frame(self, tool_name: str, payload: float, x: float, y: float, z: float) -> int:
        """
        六点法自动设置工具坐标系 提交

        Args:
            tool_name (str): 工具坐标系名称，不能超过十个字节。
            payload (float):新工具执行末端负载重量  单位kg
            x (float): 新工具执行末端负载位置 位置x 单位m
            y (float): 新工具执行末端负载位置 位置y 单位m
            z (float): 新工具执行末端负载位置 位置z 单位m

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_generate_auto_tool_frame(
            self.handle, tool_name, payload, x, y, z)
        return tag

    def rm_set_manual_tool_frame(self, frame: rm_frame_t) -> int:
        """
        手动设置工具坐标系

        Args:
            frame (rm_frame_t): 新工具坐标系参数结构体

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_manual_tool_frame(self.handle, frame)
        return tag

    def rm_change_tool_frame(self, tool_name: str) -> int:
        """
        切换当前工具坐标系

        Args:
            tool_name (str): 目标工具坐标系名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_change_tool_frame(self.handle, tool_name)
        return tag

    def rm_delete_tool_frame(self, tool_name: str) -> int:
        """
        删除指定工具坐标系

        Args:
            tool_name (str): 要删除的工具坐标系名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_delete_tool_frame(self.handle, tool_name)
        return tag

    def rm_update_tool_frame(self, frame: rm_frame_t) -> int:
        """
        修改指定工具坐标系

        Args:
            frame (rm_frame_t): 要修改的工具坐标系名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_update_tool_frame(self.handle, frame)
        return tag

    def rm_get_total_tool_frame(self) -> dict[str, any]:
        """
        获取所有工具坐标系名称

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'tool_names' (list[str]): 字符串列表，表示所有工具坐标系名称。
            - 'len' (int): 工具坐标系名称数量。
        """
        names = (rm_frame_name_t*10)()
        len_ = c_int()
        ret = rm_get_total_tool_frame(self.handle, names, byref(len_))
        tool_names = [names[i].name.decode('utf-8') for i in range(len_.value)]

        result_dict = {
            'return_code': ret,
            'tool_names': tool_names,
            'len': len_.value,
        }

        return result_dict

    def rm_get_given_tool_frame(self, tool_name: str) -> tuple[int, dict[str, any]]:
        """
        获取指定工具坐标系

        Args:
            tool_name (str): 工具坐标系名称。

        Returns:
            tuple: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - dict: 工具坐标系字典，键为rm_frame_t的参数名。
        """
        tool_frame = rm_frame_t()
        ret = rm_get_given_tool_frame(
            self.handle, tool_name, byref(tool_frame))

        return ret, tool_frame.to_dictionary()

    def rm_get_current_tool_frame(self) -> tuple[int, dict[str, any]]:
        """
        获取当前工具坐标系。

        Args:
            无。

        Returns:
            tuple: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - dict: 工具坐标系字典，键为rm_frame_t的参数名。
        """
        tool_frame = rm_frame_t()
        ret = rm_get_current_tool_frame(self.handle, byref(tool_frame))

        return ret, tool_frame.to_dictionary()

    def rm_set_tool_envelope(self, envelope: rm_envelope_balls_list_t) -> int:
        """
        设置工具坐标系的包络参数

        Args:
            envelope (rm_envelope_balls_list_t): 包络参数列表，每个工具最多支持 5 个包络球，可以没有包络

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        ret = rm_set_tool_envelope(self.handle, envelope)
        return ret

    def rm_get_tool_envelope(self, tool_name: str) -> tuple[int, dict[str, any]]:
        """
        获取工具坐标系的包络参数

        Args:
            tool_name (string): 工具坐标系名称

        Returns:
            tuple: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回设置失败，可能是参数错误或控制器发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等。
            - dict: 包络参数字典，包含了工具坐标系的包络参数信息。
        """
        envelope_balls = rm_envelope_balls_list_t()
        ret = rm_get_tool_envelope(
            self.handle, tool_name, byref(envelope_balls))

        return ret, envelope_balls.to_dictionary()


class WorkCoordinateConfig:
    """
    工作坐标系
    """

    def rm_set_auto_work_frame(self, name: str, point_num: int) -> int:
        """
        三点法自动设置工作坐标系

        Args:
            name (str): 工作坐标系名称，不能超过十个字节。
            point_num (int): 1~3代表3个标定点，依次为原点、X轴一点、Y轴一点，4代表生成坐标系。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_auto_work_frame(self.handle, name, point_num)
        return tag

    def rm_set_manual_work_frame(self, name: str, pose: list) -> int:
        """
        手动设置工作坐标系

        Args:
            name (str): 工作坐标系名称，不能超过十个字节。
            pose (list): 新工作坐标系相对于基坐标系的位姿

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        frame_pose = rm_pose_t()
        frame_pose.position = rm_position_t(*pose[:3])
        frame_pose.euler = rm_euler_t(*pose[3:])
        tag = rm_set_manual_work_frame(self.handle, name, frame_pose)
        return tag

    def rm_change_work_frame(self, tool_name: str) -> int:
        """
        切换当前工作坐标系

        Args:
            tool_name (str): 目标工作坐标系名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_change_work_frame(self.handle, tool_name)
        return tag

    def rm_delete_work_frame(self, tool_name: str) -> int:
        """
        删除指定工作坐标系

        Args:
            tool_name (str): 要删除的工作坐标系名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_delete_work_frame(self.handle, tool_name)
        return tag

    def rm_update_work_frame(self, name: str, pose: list) -> int:
        """
        修改指定工作坐标系

        Args:
            name (str): 指定工具坐标系名称
            pose (list): 更新工作坐标系相对于基坐标系的位姿

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        frame_pose = rm_pose_t()
        frame_pose.position = rm_position_t(*pose[:3])
        frame_pose.euler = rm_euler_t(*pose[3:])
        tag = rm_update_work_frame(self.handle, name, frame_pose)
        return tag

    def rm_get_total_work_frame(self) -> dict[str, any]:
        """
        获取所有工作坐标系名称

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'tool_names' (list[str]): 字符串列表，表示所有工作坐标系名称。
            - 'len' (int): 工作坐标系名称数量。
        """
        len_ = c_int()
        names = (rm_frame_name_t*10)()
        ret = rm_get_total_work_frame(self.handle, names, byref(len_))
        work_names = [names[i].name.decode('utf-8') for i in range(len_.value)]
        result_dict = {
            'return_code': ret,
            'work_names': work_names,
            'len': len_.value,
        }

        return result_dict

    def rm_get_given_work_frame(self, name: str) -> tuple[int, list[float]]:
        """
        获取指定工作坐标系

        Args:
            name (str): 指定的工作坐标系名称

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - list: 工作坐标系位姿列表。
        """
        work_frame = rm_pose_t()
        ret = rm_get_given_work_frame(self.handle, name, byref(work_frame))
        position = work_frame.position
        euler = work_frame.euler
        return ret, [position.x, position.y, position.z, euler.rx, euler.ry, euler.rz]

    def rm_get_current_work_frame(self) -> tuple[int, dict[str, any]]:
        """
        获取当前工作坐标系

        Returns:
            tuple[int, dict[str, any]]: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - dict: 工作坐标系字典，键为rm_frame_t的参数名。
        """
        frame = rm_frame_t()
        ret = rm_get_current_work_frame(self.handle, byref(frame))

        return ret, frame.to_dictionary()


class ArmState:
    """
    机械臂状态获取
    """

    def rm_get_current_arm_state(self) -> tuple[int, dict[str, any]]:
        """
        获取机械臂当前状态

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - dict: 机械臂当前状态字典，键为rm_current_arm_state_t的参数名。
        """
        state = rm_current_arm_state_t()
        ret = rm_get_current_arm_state(self.handle, byref(state))

        return ret, state.to_dictionary(self.arm_dof if self.arm_dof != 0 else ARM_DOF)

    def rm_get_current_joint_temperature(self) -> tuple[int, list[float]]:
        """
        获取关节当前温度

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节1~7温度数组，单位：℃
        """
        if self.arm_dof != 0:
            temperature = (c_float * self.arm_dof)()
        else:
            temperature = (c_float * ARM_DOF)()

        ret = rm_get_current_joint_temperature(self.handle, temperature)
        return ret, list(temperature)

    def rm_get_current_joint_current(self) -> tuple[int, list[float]]:
        """
        获取关节当前电流

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节1~7电流数组，单位：mA
        """
        if self.arm_dof != 0:
            current = (c_float * self.arm_dof)()
        else:
            current = (c_float * ARM_DOF)()

        ret = rm_get_current_joint_current(self.handle, current)
        return ret, list(current)

    def rm_get_current_joint_voltage(self) -> tuple[int, list[float]]:
        """
        获取关节当前电压

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 关节1~7电压数组，单位：V
        """
        if self.arm_dof != 0:
            voltage = (c_float * self.arm_dof)()
        else:
            voltage = (c_float * ARM_DOF)()

        ret = rm_get_current_joint_voltage(self.handle, voltage)
        return ret, list(voltage)

    def rm_set_init_pose(self, joint: list[float]) -> int:
        """
        设置机械臂的初始位置角度

        Args:
            joint (list[float]): 机械臂初始位置关节角度数组

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        if self.arm_dof != 0:
            joint_position = (c_float * self.arm_dof)(*joint)
        else:
            joint_position = (c_float * ARM_DOF)(*joint)

        tag = rm_set_init_pose(self.handle, joint_position)

        return tag

    def rm_get_init_pose(self) -> tuple[int, list[float]]:
        """
        获取机械臂初始位置角度

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 机械臂初始位置关节角度数组，单位：°
        """
        if self.arm_dof != 0:
            joint_position = (c_float * self.arm_dof)()
        else:
            joint_position = (c_float * ARM_DOF)()

        ret = rm_get_init_pose(self.handle, joint_position)
        return ret, list(joint_position)

    def rm_get_joint_degree(self) -> tuple[int, list[float]]:
        """
        获取当前关节角度

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list: 当前7个关节的角度数组，单位：°
        """
        if self.arm_dof != 0:
            joint_degree = (c_float * self.arm_dof)()
        else:
            joint_degree = (c_float * ARM_DOF)()

        ret = rm_get_joint_degree(self.handle, joint_degree)
        return ret, list(joint_degree)

    def rm_get_arm_all_state(self) -> tuple[int, dict[str, any]]:
        """
        获取机械臂所有状态信息

        Returns:
            tuple[int, dict[str, any]]: 包含两个元素的元组。
                - int: 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - dict: 机械臂所有状态信息字典，键为rm_arm_all_state_t的参数名。
        """
        joint_status = rm_arm_all_state_t()

        tag = rm_get_arm_all_state(self.handle, joint_status)

        return tag, joint_status.to_dictionary()

    def rm_get_controller_rs485_mode(self) -> dict[str, any]:
        """
        查询控制器RS485模式

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - -4: 四代控制器不支持该接口
            - 'mode' (int): 0-代表默认 RS485 串行通讯，1-代表 modbus-RTU 主站模式，2-代表 modbus-RTU 从站模式；
            - 'baudrate' (int): 波特率
            - 'timeout' (int): modbus 协议超时时间，单位 100ms，仅在 modbus-RTU 模式下提供此字段
        """
        mode = c_int()
        baudrate = c_int()
        timeout = c_int()

        ret = rm_get_controller_RS485_mode(
            self.handle, byref(mode), byref(baudrate), byref(timeout))

        # 创建一个字典来存储返回值
        result_dict = {
            'return_code': ret,
            'mode': mode.value,
            'baudrate': baudrate.value,
            'timeout': timeout.value,
        }

        return result_dict

    def rm_get_tool_rs485_mode(self) -> dict[str, any]:
        """
        查询工具端 RS485 模式

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
                - -4: 四代控制器不支持该接口
            - 'mode' (int): 0-代表默认 RS485 串行通讯 1-代表 modbus-RTU 主站模式
            - 'baudrate' (int): 波特率
            - 'timeout' (int): modbus 协议超时时间，单位 100ms，仅在 modbus-RTU 模式下提供此字段
        """
        mode = c_int()
        baudrate = c_int()
        timeout = c_int()

        ret = rm_get_tool_RS485_mode(self.handle, byref(
            mode), byref(baudrate), byref(timeout))

        # 创建一个字典来存储返回值
        result_dict = {
            'return_code': ret,
            'mode': mode.value,
            'baudrate': baudrate.value,
            'timeout': timeout.value,
        }

        return result_dict


class MovePlan:
    """
    机械臂轨迹规划指令
    """

    def rm_movej(self, joint: list[float], v: int, r: int, connect: int, block: int) -> int:
        """
        关节空间运动

        Args:
            joint (list): 各关节目标角度数组，单位：°
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)(*joint)
        else:
            joint_positions = (c_float * ARM_DOF)(*joint)

        tag = rm_movej(self.handle, joint_positions, v, r, connect, block)

        return tag

    def rm_movel(self, pose: list[float], v: int, r: int, connect: int, block: int) -> int:
        """
        笛卡尔空间直线运动

        Args:
            pose (list[float]): 目标位姿,位置单位：米，姿态单位：弧度
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose[:3])
        po1.euler = rm_euler_t(*pose[3:])

        tag = rm_movel(self.handle, po1, v, r, connect, block)

        return tag
    
    def rm_movel_offset(self, pose: list[float], v: int, r: int, connect: int, frame_type: int, block: int) -> int:
        """
        笛卡尔空间直线偏移运动 

        该函数用于机械臂末端在当前位姿的基础上沿某坐标系（工具或工作）进行位移或旋转运动。

        Args:
            offset (list[float]): 位置姿态偏移，位置单位：米，姿态单位：弧度
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
            frame_type (int): 坐标系类型
                - 0：工作坐标系
                - 1：工具坐标系
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose[:3])
        po1.euler = rm_euler_t(*pose[3:])

        tag = rm_movel_offset(self.handle, po1, v, r, connect, frame_type, block)

        return tag

    def rm_moves(self, pose: list[float], v: int, r: int, connect: int, block: int) -> int:
        """
        样条曲线运动

        Args:
            pose (list[float]): 目标位姿,位置单位：米，姿态单位：弧度
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
                **注意**
                样条曲线运动需至少连续下发三个点位（trajectory_connect设置为1），否则运动轨迹为直线。
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose[:3])
        po1.euler = rm_euler_t(*pose[3:])

        tag = rm_moves(self.handle, po1, v, r, connect, block)

        return tag

    def rm_movec(self, pose_via: list[float], pose_to: list[float], v: int, r: int, loop: int, connect: int, block: int) -> int:
        """
        笛卡尔空间圆弧运动

        Args:
            pose_via (list[float]): 中间点位姿，位置单位：米，姿态单位：弧度
            pose_to (list[float]): 终点位姿，位置单位：米，姿态单位：弧度
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            loop (int): 规划圈数.
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose_via[:3])
        po1.euler = rm_euler_t(*pose_via[3:])

        po2 = rm_pose_t()
        po2.position = rm_position_t(*pose_to[:3])
        po2.euler = rm_euler_t(*pose_to[3:])
        tag = rm_movec(self.handle, po1, po2, v, r, loop, connect, block)

        return tag

    def rm_movej_p(self, pose: list[float], v: int, r: int, connect: int, block: int) -> int:
        """
        该函数用于关节空间运动到目标位姿

        Args:
            pose (list[float]): 目标位姿，位置单位：米，姿态单位：弧度。
            v (int): 速度百分比系数，1~100
            r (int, optional): 交融半径百分比系数，0~100。
            connect (int): 轨迹连接标志
                - 0：立即规划并执行轨迹，不与后续轨迹连接。
                - 1：将当前轨迹与下一条轨迹一起规划，但不立即执行。阻塞模式下，即使发送成功也会立即返回。
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose[:3])
        po1.euler = rm_euler_t(*pose[3:])

        tag = rm_movej_p(self.handle, po1, v, r, connect, block)

        return tag

    def rm_movej_canfd(self, joint: list[float], follow: bool, expand: float = 0, trajectory_mode: int = 0, radio: int = 0) -> int:
        """
        角度不经规划，直接通过CANFD透传给机械臂
        @details 角度透传到 CANFD，若指令正确，机械臂立即执行
        <b>备注</b>：
            透传效果受通信周期和轨迹平滑度影响，因此要求通信周期稳定，避免大幅波动。
            用户在使用此功能时，建议进行良好的轨迹规划，以确保机械臂的稳定运行。
            I系列有线网口周期最快可达2ms，提供了更高的实时性。
        Args:
            joint               (list[float]): 关节1~7目标角度数组,单位：°
            follow              (bool): true-高跟随，false-低跟随。若使用高跟随，透传周期要求不超过 10ms。
            expand              (float, optional): 如果存在通用扩展轴，并需要进行透传，可使用该参数进行透传发送。Defaults to 0.
            trajectory_mode     (int): 高跟随模式下，0-完全透传模式、1-曲线拟合模式、2-滤波模式
            radio               (int): 曲线拟合模式和滤波模式下的平滑系数（数值越大效果越好），滤波模式下取值范围0~100，曲线拟合模式下取值范围0~999

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
        """
        config = rm_movej_canfd_mode_t()
        joint_array = (c_float * 7)(*joint)
        config.joint = ctypes.pointer(joint_array)
        config.follow = follow
        config.expand = expand
        config.trajectory_mode = trajectory_mode
        config.radio = radio

        tag = rm_movej_canfd(self.handle, config)

        return tag

    def rm_movep_canfd(self, pose: list[float], follow: bool, trajectory_mode: int = 0, radio: int = 0) -> int:
        """
        位姿不经规划，直接通过CANFD透传给机械臂
        @details 当目标位姿被透传到机械臂控制器时，控制器首先尝试进行逆解计算。
        若逆解成功且计算出的各关节角度与当前角度差异不大，则直接下发至关节执行，跳过额外的轨迹规划步骤。
        这一特性适用于需要周期性调整位姿的场景，如视觉伺服等应用。
        <b>备注</b>：
            透传效果受通信周期和轨迹平滑度影响，因此要求通信周期稳定，避免大幅波动。
            用户在使用此功能时，建议进行良好的轨迹规划，以确保机械臂的稳定运行。
            I系列有线网口周期最快可达2ms，提供了更高的实时性。
        Args:
            pose (list[float]): 位姿 (若位姿列表长度为7则认为使用四元数表达位姿，长度为6则认为使用欧拉角表达位姿)
            follow (bool): true-高跟随，false-低跟随。若使用高跟随，透传周期要求不超过 10ms。
            trajectory_mode     (int): 高跟随模式下，0-完全透传模式、1-曲线拟合模式、2-滤波模式
            radio               (int): 曲线拟合模式和滤波模式下的平滑系数（数值越大效果越好），滤波模式下取值范围0~100，曲线拟合模式下取值范围0~999

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
        """
        config = rm_movep_canfd_mode_t()
        config.pose.position = rm_position_t(*pose[:3])
        # 四元数
        if len(pose) == 7:
            config.pose.quaternion = rm_quat_t(*pose[3:])
        # 欧拉角
        elif len(pose) == 6:
            config.pose.euler = rm_euler_t(*pose[3:])
        else:
            print("Error: pose length is error.")
        config.follow = follow
        config.trajectory_mode = trajectory_mode
        config.radio = radio

        tag = rm_movep_canfd(self.handle, config)

        return tag

    def rm_movej_follow(self, joint: list[float]) -> int:
        """
        关节空间跟随运动

        Args:
            joint (list[float]): 关节1~7目标角度数组,单位：°

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
        """
        if self.arm_dof != 0 and self.arm_dof == len(joint):
            joint_positions = (c_float * self.arm_dof)(*joint)
        else:
            joint_positions = (c_float * ARM_DOF)(*joint)

        tag = rm_movej_follow(self.handle, joint_positions)

        return tag

    def rm_movep_follow(self, pose: list[float]) -> int:
        """
        笛卡尔空间跟随运动

        Args:
            pose (list[float]): 位姿 (若位姿列表长度为7则认为使用四元数表达位姿，长度为6则认为使用欧拉角表达位姿)

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
        """
        po1 = rm_pose_t()

        po1.position = rm_position_t(*pose[:3])
        # 四元数
        if len(pose) == 7:
            po1.quaternion = rm_quat_t(*pose[3:])
        # 欧拉角
        elif len(pose) == 6:
            po1.euler = rm_euler_t(*pose[3:])
        else:
            print("Error: pose length is error.")

        tag = rm_movep_follow(self.handle, po1)

        return tag


class ArmTeachMove:
    """
    机械臂示教及步进运动
    """

    def rm_set_joint_step(self, num: int, step: float, v: int, block: int) -> int:
        """
        关节步进

        Args:
            num (int): 关节序号，1~7
            step (float): 步进的角度，
            v (int): 速度百分比系数，1~100
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        tag = rm_set_joint_step(self.handle, num, step, v, block)
        return tag

    def rm_set_pos_step(self, teach_type: rm_pos_teach_type_e, step: float, v: int, block: int) -> int:
        """
        当前工作坐标系下，位置步进

        Args:
            teach_type (rm_pos_teach_type_e): 示教类型
            step (float): 步进的距离，单位m，精确到0.001mm
            v (int): 速度百分比系数，1~100
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        tag = rm_set_pos_step(self.handle, teach_type, step, v, block)
        return tag

    def rm_set_ort_step(self, teach_type: rm_ort_teach_type_e, step: float, v: int, block: int) -> int:
        """
        当前工作坐标系下，姿态步进

        Args:
            teach_type (rm_ort_teach_type_e): 示教类型
            step (float): 步进的弧度，单位rad，精确到0.001rad
            v (int): 速度百分比系数，1~100
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为关节。
            - -5: 单线程模式超时未接收到返回，请确保超时时间设置合理。
        """
        tag = rm_set_ort_step(self.handle, teach_type, step, v, block)
        return tag

    def rm_set_joint_teach(self, num: int, direction: int, v: int) -> int:
        """
        关节示教

        Args:
            num (int): 示教关节的序号，1~7
            direction (int): 示教方向，0-负方向，1-正方向
            v (int): 速度百分比系数，1~100

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_joint_teach(self.handle, num, direction, v)
        return tag

    def rm_set_pos_teach(self, teach_type: rm_pos_teach_type_e, direction: int, v: int) -> int:
        """
        当前工作坐标系下，笛卡尔空间位置示教

        Args:
            teach_type (rm_pos_teach_type_e): 示教类型
            direction (int): 示教方向，0-负方向，1-正方向
            v (int): 即规划速度和加速度占机械臂末端最大线速度和线加速度的百分比

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_pos_teach(self.handle, teach_type, direction, v)
        return tag

    def rm_set_ort_teach(self, teach_type: rm_ort_teach_type_e, direction: int, v: int) -> int:
        """
        当前工作坐标系下，笛卡尔空间姿态示教

        Args:
            teach_type (rm_ort_teach_type_e): 示教类型
            direction (int): 示教方向，0-负方向，1-正方向
            v (int): 速度比例1~100，即规划速度和加速度占机械臂末端最大角速度和角加速度的百分比

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_ort_teach(self.handle, teach_type, direction, v)
        return tag

    def rm_set_stop_teach(self) -> int:
        """
        示教停止

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_stop_teach(self.handle)
        return tag

    def rm_set_teach_frame(self, frame_type: int) -> int:
        """
        切换示教运动坐标系

        Args:
            frame_type (int): 0: 工作坐标系运动, 1: 工具坐标系运动

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_teach_frame(self.handle, frame_type)
        return tag

    def rm_get_teach_frame(self) -> tuple[int, int]:
        """
        获取示教参考坐标系

        Returns:
            tuple[int,int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 0: 工作坐标系运动, 1: 工具坐标系运动
        """
        frame_type = c_int()
        tag = rm_get_teach_frame(self.handle, byref(frame_type))
        return tag, frame_type.value


class ArmMotionControl:
    """
    机械臂运动的急停、暂停、继续等控制
    """

    def rm_set_arm_slow_stop(self) -> int:
        """
        轨迹缓停，在当前正在运行的轨迹上停止

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_slow_stop(self.handle)
        return tag

    def rm_set_arm_stop(self) -> int:
        """
        轨迹急停，关节最快速度停止，轨迹不可恢复

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_stop(self.handle)
        return tag

    def rm_set_arm_pause(self) -> int:
        """
        轨迹暂停，暂停在规划轨迹上，轨迹可恢复

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_pause(self.handle)
        return tag

    def rm_set_arm_continue(self) -> int:
        """
        轨迹暂停后，继续当前轨迹运动

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_continue(self.handle)
        return tag

    def rm_set_delete_current_trajectory(self) -> int:
        """
        清除当前轨迹

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_delete_current_trajectory(self.handle)
        return tag

    def rm_set_arm_delete_trajectory(self) -> int:
        """
        清除所有轨迹

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_delete_trajectory(self.handle)
        return tag

    def rm_get_arm_current_trajectory(self) -> dict[str, any]:
        """
        获取当前正在规划的轨迹信息

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'trajectory_type' (rm_arm_current_trajectory_e): 返回的规划类型
            - 'data' (list[float]): 无规划和关节空间规划为当前关节1~7角度数组；笛卡尔空间规划则为当前末端位姿
        """
        plan_type = c_int()

        if self.arm_dof != 0:
            data = (c_float * self.arm_dof)()
        else:
            data = (c_float * ARM_DOF)()
        tag = rm_get_arm_current_trajectory(
            self.handle, byref(plan_type), data)

        # 创建一个字典来存储返回值
        result_dict = {
            'return_code': tag,
            'trajectory_type': plan_type.value,
            'data': list(data),
        }

        return result_dict


class ControllerConfig:
    """
    系统配置
    """

    def rm_get_controller_state(self) -> dict[str, any]:
        """
        获取控制器状态

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'voltage' (float): 返回的电压
            - 'current' (float): 返回的电流
            - 'temperature' (float): 返回的温度
            - 'sys_err' (int): 控制器运行错误代码
        """
        voltage = c_float()
        current = c_float()
        temperature = c_float()
        sys_err = c_int()
        ret = rm_get_controller_state(self.handle, byref(voltage), byref(current),
                                      byref(temperature), byref(sys_err))

        # 创建一个字典来存储返回值
        result_dict = {
            'return_code': ret,
            'voltage': voltage.value,
            'current': current.value,
            'temperature': temperature.value,
            'system_error': sys_err.value,
        }

        return result_dict

    def rm_set_arm_power(self, power: int) -> int:
        """
        设置机械臂电源

        Args:
            power (int): 1-上电状态，0 断电状态

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_arm_power(self.handle, power)
        return tag

    def rm_get_arm_power_state(self) -> tuple[int, int]:
        """
        读取机械臂电源状态

        Returns:
            tuple[int, int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 获取到的机械臂电源状态，1-上电状态，0 断电状态
        """
        power = c_int()
        tag = rm_get_arm_power_state(self.handle, byref(power))
        return tag, power.value

    def rm_get_system_runtime(self) -> dict[str, any]:
        """
        读取控制器的累计运行时间

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'day' (int): 读取到的时间
            - 'hour' (int): 读取到的时间
            - 'min' (int): 读取到的时间
            - 'sec' (int): 读取到的时间
        """
        day = c_int()
        hour = c_int()
        min = c_int()
        sec = c_int()

        ret = rm_get_system_runtime(self.handle, byref(
            day), byref(hour), byref(min), byref(sec))
        result_dict = {
            'return_code': ret,
            'day': day.value,
            'hour': hour.value,
            'min': min.value,
            'sec': sec.value,
        }

        return result_dict

    def rm_clear_system_runtime(self) -> int:
        """
        清零控制器的累计运行时间

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_clear_system_runtime(self.handle)
        return tag

    def rm_get_joint_odom(self) -> tuple[int, list[float]]:
        """
        读取关节的累计转动角度

        Returns:
            tuple[int, list[float]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list[float]: 各关节累计的转动角度，单位：度
        """
        if self.arm_dof != 0:
            joint_odom = (c_float * self.arm_dof)()
        else:
            joint_odom = (c_float * ARM_DOF)()

        ret = rm_get_joint_odom(self.handle, joint_odom)
        return ret, list(joint_odom)

    def rm_clear_joint_odom(self) -> int:
        """
        清零关节累计转动的角度

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_clear_joint_odom(self.handle)
        return tag

    def rm_get_arm_software_info(self) -> tuple[int, dict[str, any]]:
        """
        读取机械臂软件信息

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str,any]: 机械臂软件版本信息字典，键为rm_arm_software_version_t结构体的字段名称
        """
        version = rm_arm_software_version_t()
        ret = rm_get_arm_software_info(self.handle, byref(version))

        return ret, version.to_dict(self.robot_controller_version)

    def rm_set_netip(self, ip: str) -> int:
        """
        配置有线网口 IP 地址

        Args:
            ip (str): _description_

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_NetIP(self.handle, ip)
        return tag

    def rm_clear_system_err(self) -> int:
        """
        清除系统错误

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_clear_system_err(self.handle)
        return tag


class CommunicationConfig:
    """
    配置通讯内容

    @details 机械臂控制器可通过网口、WIFI、RS232-USB 接口和 RS485 接口与用户通信，用户使用时无需切换，可使用上述任一接口，
    控制器收到指令后，若指令格式正确，则会通过相同的接口反馈数据。
    """

    def rm_set_wifi_ap(self, wifi_name: str, password: str) -> int:
        """
        配置 wifiAP 模式

        Args:
            wifi_name (str): wifi名称
            password (str): wifi密码

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_wifi_ap(self.handle, wifi_name, password)
        return tag

    def rm_set_wifi_sta(self, router_name: str, password: str) -> int:
        """
        配置WiFi STA模式

        Args:
            router_name (str): 路由器名称
            password (str): 路由器Wifi密码

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_wifi_sta(self.handle, router_name, password)
        return tag

    def rm_set_RS485(self, baudrate: int) -> int:
        """
        控制器RS485接口波特率设置，设置成功后蜂鸣器响

        Args:
            baudrate (int): 波特率：9600,19200,38400,115200和460800，若用户设置其他数据，控制器会默认按照460800处理。

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 四代不支持该接口
        """
        tag = rm_set_RS485(self.handle, baudrate)
        return tag

    def rm_get_wired_net(self) -> dict[str, any]:
        """
        获取有线网卡信息，未连接有线网卡则会返回无效数据

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'ip' (str): 网络地址
            - 'mask' (str): 子网掩码
            - 'mac' (str): MAC地址
        """
        ip = ctypes.create_string_buffer(255)
        mask = ctypes.create_string_buffer(255)
        mac = ctypes.create_string_buffer(255)
        ret = rm_get_wired_net(self.handle, ip, mask, mac)
        result_dict = {
            'return_code': ret,
            'ip': ip.value.decode(),
            'mask': mask.value.decode(),
            'mac': mac.value.decode(),
        }

        return result_dict

    def rm_get_wifi_net(self) -> tuple[int, dict[str, any]]:
        """
        查询无线网卡网络信息

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str,any]: 无线网络信息字典，键为rm_wifi_net_t结构体的字段
        """
        net = rm_wifi_net_t()
        ret = rm_get_wifi_net(self.handle, byref(net))

        return ret, net.to_dict()

    def rm_set_net_default(self) -> int:
        """
        恢复网络出厂设置

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_net_default(self.handle)
        return tag

    def rm_set_wifi_close(self) -> int:
        """
        配置关闭 wifi 功能，需要重启后生效

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_wifi_close(self.handle)
        return tag


class ControllerIOConfig:
    """
    控制器端IO
    机械臂控制器提供IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
    """

    def rm_set_io_mode(self, io_num: int, io_mode: int, io_speed: int=0, io_speed_mode: int=0) -> int:
        """
        Args:
            io_num (int): IO 端口号，范围：1~4
            io_mode (int): 模式，0-通用输入模式，1-通用输出模式、2-输入开始功能复用模式、3-输入暂停功能复用模式、
            4-输入继续功能复用模式、5-输入急停功能复用模式、6-输入进入电流环拖动复用模式、7-输入进入力只动位置拖动模式（六维力版本可配置）、
            8-输入进入力只动姿态拖动模式（六维力版本可配置）、9-输入进入力位姿结合拖动复用模式（六维力版本可配置）、
            10-输入外部轴最大软限位复用模式（外部轴模式可配置）、11-输入外部轴最小软限位复用模式（外部轴模式可配置）、12-输入初始位姿功能复用模式、
            13-输出碰撞功能复用模式。
            io_speed (int): 速度取值范围0-100
            io_speed_mode (int): 模式取值范围1或2，
                                1表示单次触发模式,单次触发模式下当IO拉低速度设置为speed参数值，IO恢复高电平速度设置为初始值
                                2表示连续触发模式，连续触发模式下IO拉低速度设置为speed参数值，IO恢复高电平速度维持当前值

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        config = rm_io_config_t(io_mode=io_mode, io_real_time_config_t=rm_io_real_time_config_t(io_speed, io_speed_mode))
        tag = rm_set_IO_mode(self.handle, io_num, config)
        return tag

    def rm_set_do_state(self, io_num: int, state: int) -> int:
        """
        设置数字IO输出

        Args:
            io_num (int): IO 端口号，范围：1~4
            state (int): IO 状态，1-输出高，0-输出低

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_DO_state(self.handle, io_num, state)
        return tag

    def rm_get_io_state(self, io_num: int) -> tuple[int, dict[str, any]]:
        """
        获取数字 IO 状态

        Args:
            io_num (int): IO 端口号，范围：1~4

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'io_state' (int): io 状态
            - 'io_config' (dict): 配置字典
                - 'io_mode' (int):模式
                                0-通用输入模式，1-通用输出模式、2-输入开始功能复用模式、3-输入暂停功能复用模式、
                                4-输入继续功能复用模式、5-输入急停功能复用模式、6-输入进入电流环拖动复用模式、7-输入进入力只动位置拖动模式（六维力版本可配置）、
                                8-输入进入力只动姿态拖动模式（六维力版本可配置）、9-输入进入力位姿结合拖动复用模式（六维力版本可配置）、
                                10-输入外部轴最大软限位复用模式（外部轴模式可配置）、11-输入外部轴最小软限位复用模式（外部轴模式可配置）、
                                12-输入初始位姿功能复用模式、13-输出碰撞功能复用模式、14-实时调速功能复用模式
                - 'io_real_time_config_t' (dict):实时调速功能复用模式配置
                    - speed (int):速度取值范围0-100(当io_mode不为14时，默认值为-1)
                    - mode (int) :模式取值范围1或2 (当io_mode不为14时，默认值为-1)
                            1-单次触发模式，当IO拉低速度设置为speed参数值，IO恢复高电平速度设置为初始值
                            2-连续触发模式，IO拉低速度设置为speed参数值，IO恢复高电平速度维持当前值
        """
        config = rm_io_get_t()
        ret = rm_get_IO_state(self.handle, io_num, byref(config))

        return ret, config.to_dict()

    def rm_get_io_input(self) -> tuple[int, list[int]]:
        """
        获取所有 IO 输入状态

        Returns:
            tuple[int, list[int]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list[int]: 4路数字输入状态列表，1：高，0：低，-1：该端口不是输入模式
        """
        DI = (c_int * 4)()

        ret = rm_get_IO_input(self.handle, DI)

        return ret, list(DI)

    def rm_get_io_output(self) -> tuple[int, list[int]]:
        """
        获取所有 IO 输出状态

        Returns:
            tuple[int, list[int]]: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - list[int]: 4路数字输出状态列表，1：高，0：低，-1：该端口不是输出模式
        """
        DO = (c_int * 4)()

        ret = rm_get_IO_output(self.handle, DO)

        return ret, list(DO)

    def rm_set_voltage(self, voltage_type: int) -> int:
        """
        设置控制器电源输出

        Args:
            voltage_type (int): 电源输出类型，0：0V，2：12V，3：24V

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_voltage(self.handle, voltage_type)
        return tag

    def rm_get_voltage(self) -> tuple[int, int]:
        """
        获取控制器电源输出类

        Returns:
            tuple[int, int]: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 电源输出类型，0：0V，2：12V，3：24V
        """
        voltage_type = c_int()
        tag = rm_get_voltage(self.handle, byref(voltage_type))
        return tag, voltage_type.value

class EffectorIOConfig:
    """
   末端工具IO
    机械臂末端工具端提供多种IO端口，用于与外部设备交互。可查阅文档了解其数量分类等。
    """
    def rm_set_tool_do_state(self, io_num: int, state: int) -> int:
        """
        设置工具端数字 IO 输出

        Args:
            io_num (int): IO 端口号，范围：1~2
            state (int): IO 状态，1-输出高，0-输出低

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_tool_DO_state(self.handle, io_num, state)
        return tag

    def rm_set_tool_IO_mode(self, io_num: int, state: int) -> int:
        """
        设置工具端数字 IO 模式

        Args:
            io_num (int): IO 端口号，范围：1~2
            state (int): 模式，0-输入状态，1-输出状态

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_tool_IO_mode(self.handle, io_num, state)
        return tag

    def rm_get_tool_io_state(self) -> dict[str, any]:
        """
        获取数字 IO 状态

        Returns:
            dict[str, any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'IO_Mode' (list[int]): 0-输入模式，1-输出模式
            - 'IO_state' (list[int]): 0-低，1-高

        """
        mode = (c_int * 2)()
        state = (c_int * 2)()

        ret = rm_get_tool_IO_state(self.handle, mode, state)

        result_dict = {
            'return_code': ret,
            'IO_Mode': list(mode),
            'IO_state': list(state),
        }
        return result_dict

    def rm_set_tool_voltage(self, voltage_type: int) -> int:
        """
        设置工具端电源输出

        Args:
            voltage_type (int): 电源输出类型，0：0V，1：5V，2：12V，3：24V，

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_tool_voltage(self.handle, voltage_type)
        return tag

    def rm_get_tool_voltage(self) -> tuple[int, int]:
        """
        获取工具端电源输出

        Returns:
            tuple[int, int]: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 电源输出类型，0：0V，1：5V，2：12V，3：24V，
        """
        voltage_type = c_int()
        tag = rm_get_tool_voltage(self.handle, byref(voltage_type))
        return tag, voltage_type.value


class GripperControl:
    """
    夹爪控制及状态获取
    @details 睿尔曼机械臂末端配备了因时机器人公司的 EG2-4C2 手爪，为了便于用户操作手爪，机械臂控制器
    对用户开放了手爪的控制协议（手爪控制协议与末端modbus 功能互斥）
    """
    def rm_set_rm_plus_mode(self, mode: int) -> int:
        """
        设置末端生态协议模式
        Args:
            mode 末端生态协议模式
            0：禁用协议 
            9600：开启协议（波特率9600）
            115200：开启协议（波特率115200）
            256000：开启协议（波特率256000）
            460800：开启协议（波特率460800）

        Returns:
            int 设置末端生态协议模式结果 0成功
        """

        tag = rm_set_rm_plus_mode(self.handle, mode)
        return tag

    def rm_get_rm_plus_mode(self) -> tuple[int, int]:
        """
        查询末端生态协议模式
        Returns:
            tag 函数执行的状态码
            - 0: 成功
            - 1: 控制器返回false，传递参数错误或机械臂状态发生错误
            - -1: 数据发送失败，通信过程中出现问题
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整
            mode 末端生态协议模式
            - 0：禁用协议 
            - 9600：开启协议（波特率9600）
            - 115200：开启协议（波特率115200）
            - 256000：开启协议（波特率256000）
            - 460800：开启协议（波特率460800）
        """
        plus_mode_type = c_int()
        tag = rm_get_rm_plus_mode(self.handle, byref(plus_mode_type))
        return tag, plus_mode_type.value
    
    def rm_set_rm_plus_touch(self,mode: int) -> int:
        """
        设置触觉传感器模式(末端生态协议支持)
        Args:
            mode 触觉传感器开关状态 
            0：关闭触觉传感器 
            1：打开触觉传感器（返回处理后数据） 
            2：打开触觉传感器（返回原始数据）
        Returns:
            int 设置触觉传感器模式结果 0成功
        """
        tag = rm_set_rm_plus_touch(self.handle, mode)
        return tag
    
    def rm_get_rm_plus_touch(self) -> tuple[int,int]:
        """
        查询触觉传感器模式(末端生态协议支持)
        Returns:
            -触觉传感器模式查询状态
            -mode 触觉传感器开关状态 
              0：关闭触觉传感器 
              1：打开触觉传感器（返回处理后数据） 
              2：打开触觉传感器（返回原始数据）
        """
        plus_touch_type = c_int()
        tag = rm_get_rm_plus_touch(self.handle, byref(plus_touch_type))
        return tag, plus_touch_type.value

    def rm_get_rm_plus_base_info(self) -> tuple[int,dict[str, any]]:
        """
        读取末端设备基础信息(末端生态协议支持)
        Returns:
            -函数执行的状态码
            -rm_plus_base_info_t 末端设备基础信息
        """
        base_info_type = rm_plus_base_info_t()
        tag = rm_get_rm_plus_base_info(self.handle, byref(base_info_type))
        return tag, base_info_type.to_dict()
    
    def rm_get_rm_plus_state_info(self) -> tuple[int, dict[str, any]]:
        """
        读取末端设备实时信息(末端生态协议支持)
        Returns:
            -函数执行的状态码
            -rm_plus_state_info_t 末端设备实时信息
        """
        state_info_type = rm_plus_state_info_t()
        tag = rm_get_rm_plus_state_info(self.handle, byref(state_info_type))
        return tag, state_info_type.to_dict()


    def rm_set_gripper_route(self, min_route: int, max_route: int) -> int:
        """
        设置手爪行程，即手爪开口的最大值和最小值，设置成功后会自动保存，手爪断电不丢失

        Args:
            min_route (int): 手爪开口最小值，范围：0~1000，无单位量纲
            max_route (int): 手爪开口最大值，范围：0~1000，无单位量纲

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4:超时
        """
        tag = rm_set_gripper_route(self.handle, min_route, max_route)
        return tag

    def rm_set_gripper_release(self, speed: int, block: bool, timeout: int) -> int:
        """
        松开手爪，即手爪以指定的速度运动到开口最大处

        Args:
            speed (int): 手爪松开速度，范围 1~1000，无单位量纲
            block (bool): true 表示阻塞模式，等待控制器返回夹爪到位指令；false 表示非阻塞模式，不接收夹爪到位指令；
            timeout (int): 阻塞模式：设置等待夹爪到位超时时间，单位：秒
                            非阻塞模式：0-发送后立即返回；其他值-接收设置成功指令后返回；

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4:超时
        """
        tag = rm_set_gripper_release(self.handle, speed, block, timeout)
        return tag

    def rm_set_gripper_pick(self, speed: int, force: int, block: bool, timeout: int) -> int:
        """
        手爪力控夹取，手爪以设定的速度和力夹取，当夹持力超过设定的力阈值后，停止夹取

        Args:
            speed (int): 手爪夹取速度，范围 1~1000，无单位量纲
            force (int): 力控阈值，范围：50~1000，无单位量纲
            block (bool): true 表示阻塞模式，等待控制器返回夹爪到位指令；false 表示非阻塞模式，不接收夹爪到位指令；
            timeout (int): 阻塞模式：设置等待夹爪到位超时时间，单位：秒
                            非阻塞模式：0-发送后立即返回；其他值-接收设置成功指令后返回；

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4:超时
        """
        tag = rm_set_gripper_pick(self.handle, speed, force, block, timeout)
        return tag

    def rm_set_gripper_pick_on(self, speed: int, force: int, block: bool, timeout: int) -> int:
        """
        手爪持续力控夹取

        Args:
            speed (int): 手爪夹取速度，范围 1~1000，无单位量纲
            force (int): 力控阈值，范围：50~1000，无单位量纲
            block (bool): true 表示阻塞模式，等待控制器返回夹爪到位指令；false 表示非阻塞模式，不接收夹爪到位指令；
            timeout (int): 阻塞模式：设置等待夹爪到位超时时间，单位：秒
                            非阻塞模式：0-发送后立即返回；其他值-接收设置成功指令后返回；

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4:超时
        """
        tag = rm_set_gripper_pick_on(self.handle, speed, force, block, timeout)
        return tag

    def rm_set_gripper_position(self, position: int, block: bool, timeout: int) -> int:
        """
        设置手爪达到指定位置

        Args:
            position (int): 手爪开口位置，范围：1~1000，无单位量纲
            block (bool): true 表示阻塞模式，等待控制器返回夹爪到位指令；false 表示非阻塞模式，不接收夹爪到位指令；
            timeout (int): 阻塞模式：设置等待夹爪到位超时时间，单位：秒
                            非阻塞模式：0-发送后立即返回；其他值-接收设置成功指令后返回；

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4:超时
        """
        tag = rm_set_gripper_position(self.handle, position, block, timeout)
        return tag

    def rm_get_gripper_state(self) -> tuple[int, dict[str, any]]:
        """
        查询夹爪状态

        Returns:
            tuple[int,dict[str, any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str, any]: 夹爪状态信息字典，键为rm_gripper_state_t结构体的字段名称
        """
        state = rm_gripper_state_t()
        tag = rm_get_gripper_state(self.handle, byref(state))
        return tag, state.to_dict()


class Force:
    """
    末端力传感器
    @details
    **六维力**
    睿尔曼机械臂六维力版末端配备集成式六维力传感器，无需外部走线，用户可直接通过协议对六维力进行操作，
    获取六维力数据。如下图所示，正上方为六维力的 Z 轴，航插反方向为六维力的 Y 轴，坐标系符合右手定则。
    机械臂位于零位姿态时，工具坐标系与六维力的坐标系方向一致。
    另外，六维力额定力 200N，额定力矩 8Nm，过载水平 300%FS，工作温度 5~80℃，准度 0.5%FS。使用过程中
    注意使用要求，防止损坏六维力传感器。
    @image html force.png "六维力坐标系"
    **一维力**
    睿尔曼机械臂一维力版末端接口板集成了一维力传感器，可获取 Z 方向的力，量程200N，准度 0.5%FS。
    @image html oneforce.png "一维力坐标系"
    """

    def rm_get_force_data(self) -> tuple[int, dict[str, any]]:
        """
        查询当前六维力传感器得到的力和力矩信息：Fx,Fy,Fz,Mx,My,Mz

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str, any]: 六维力数据字典，键为rm_force_data_t结构体的字段名称
        """
        data = rm_force_data_t()
        tag = rm_get_force_data(self.handle, byref(data))
        return tag, data.to_dict()

    def rm_clear_force_data(self) -> int:
        """
        将六维力数据清零，标定当前状态下的零位

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_clear_force_data(self.handle)
        return tag

    def rm_set_force_sensor(self, block: bool) -> int:
        """
        自动设置六维力重心参数
        @details 设置六维力重心参数，六维力重新安装后，必须重新计算六维力所受到的初始力和重心。分别在不同姿态下，获取六维力的数据，
        用于计算重心位置。该指令下发后，机械臂以固定的速度运动到各标定点。
        以RM65机械臂为例，四个标定点的关节角度分别为：
            位置1关节角度：{0,0,-60,0,60,0}
            位置2关节角度：{0,0,-60,0,-30,0}
            位置3关节角度：{0,0,-60,0,-30,180}
            位置4关节角度：{0,0,-60,0,-120,0}
        Args:
            block (bool): true 表示阻塞模式，等待标定完成后返回；false 表示非阻塞模式，发送后立即返回

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_force_sensor(self.handle, block)
        return tag

    def rm_manual_set_force(self, point_num: int, joint: list[float], block: bool) -> int:
        """
        手动标定六维力数据

        @details 六维力重新安装后，必须重新计算六维力所受到的初始力和重心。该手动标定流程，适用于空间狭窄工作区域，以防自动标定过程中
        机械臂发生碰撞，用户可以手动选取四个位置下发，当下发完四个点后，机械臂开始自动沿用户设置的目标运动，并在此过程中计算六维力重心。
        @attention 上述4个位置必须按照顺序依次下发，当下发完位置4后，机械臂开始自动运行计算重心。

        Args:
            point_num (int): 点位；1~4
            joint (list[float]): 关节角度，单位：°
            block (bool): true 表示阻塞模式，等待标定完成后返回；false 表示非阻塞模式，发送后立即返回

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)(*joint)
        else:
            joint_positions = (c_float * ARM_DOF)(*joint)
        tag = rm_manual_set_force(
            self.handle, point_num, joint_positions, block)
        return tag

    def rm_stop_set_force_sensor(self) -> int:
        """
        停止标定力传感器重心

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_stop_set_force_sensor(self.handle)
        return tag

    def rm_get_fz(self) -> tuple[int, dict[str, any]]:
        """
        查询末端一维力数据

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str, any]: 一维力数据字典，键为rm_fz_data_t结构体的字段名称
        """
        data = rm_fz_data_t()
        tag = rm_get_Fz(self.handle, byref(data))
        return tag, data.to_dict()

    def rm_clear_fz(self) -> int:
        """
        清零末端一维力数据，清空一维力数据后，后续所有获取到的数据都是基于当前的偏置。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_clear_Fz(self.handle)
        return tag

    def rm_auto_set_fz(self, block: bool) -> int:
        """
        自动标定一维力数据
        @details 设置一维力重心参数，一维力重新安装后，必须重新计算一维力所受到的初始力和重心。
        分别在不同姿态下，获取一维力的数据，用于计算重心位置，该步骤对于基于一维力的力位混合控制操作具有重要意义。
        Args:
            block (bool): true 表示阻塞模式，等待标定完成后返回；false 表示非阻塞模式，发送后立即返回

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_auto_set_Fz(self.handle, block)
        return tag

    def rm_manual_set_fz(self, joint1: list[float], joint2: list[float], block: bool) -> int:
        """
        手动标定一维力数据
        @details 设置一维力重心参数，一维力重新安装后，必须重新计算一维力所受到的初始力和重心。该手动标定流程，
        适用于空间狭窄工作区域，以防自动标定过程中机械臂发生碰撞，用户可以手动选取2个位置下发，当下发完后，
        机械臂开始自动沿用户设置的目标运动，并在此过程中计算一维力重心。

        Args:
            joint1 (list[float]): 位置1关节角度数组，单位：度
            joint2 (list[float]): 位置2关节角度数组，单位：度
            block (bool): true 表示阻塞模式，等待标定完成后返回；false 表示非阻塞模式，发送后立即返回

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        if self.arm_dof != 0:
            joint_positions1 = (c_float * self.arm_dof)(*joint1)
            joint_positions2 = (c_float * self.arm_dof)(*joint2)
        else:
            joint_positions1 = (c_float * ARM_DOF)(*joint1)
            joint_positions2 = (c_float * ARM_DOF)(*joint2)
        tag = rm_manual_set_Fz(
            self.handle, joint_positions1, joint_positions2, block)
        return tag


class DragTeach:
    """
    拖动示教

    @details 睿尔曼机械臂在拖动示教过程中，可记录拖动的轨迹点，并根据用户的指令对轨迹进行复现。
    """

    def rm_start_drag_teach(self, trajectory_record: int) -> int:
        """
        拖动示教开始

        Args:
            trajectory_record (int): 拖动示教时记录轨迹，0-不记录，1-记录轨迹

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_start_drag_teach(self.handle, trajectory_record)
        return tag

    def rm_stop_drag_teach(self) -> int:
        """
        拖动示教结束

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_stop_drag_teach(self.handle)
        return tag

    def rm_start_multi_drag_teach(self, mode: int, singular_wall: int) -> int:
        """
        开始复合模式拖动示教
        仅支持三代控制器，四代控制器使用rm_start_multi_drag_teach_new

        Args:
            mode (int): 拖动示教模式 0-电流环模式，1-使用末端六维力，只动位置，2-使用末端六维力，只动姿态，3-使用末端六维力，位置和姿态同时动
            singular_wall (int): 仅在六维力模式拖动示教中生效，用于指定是否开启拖动奇异墙，0表示关闭拖动奇异墙，1表示开启拖动奇异墙

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        @attention 失败的可能原因:
            - 当前机械臂非六维力版本（六维力拖动示教）。
            - 机械臂当前处于 IO 急停状态
            - 机械臂当前处于仿真模式
            - 输入参数有误
            - 使用六维力模式拖动示教时，当前已处于奇异区
        """
        tag = rm_start_multi_drag_teach(self.handle, mode, singular_wall)
        return tag

    def rm_start_multi_drag_teach_new(self, param: rm_multi_drag_teach_t) -> int:
        """
        开始复合模式拖动示教-新参数

        Args:
            param (rm_multi_drag_teach_t): 复合拖动示教参数

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        @attention 失败的可能原因:
            - 当前机械臂非六维力版本（六维力拖动示教）。
            - 机械臂当前处于 IO 急停状态
            - 机械臂当前处于仿真模式
            - 输入参数有误
            - 使用六维力模式拖动示教时，当前已处于奇异区
        """
        tag = rm_start_multi_drag_teach_new(self.handle, param)
        return tag

    def rm_set_drag_teach_sensitivity(self, grade: int) -> int:
        """
        设置电流环拖动示教灵敏度

        Args:
            grade (int): 灵敏度等级，取值范围0~100%，数值越小越沉，当设置为100时保持原本拖动灵敏度

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_drag_teach_sensitivity(self.handle, grade)
        return tag

    def rm_get_drag_teach_sensitivity(self) -> tuple[int, int]:
        """
        获取电流环拖动示教灵敏度

        Returns:
            tuple[int, int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 灵敏度等级，取值范围0~100%，数值越小越沉，当设置为100时保持原本拖动灵敏度
        """
        grade = c_int()
        tag = rm_get_drag_teach_sensitivity(self.handle, byref(grade))
        return tag, grade.value
    
    def rm_drag_trajectory_origin(self, block: int) -> int:
        """
        运动到轨迹起点
        @details 轨迹复现前，必须控制机械臂运动到轨迹起点，如果设置正确，机械臂将以20%的速度运动到轨迹起点

        Args:
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_drag_trajectory_origin(self.handle, block)
        return tag

    def rm_run_drag_trajectory(self, timeout: int) -> int:
        """
        轨迹复现开始
        @attention 必须在拖动示教结束后才能使用，同时保证机械臂位于拖动示教的起点位置，可调用rm_drag_trajectory_origin接口运动至起点位置
        Args:
            timeout (int): 阻塞设置
            - 多线程模式：
                - 0：非阻塞模式，发送指令后立即返回。
                - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
            - 单线程模式：
                - 0：非阻塞模式。
                - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_run_drag_trajectory(self.handle, timeout)
        return tag

    def rm_pause_drag_trajectory(self) -> int:
        """
        控制机械臂在轨迹复现过程中的暂停

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_pause_drag_trajectory(self.handle)
        return tag

    def rm_continue_drag_trajectory(self) -> int:
        """
        控制机械臂在轨迹复现过程中暂停之后的继续，

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_continue_drag_trajectory(self.handle)
        return tag

    def rm_stop_drag_trajectory(self) -> int:
        """
        控制机械臂在轨迹复现过程中的停止

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_stop_drag_trajectory(self.handle)
        return tag

    def rm_set_force_position(self, sensor: int, mode: int, direction: int, force: float) -> int:
        """
        力位混合控制
        @details 在笛卡尔空间轨迹规划时，使用该功能可保证机械臂末端接触力恒定，使用时力的方向与机械臂运动方向不能在同一方向。
        开启力位混合控制，执行笛卡尔空间运动，接收到运动完成反馈后，需要等待2S后继续下发下一条运动指令。
        Args:
            sensor (int): 0-一维力；1-六维力
            mode (int): 0-基坐标系力控；1-工具坐标系力控；
            direction (int): 力控方向；0-沿X轴；1-沿Y轴；2-沿Z轴；3-沿RX姿态方向；4-沿RY姿态方向；5-沿RZ姿态方向
            force (float): 力的大小，单位N

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_force_position(
            self.handle, sensor, mode, direction, force)
        return tag
    
    def rm_set_force_position_new(self, param: rm_force_position_t) -> int:
        """
        力位混合控制-新参数
        @details 在笛卡尔空间轨迹规划时，使用该功能可保证机械臂末端接触力恒定，使用时力的方向与机械臂运动方向不能在同一方向。
        开启力位混合控制，执行笛卡尔空间运动，接收到运动完成反馈后，需要等待2S后继续下发下一条运动指令。
        Args:
            param (rm_force_position_t): 力位混合控制参数

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_force_position_new(self.handle, param)
        return tag

    def rm_stop_force_position(self) -> int:
        """
        结束力位混合控制

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_stop_force_position(self.handle)
        return tag

    def rm_save_trajectory(self, file_path: str) -> tuple[int, int]:
        """
        保存拖动示教轨迹

        Args:
            file_path (str): 轨迹要保存的文件路径及名称，例: c:/rm_test.txt

        Returns:
            tuple[int,int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - int: 轨迹点总数
        """
        num = c_int()
        tag = rm_save_trajectory(self.handle, file_path, byref(num))
        return tag, num.value
    
    def rm_set_force_drag_mode(self, mode: int) -> int:
        """
        设置六维力拖动示教模式

        Args:
            mode (int): 0表示快速拖动模式 1表示精准拖动模式

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 非六维力版本机械臂，不支持此功能。
        """
        tag = rm_set_force_drag_mode(self.handle, mode)
        return tag

    def rm_get_force_drag_mode(self) -> tuple[int, int]:
        """
        查询六维力拖动示教模式

        Returns:
            tuple[int, int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 非六维力版本机械臂，不支持此功能。
            - int: 0表示快速拖动模式 1表示精准拖动模式
        """
        mode = c_int()
        tag = rm_get_force_drag_mode(self.handle, byref(mode))
        return tag, mode.value
    

class HandControl:
    """
    五指灵巧手控制
    """

    def rm_set_hand_posture(self, posture_num: int, block: bool, timeout: int) -> int:
        """
        设置灵巧手目标手势序列号

        Args:
            posture_num (int): 预先保存在灵巧手内的手势序号，范围：1~40
            block (bool): true 表示阻塞模式，等待灵巧手运动结束后返回；false 表示非阻塞模式，发送后立即返回
            timeout (int): 阻塞模式下超时时间设置，单位：秒

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为灵巧手
            - -5: 超时未返回。
        """
        tag = rm_set_hand_posture(self.handle, posture_num, block, timeout)
        return tag

    def rm_set_hand_seq(self, seq_num: int, block: bool, timeout: int) -> int:
        """
        设置灵巧手目标手势序列号

        Args:
            seq_num (int): 预先保存在灵巧手内的手势序号，范围：1~40
            block (bool): true 表示阻塞模式，等待灵巧手运动结束后返回；false 表示非阻塞模式，发送后立即返回
            timeout (int): 阻塞模式下超时时间设置，单位：秒

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 当前到位设备校验失败，即当前到位设备不为灵巧手
            - -5: 超时未返回。
        """
        tag = rm_set_hand_seq(self.handle, seq_num, block, timeout)
        return tag

    def rm_set_hand_angle(self, hand_angle: list[int]) -> int:
        """
        设置灵巧手各自由度角度
        @details 设置灵巧手角度，灵巧手有6个自由度，从1~6分别为小拇指，无名指，中指，食指，大拇指弯曲，大拇指旋转
        Args:
            hand_angle (list[int]): 手指角度数组，范围：0~1000. 另外，-1代表该自由度不执行任何操作，保持当前状态

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 超时未返回
        """
        angle = (c_int * 6)(*hand_angle)
        tag = rm_set_hand_angle(self.handle, angle)
        return tag

    def rm_set_hand_follow_angle(self, hand_angle: list[int], block:bool) -> int:
        """
        设置灵巧手角度跟随控制
        @details 设置灵巧手跟随角度，灵巧手有6个自由度，从1~6分别为小拇指，无名指，中指，食指，大拇指弯曲，大拇指旋转
        Args:
            hand_angle (list[int]): 手指角度数组，最大表示范围为-32768到+32767，按照灵巧手厂商定义的角度做控制，例如因时的范围为0-2000
            block (int): 设置0时为非阻塞模式；1位阻塞模式，超时时间20ms

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 超时未返回
        """
        angle = (c_int * 6)(*hand_angle)
        tag = rm_set_hand_follow_angle(self.handle, angle, block)
        return tag

    def rm_set_hand_follow_pos(self, hand_pos: list[int], block:bool) -> int:
        """
        设置灵巧手位置跟随控制
        @details 设置灵巧手跟随角度，灵巧手有6个自由度，从1~6分别为小拇指，无名指，中指，食指，大拇指弯曲，大拇指旋转
        Args:
            hand_pos (list[int]): 手指位置数组，最大范围为0-65535，按照灵巧手厂商定义的角度做控制，例如因时的范围为0-1000
            block (int): 设置0时为非阻塞模式；1位阻塞模式，超时时间20ms

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 超时未返回
        """
        pos = (c_int * 6)(*hand_pos)
        tag = rm_set_hand_follow_pos(self.handle, pos, block)
        return tag
    
    def rm_set_hand_speed(self, speed: int) -> int:
        """
        设置灵巧手速度

        Args:
            speed (int): 手指速度，范围：1~1000

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 超时未返回
        """
        tag = rm_set_hand_speed(self.handle, speed)
        return tag

    def rm_set_hand_force(self, force: int) -> int:
        """
        设置灵巧手力阈值

        Args:
            force (int): 手指力，范围：1~1000

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 超时未返回
        """
        tag = rm_set_hand_force(self.handle, force)
        return tag


class ModbusConfig:
    """
    Modbus 配置

    @details 睿尔曼机械臂在控制器和末端接口板上各提供一个RS485通讯接口，这些接口可通过接口配置为标准的Modbus RTU模式。
    在Modbus RTU模式下，用户可通过提供的接口对连接在端口上的外设进行读写操作。

    @attention
        - 控制器的RS485接口在未配置为Modbus RTU模式时，可用于直接控制机械臂。
        - Modbus RTU模式与机械臂控制模式不兼容。若需恢复机械臂控制模式，必须关闭该端口的Modbus RTU模式。
        - 关闭Modbus RTU模式后，系统将自动切换回机械臂控制模式，使用波特率460800BPS，停止位1，数据位8，无校验。

    此外，I系列控制器还支持modbus-TCP主站配置，允许用户配置使用modbus-TCP主站，以连接外部设备的modbus-TCP从站。
    """

    def rm_set_modbus_mode(self, port: int, baudrate: int, timeout: int) -> int:
        """
        配置通讯端口ModbusRTU模式

        Args:
            port (int): 通讯端口，0-控制器RS485端口为RTU主站，1-末端接口板RS485接口为RTU主站，2-控制器RS485端口为RTU从站
            baudrate (int): 波特率，支持 9600,115200,460800 三种常见波特率
            timeout (int): 超时时间，单位百毫秒。。对Modbus设备所有的读写指令，在规定的超时时间内未返回响应数据，则返回超时报错提醒。超时时间不能为0，若设置为0，则机械臂按1进行配置。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_set_modbus_mode(self.handle, port, baudrate, timeout)
        return tag

    def rm_close_modbus_mode(self, port: int) -> int:
        """
        关闭通讯端口 Modbus RTU 模式

        Args:
            port (int): 通讯端口，0-控制器RS485端口为RTU主站，1-末端接口板RS485接口为RTU主站，2-控制器RS485端口为RTU从站

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_close_modbus_mode(self.handle, port)
        return tag

    def rm_set_modbustcp_mode(self, ip: str, port: int, timeout: int) -> int:
        """
        配置连接
        Args:
            ip (str): 从机IP地址
            port (int): 端口号
            timeout (int): 超时时间，单位毫秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_set_modbustcp_mode(self.handle, ip, port, timeout)
        return tag

    def rm_close_modbustcp_mode(self) -> int:
        """
        关闭通讯端口ModbusRTU模式

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_close_modbustcp_mode(self.handle)
        return tag

    def rm_read_coils(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, int]:
        """
        读线圈

        Args:
            read_params (rm_peripheral_read_write_params_t): 线圈读取参数结构体，该指令最多一次性支持读 8 个线圈数据，即返回的数据不会超过一个字节

        Returns:
            tuple[int,int]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - int: 返回线圈状态，数据类型：int8
        """
        data = c_int()
        tag = rm_read_coils(self.handle, read_params, byref(data))
        return tag, data.value

    def rm_read_input_status(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, int]:
        """
        读离散量输入

        Args:
            read_params (rm_peripheral_read_write_params_t): 离散量输入读取参数结构体，该指令最多一次性支持读 8 个离散量数据，即返回的数据不会超过一个字节

        Returns:
            tuple[int,int]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - int: 返回离散量，数据类型：int8
        """
        data = c_int()
        tag = rm_read_input_status(self.handle, read_params, byref(data))
        return tag, data.value

    def rm_read_holding_registers(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, int]:
        """
        读保持寄存器

        Args:
            read_params (rm_peripheral_read_write_params_t): 保持寄存器数据读取参数结构体，该指令每次只能读 1 个寄存器，即 2 个字节的数据，不可一次性读取多个寄存器数据，该结构体成员num无需设置

        Returns:
            tuple[int,int]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - int: 返回寄存器数据，数据类型：int16
        """
        data = c_int()
        tag = rm_read_holding_registers(self.handle, read_params, byref(data))
        return tag, data.value

    def rm_read_input_registers(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, int]:
        """
        读输入寄存器

        Args:
            read_params (rm_peripheral_read_write_params_t): 输入寄存器数据读取参数结构体，该指令每次只能读 1 个寄存器，即 2 个字节的数据，不可一次性读取多个寄存器数据，该结构体成员num无需设置

        Returns:
            tuple[int,int]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - int: 返回寄存器数据，数据类型：int16
        """
        data = c_int()
        tag = rm_read_input_registers(self.handle, read_params, byref(data))
        return tag, data.value

    def rm_write_single_coil(self, write_params: rm_peripheral_read_write_params_t, data: int) -> int:
        """
        写单圈数据

        Args:
            write_params (rm_peripheral_read_write_params_t): 单圈数据写入参数结构体，该结构体成员num无需设置
            data (int): 要写入线圈的数据，数据类型：int16

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_write_single_coil(self.handle, write_params, data)
        return tag

    def rm_write_single_register(self, write_params: rm_peripheral_read_write_params_t, data: int) -> int:
        """
        写单个寄存器

        Args:
            write_params (rm_peripheral_read_write_params_t): 单个寄存器数据写入参数结构体，该结构体成员num无需设置
            data (int): 要写入寄存器的数据，类型：int16

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        tag = rm_write_single_register(self.handle, write_params, data)
        return tag

    def rm_write_registers(self, write_params: rm_peripheral_read_write_params_t, data: list[int]) -> int:
        """
        写多个寄存器

        Args:
            write_params (rm_peripheral_read_write_params_t): 多个寄存器数据写入参数结构体。其中寄存器每次写的数量不超过10个，即该结构体成员num<=10。
            data (list[int]): 要写入寄存器的数据数组，类型：byte。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        data_num = int(write_params.num * 2)
        datas = (c_int * data_num)(*data)
        tag = rm_write_registers(self.handle, write_params, datas)
        return tag

    def rm_write_coils(self, write_params: rm_peripheral_read_write_params_t, data: list[int]) -> int:
        """
        写多圈数据

        Args:
            write_params (rm_peripheral_read_write_params_t): 多圈数据写入参数结构体。每次写的数量不超过 160 个，即该结构体成员num<=160。
            data (list[int]): 要写入线圈的数据数组，类型：byte。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 读取失败，超时时间内未获取到数据。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 四代控制器不支持该接口
        """
        data_num = int(write_params.num // 8 + 1)
        datas = (c_int * data_num)(*data)
        tag = rm_write_coils(self.handle, write_params, datas)
        return tag

    def rm_read_multiple_coils(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, list[int]]:
        """
        读多圈数据

        Args:
            read_params (rm_peripheral_read_write_params_t): 多圈数据读取参数结构体，要读的线圈的数量 8< num <= 120，该指令最多一次性支持读 120 个线圈数据， 即 15 个 byte

        Returns:
            tuple[int,list[int]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - list[int]: 返回线圈状态列表，数据类型：int8
        """
        data_num = int(read_params.num//8+1)
        data = (c_int * data_num)()
        tag = rm_read_multiple_coils(self.handle, read_params, data)
        return tag, list(data)

    def rm_read_multiple_holding_registers(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, list[int]]:
        """
        读多个保存寄存器

        Args:
            read_params (rm_peripheral_read_write_params_t): 多个保存寄存器读取参数结构体，要读的寄存器的数量 2 < num < 13，该指令最多一次性支持读 12 个寄存器数据， 即 24 个 byte

        Returns:
            tuple[int,list[int]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - list[int]: 返回寄存器数据列表，数据类型：int8
        """
        data_num = int(read_params.num * 2)
        data = (c_int * data_num)()
        tag = rm_read_multiple_holding_registers(
            self.handle, read_params, data)
        return tag, list(data)

    def rm_read_multiple_input_registers(self, read_params: rm_peripheral_read_write_params_t) -> tuple[int, list[int]]:
        """
        读多个输入寄存器

        Args:
            read_params (rm_peripheral_read_write_params_t): 多个输入寄存器读取参数结构体。要读的寄存器的数量 2 < num < 13，该指令最多一次性支持读 12 个寄存器数据， 即 24 个 byte

        Returns:
            tuple[int,list[int]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 四代控制器不支持该接口
            - list[int]: 返回寄存器数据列表，数据类型：int8
        """
        data_num = int(read_params.num * 2)
        data = (c_int * data_num)()
        tag = rm_read_multiple_input_registers(
            self.handle, read_params, data)
        return tag, list(data)


class InstallPos:
    """
    安装方式及关节、末端软件版本号查询
    @details 睿尔曼机械臂可支持不同形式的安装方式，但是安装方式不同，机器人的动力学模型参数和坐标系的方向也有所差别。
    """

    def rm_set_install_pose(self, x: float, y: float, z: float) -> int:
        """
        设置安装方式参数

        Args:
            x (float): 旋转角，单位 °
            y (float): 俯仰角，单位 °
            z (float): 方位角，单位 °

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_install_pose(self.handle, x, y, z)
        return tag

    def rm_get_install_pose(self) -> dict[str, any]:
        """
        获取安装方式参数

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'x' (float): 旋转角，单位 °
            - 'y' (float): 俯仰角，单位 °
            - 'z' (float): 方位角，单位 °
        """
        x = c_float()
        y = c_float()
        z = c_float()

        ret = rm_get_install_pose(self.handle, byref(x), byref(y), byref(z))

        # 创建一个字典来存储返回值
        result_dict = {
            'return_code': ret,
            'x': x.value,
            'y': y.value,
            'z': z.value,
        }

        return result_dict

    def rm_get_joint_software_version(self) -> tuple[int, dict[str, any]]:
        """
        查询关节软件版本号

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - dict[str,any]: 包含以下键值的字典:
                -'version' (list[int]): （三代控制器）获取到的各关节软件版本号数组，需转换为十六进制，例如获取某关节版本为54536，转换为十六进制为D508，则当前关节的版本号为 Vd5.0.8
                - 'joints_v' (list[str]): （四代控制器）获取到的各关节软件版本号字符串数组
        """
        if self.arm_dof != 0:
            version = (c_int * self.arm_dof)()
            joints_v = (rm_version_t * self.arm_dof)()
        else:
            version = (c_int * ARM_DOF)()
            joints_v = (rm_version_t * ARM_DOF)()

        ret = rm_get_joint_software_version(self.handle, version, joints_v)
        result_dict = {}
        if(self.robot_controller_version == 3):
            result_dict['version'] = [version[i] for i in range(self.arm_dof)]
        else:
            result_dict['joints_v'] = [joints_v[i].version.decode('utf-8') for i in range(self.arm_dof)]
        return ret, result_dict

    def rm_get_tool_software_version(self) -> tuple[int,dict[str,any]]:
        """
        查询末端接口板软件版本号

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - dict[str,any]: 包含以下键值的字典:
                -'version' (int): （三代控制器）获取到的末端接口板软件版本号，需转换为十六进制，例如获取到版本号393，转换为十六进制为189，则当前关节的版本号为 V1.8.9
                - 'tool_v' (str): （四代控制器）获取到的末端接口板软件版本号字符串
        """
        version = c_int()
        tool_v = rm_version_t()

        ret = rm_get_tool_software_version(self.handle, byref(version), byref(tool_v))
        result_dict = {}
        if(self.robot_controller_version == 3):
            result_dict['version'] = version.value
        else:
            result_dict['tool_v'] = tool_v.version.decode('utf-8')

        return ret,result_dict


class ForcePositionControl:
    """透传力位混合控制补偿
    """

    def rm_start_force_position_move(self) -> int:
        """
        开启透传力位混合控制补偿模式

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_start_force_position_move(self.handle)
        return tag

    def rm_stop_force_position_move(self) -> int:
        """
        停止透传力位混合控制补偿模式

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_stop_force_position_move(self.handle)
        return tag

    def rm_force_position_move_joint(self, joint: list[float], sensor: int, mode: int, dir: int, force: float, follow: bool) -> int:
        """
        透传力位混合补偿-角度方式

        Args:
            joint (list[float]): 目标关节角度，单位：°
            sensor (int): 所使用传感器类型，0-一维力，1-六维力
            mode (int): 模式，0-沿基坐标系，1-沿工具端坐标系
            dir (int): 力控方向，0~5分别代表X/Y/Z/Rx/Ry/Rz，其中一维力类型时默认方向为Z方向
            force (float): 力的大小 单位N
            follow (bool): 是否高跟随

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        if self.arm_dof != 0:
            joint = (c_float * self.arm_dof)(*joint)
        else:
            joint = (c_float * ARM_DOF)(*joint)
        tag = rm_force_position_move_joint(
            self.handle, joint, sensor, mode, dir, force, follow)
        return tag

    def rm_force_position_move_pose(self, pose: list[float], sensor: int, mode: int, dir: int, force: float, follow: bool) -> int:
        """
        透传力位混合补偿-位姿方式

        Args:
            pose (list[float]): 当前坐标系下目标位姿列表，支持欧拉角及四元数方式表示姿态，若列表长度为6，则认为使用欧拉角方式表示；列表长度为7则认为使用四元数表示
            sensor (int): 所使用传感器类型，0-一维力，1-六维力
            mode (int): 模式，0-沿基坐标系，1-沿工具端坐标系
            dir (int): 力控方向，0~5分别代表X/Y/Z/Rx/Ry/Rz，其中一维力类型时默认方向为Z方向
            force (float): 力的大小 单位N
            follow (bool): 是否高跟随

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        po1 = rm_pose_t()

        po1.position = rm_position_t(*pose[:3])
        # 四元数
        if len(pose) == 7:
            po1.quaternion = rm_quat_t(*pose[3:])
        # 欧拉角
        elif len(pose) == 6:
            po1.euler = rm_euler_t(*pose[3:])
        else:
            print("Error: pose length is error.")
        tag = rm_force_position_move_pose(
            self.handle, po1, sensor, mode, dir, force, follow)
        return tag

    def rm_force_position_move(self, param:rm_force_position_move_t) -> int:
        """透传力位混合补偿-新参数

        Args:
            param (rm_force_position_move_t): 透传力位混合补偿参数

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """

        tag = rm_force_position_move(self.handle, param)
        return tag

class LiftControl:
    """升降机构控制
    """

    def rm_set_lift_speed(self, speed: int) -> int:
        """
        升降机构速度开环控制

        Args:
            speed (int): 速度百分比，-100~100。
            - speed<0：升降机构向下运动
            - speed>0：升降机构向上运动
            - speed=0：升降机构停止运动

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_lift_speed(self.handle, speed)
        return tag

    def rm_set_lift_height(self, speed: int, height: int, block: int) -> int:
        """
        升降机构位置闭环控制

        Args:
            speed (int): 速度百分比，1~100
            height (int): 目标高度，单位 mm，范围：0~2600
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_lift_height(self.handle, speed, height, block)
        return tag

    def rm_get_lift_state(self) -> tuple[int, dict[str, any]]:
        """
        获取升降机构状态

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组
            -int 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str,any]: 获取到的升降机构状态字典，键为rm_expand_state_t结构体的字段名称
        """
        data = rm_expand_state_t()
        tag = rm_get_lift_state(self.handle, byref(data))
        return tag, data.to_dict()


class ExpandControl:
    """扩展关节控制
    """

    def rm_set_expand_speed(self, speed: int) -> int:
        """
        扩展关节速度环控制

        Args:
            speed (int): 速度百分比，-100~100。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_expand_speed(self.handle, speed)
        return tag

    def rm_set_expand_pos(self, speed: int, height: int, block: int) -> int:
        """
        扩展关节位置环控制

        Args:
            speed (int): 速度百分比，1~100
            height (int): 扩展关节角度，单位度
            block (int): 阻塞设置
                - 多线程模式：
                    - 0：非阻塞模式，发送指令后立即返回。
                    - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
                - 单线程模式：
                    - 0：非阻塞模式。
                    - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_expand_pos(self.handle, speed, height, block)
        return tag

    def rm_get_expand_state(self) -> tuple[int, dict[str, any]]:
        """
        获取扩展关节状态

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组
            - int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
            - dict[str,any]: 获取到的扩展关节状态字典，键为rm_expand_state_t结构体的字段名称
        """
        data = rm_expand_state_t()
        tag = rm_get_expand_state(self.handle, byref(data))
        return tag, data.to_dict()


class ProjectManagement:
    """
    在线编程文件下发、管理
    """

    def rm_send_project(self, send_project: rm_send_project_t) -> tuple[int, int]:
        """
        文件下发。

        Args:
            send_project (rm_send_project_t): 要发送的文件数据。

        Returns:
            Tuple[int, int]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 文件名称校验失败
                    - -5: 文件读取失败
                    - -6: 四代控制器不支持该接口
                -int 若运行失败，该参数返回有问题的工程行数
                    - -1: 无错误，文件成功下发
                    - 0: 校验数据长度不对
                    - 其他值: 有问题的工程行数
        """
        err_line = c_int()
        tag = rm_send_project(self.handle, send_project, byref(err_line))
        return tag, err_line.value if tag != 0 else -1

    def rm_get_program_trajectory_list(self, page_num: int, page_size: int, vague_search: str) -> tuple[int, dict[str, any]]:
        """
        获取在线编程列表

        Args:
            page_num (int): 页码
            page_size (int): 每页大小
            vague_search (str): 模糊搜索

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 获取到的在线编程列表字典，键为rm_program_trajectorys_t结构体的字段名称
        """
        trajectorys = rm_program_trajectorys_t()
        ret = rm_get_program_trajectory_list(
            self.handle, page_num, page_size, vague_search, byref(trajectorys))
        return ret, trajectorys.to_dict()

    def rm_set_program_id_run(self, tra_id: int, speed: int, timeout: int) -> int:
        """
        开始运行指定编号轨迹

        Args:
            tra_id (int): 运行指定的ID，1-100，存在轨迹可运行
            speed (int): 1-100，需要运行轨迹的速度，若设置为0，则按照存储的速度运行
            timeout (int): 阻塞设置
            - 多线程模式：
                - 0：非阻塞模式，发送指令后立即返回。
                - 1：阻塞模式，等待机械臂到达目标位置或规划失败后才返回。
            - 单线程模式：
                - 0：非阻塞模式。
                - 其他值：阻塞模式并设置超时时间，单位为秒。

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 运行状态已停止但未接收到运行成功，是否在外部停止了轨迹。
        """
        tag = rm_set_program_id_run(self.handle, tra_id, speed, timeout)
        return tag

    def rm_get_program_run_state(self) -> tuple[int, dict[str, any]]:
        """
        查询在线编程运行状态

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 获取到的在线编程运行状态字典，键为rm_program_run_state_t结构体的字段名称
        """
        run_state = rm_program_run_state_t()
        ret = rm_get_program_run_state(self.handle, byref(run_state))
        return ret, run_state.to_dict()
    
    def rm_get_flowchart_program_run_state(self) -> tuple[int, dict[str, any]]:
        """
        查询流程图编程运行状态

        Returns:
            tuple[int, dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 四代控制器不支持该接口
                -dict[str,any] 获取到的在线编程运行状态字典，键为rm_program_run_state_t结构体的字段名称
        """
        run_state = rm_flowchart_run_state_t()
        ret = rm_get_flowchart_program_run_state(self.handle, byref(run_state))
        return ret, run_state.to_dict()

    def rm_delete_program_trajectory(self, tra_id: int) -> int:
        """
        删除指定编号轨迹

        Args:
            tra_id (int): 指定轨迹的ID

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_delete_program_trajectory(self.handle, tra_id)
        return tag

    def rm_update_program_trajectory(self, tra_id: int, speed: int, name: str) -> int:
        """
        修改指定编号的轨迹信息

        Args:
            tra_id (int): 指定在线编程轨迹编号
            speed (int): 更新后的规划速度比例 1-100
            name (str): 更新后的文件名称

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_update_program_trajectory(self.handle, tra_id, speed, name)
        return tag

    def rm_set_default_run_program(self, tra_id: int) -> int:
        """
        设置 IO 默认运行编号

        Args:
            tra_id (int): 设置 IO 默认运行的在线编程文件编号，支持 0-100，0 代表取消设置

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_default_run_program(self.handle, tra_id)
        return tag

    def rm_get_default_run_program(self) -> tuple[int, int]:
        """
        获取 IO 默认运行编号

        Returns:
            tuple[int,int]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -int IO 默认运行的在线编程文件编号，支持 0-100，0 代表无默认
        """
        tra_id = c_int()
        tag = rm_get_default_run_program(self.handle, byref(tra_id))
        return tag, tra_id.value


class GlobalWaypointManage:
    """
    全局路点管理
    """

    def rm_add_global_waypoint(self, waypoint: rm_waypoint_t) -> int:
        """
        新增全局路点

        Args:
            waypoint (rm_waypoint_t): 新增全局路点参数（无需输入新增全局路点时间）

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_add_global_waypoint(self.handle, waypoint)
        return tag

    def rm_update_global_waypoint(self, waypoint: rm_waypoint_t) -> int:
        """
        更新全局路点

        Args:
            waypoint (rm_waypoint_t): 更新全局路点参数（无需输入更新全局路点时间）

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_update_global_waypoint(self.handle, waypoint)
        return tag

    def rm_delete_global_waypoint(self, point_name: str) -> int:
        """
        删除全局路点

        Args:
            point_name (str): 全局路点名称

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_delete_global_waypoint(self.handle, point_name)
        return tag

    def rm_get_given_global_waypoint(self, point_name: str) -> tuple[int, dict[str, any]]:
        """
        查询指定全局路点

        Args:
            point_name (str): 指定全局路点名称

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回指定全局路点的参数字典，键为rm_waypoint_t结构体的字段名称
        """
        waypoint = rm_waypoint_t()
        tag = rm_get_given_global_waypoint(
            self.handle, point_name, byref(waypoint))
        return tag, waypoint.to_dict()

    def rm_get_global_waypoints_list(self, page_num: int, page_size: int, vague_search: str) -> tuple[int, dict[str, any]]:
        """
        查询多个全局路点

        Args:
            page_num (int): 页码
            page_size (int): 每页大小
            vague_search (str): 模糊搜索

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回符合条件的全局路点列表字典，键为rm_waypoint_list_t结构体的字段名称
        """
        waypoint_list = rm_waypoint_list_t()
        ret = rm_get_global_waypoints_list(
            self.handle, page_num, page_size, vague_search, byref(waypoint_list))
        return ret, waypoint_list.to_dict()


class ElectronicFenceConfig:
    """
    电子围栏和虚拟墙

    @details I 系列机械臂具备电子围栏与虚拟墙功能，并提供了针对控制器所保存的电子围栏或虚拟墙几何模型参数的操作接口。
    用户可以通过这些接口，实现对电子围栏或虚拟墙的新增、查询、更新和删除操作，在使用中，可以灵活地使用保存在
    控制器中的参数配置，需要注意的是，目前控制器支持保存的参数要求不超过10 个。

    <b> 电子围栏</b>
    电子围栏功能通过精确设置参数，确保机械臂的轨迹规划、示教等运动均在设定的电子围栏范围内进行。当机械臂的运动
    轨迹可能超出电子围栏的界限时，系统会立即返回相应的错误码，并自动中止运动，从而有效保障机械臂的安全运行。
    @attention 电子围栏目前仅支持长方体和点面矢量平面这两种形状，并且其仅在仿真模式下生效，为用户提供一个预演轨迹与进行轨迹优化的安全环境。

    <b> 虚拟墙</b>
    虚拟墙功能支持在电流环拖动示教与力控拖动示教两种模式下，对拖动范围进行精确限制。在这两种特定的示教模式下，用户可以借助虚拟墙功能，确保
    机械臂的拖动操作不会超出预设的范围。
    @attention 虚拟墙功能目前支持长方体和球体两种形状，并仅在上述两种示教模式下有效。在其他操作模式下，此功能将自动失效。因此，请确保在正确的操作模式
    下使用虚拟墙功能，以充分发挥其限制拖动范围的作用。
    """

    def rm_add_electronic_fence_config(self, electronic_fence: rm_fence_config_t) -> int:
        """
        新增几何模型参数

        Args:
            electronic_fence (rm_fence_config_t): 几何模型参数结构体

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_add_electronic_fence_config(self.handle, electronic_fence)
        return tag

    def rm_update_electronic_fence_config(self, electronic_fence: rm_fence_config_t) -> int:
        """
        更新几何模型参数

        Args:
            electronic_fence (rm_fence_config_t): 几何模型参数结构体

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_update_electronic_fence_config(self.handle, electronic_fence)
        return tag

    def rm_delete_electronic_fence_config(self, name: str) -> int:
        """
        删除指定几何模型

        Args:
            name (str): 几何模型名称，不超过 10 个字节，支持字母、数字、下划线

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_delete_electronic_fence_config(self.handle, name)
        return tag

    def rm_get_electronic_fence_list_names(self) -> dict[str, any]:
        """
        查询所有几何模型名称

        Returns:
            dict[str,any]: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'job_names' (list[str]): 字符串列表，表示所有几何模型名称。
            - 'len' (int): 几何模型名称列表长度
        """
        max_len = 10
        names = (rm_fence_names_t * max_len)()
        length = c_int()
        ret = rm_get_electronic_fence_list_names(
            self.handle, names, byref(length))
        job_names = [names[i].name.decode('utf-8')
                     for i in range(length.value)]
        result_dict = {
            'return_code': ret,
            'job_names': job_names,
            'len': length.value,
        }

        return result_dict

    def rm_get_given_electronic_fence_config(self, name: str) -> tuple[int, dict[str, any]]:
        """
        查询指定几何模型参数

        Args:
            name (str): 指定几何模型名称

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回指定几何模型的参数字典，键为rm_fence_config_t结构体的字段名称
        """
        config = rm_fence_config_t()
        ret = rm_get_given_electronic_fence_config(
            self.handle, name, byref(config))
        return ret, config.to_dict()

    def rm_get_electronic_fence_list_infos(self) -> dict[str, any]:
        """
        查询所有几何模型参数

        Returns:
            _type_: 包含以下键值的字典:
            - 'return_code' (int): 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - 'electronic_fence_list' (list[dict]): 几何模型参数列表,。
            - 'len' (int): 几何模型列表长度
        """
        infos = rm_fence_config_list_t()
        length = c_int()
        ret = rm_get_electronic_fence_list_infos(
            self.handle, byref(infos), byref(length))
        result_dict = {
            'return_code': ret,
            'electronic_fence_list': [infos.config[i].to_dict() for i in range(length.value)],
            'len': length.value,
        }

        return result_dict

    def rm_set_electronic_fence_enable(self, electronic_fence_enable: rm_electronic_fence_enable_t) -> int:
        """
        设置电子围栏使能状态

        Args:
            electronic_fence_enable (rm_electronic_fence_enable_t): 电子围栏使能状态

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_electronic_fence_enable(
            self.handle, electronic_fence_enable)
        return tag

    def rm_get_electronic_fence_enable(self) -> tuple[int, dict[str, any]]:
        """
        获取电子围栏使能状态

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回电子围栏使能状态字典，键为rm_electronic_fence_enable_t结构体的字段名称
        """
        enable = rm_electronic_fence_enable_t()
        ret = rm_get_electronic_fence_enable(self.handle, byref(enable))
        return ret, enable.to_dict()

    def rm_set_electronic_fence_config(self, electronic_fence: rm_fence_config_t) -> int:
        """
        设置当前电子围栏参数配置

        Args:
            electronic_fence (rm_fence_config_t): 当前电子围栏参数结构体（无需设置电子围栏名称）

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_electronic_fence_config(self.handle, electronic_fence)
        return tag

    def rm_get_electronic_fence_config(self) -> tuple[int, dict[str, any]]:
        """
        获取当前电子围栏参数

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回当前电子围栏参数字典，键为rm_fence_config_t结构体的字段名称（不返回电子围栏名称）
        """
        config = rm_fence_config_t()
        ret = rm_get_electronic_fence_config(self.handle, byref(config))
        return ret, config.to_dict()

    def rm_set_virtual_wall_enable(self, virtual_wall_enable: rm_electronic_fence_enable_t) -> int:
        """
        设置虚拟墙使能状态

        Args:
            virtual_wall_enable (rm_electronic_fence_enable_t): 虚拟墙状态结构体

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_virtual_wall_enable(self.handle, virtual_wall_enable)
        return tag

    def rm_get_virtual_wall_enable(self) -> tuple[int, dict[str, any]]:
        """
        获取虚拟墙使能状态

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回虚拟墙使能状态字典，键为rm_electronic_fence_enable_t结构体的字段名称
        """
        enable = rm_electronic_fence_enable_t()
        ret = rm_get_virtual_wall_enable(self.handle, byref(enable))
        return ret, enable.to_dict()

    def rm_set_virtual_wall_config(self, virtual_wall: rm_fence_config_t) -> int:
        """
        设置当前虚拟墙参数

        Args:
            virtual_wall (rm_fence_config_t): 当前虚拟墙参数（无需设置虚拟墙名称）

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_virtual_wall_config(self.handle, virtual_wall)
        return tag

    def rm_get_virtual_wall_config(self) -> tuple[int, dict[str, any]]:
        """
        获取当前虚拟墙参数

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回当前虚拟墙参数字典，键为rm_fence_config_t结构体的字段名称（不返回虚拟墙名称）
        """
        config = rm_fence_config_t()
        ret = rm_get_virtual_wall_config(self.handle, byref(config))
        return ret, config.to_dict()


class SelfCollision:
    """
    自碰撞安全检测
    @details 睿尔曼机械臂支持自碰撞安全检测，自碰撞安全检测使能状态下，可确保在轨迹规划、示教等运动过程中机械臂的各个部分不会相互碰撞。
    @attention 以上自碰撞安全检测功能目前只在仿真模式下生效，用于进行预演轨迹与轨迹优化。
    """

    def rm_set_self_collision_enable(self, enable: bool) -> int:
        """
        设置自碰撞安全检测使能状态

        Args:
            enable (bool): true代表使能，false代表禁使能

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_set_self_collision_enable(self.handle, enable)
        return tag

    def rm_get_self_collision_enable(self) -> tuple[int, bool]:
        """
        获取自碰撞安全检测使能状态

        Returns:
            tuple[int,bool]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -bool 返回自碰撞安全检测使能状态，true代表使能，false代表禁使能
        """
        enable = c_bool()
        tag = rm_get_self_collision_enable(self.handle, byref(enable))
        return tag, enable.value
  

class UdpConfig:
    """
    UDP 主动上报配置
    @details 睿尔曼机械臂提供 UDP 机械臂状态主动上报接口，使用时，需要和机械臂处于同一局域网络下，通过设置主动上报配置接口的目标 IP或和机械臂建立 TCP 连接，
    机械臂即会主动周期性上报机械臂状态数据，数据周期可配置，默认 5ms。
    @attention 配置正确并开启三线程模式后，通过注册回调函数可接收并处理主动上报数据。
    """

    def rm_set_realtime_push(self, config: rm_realtime_push_config_t) -> int:
        """
        设置 UDP 机械臂状态主动上报配置

        Args:
            config (rm_realtime_push_config_t): UDP配置结构体

        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        tag = rm_set_realtime_push(self.handle, config)
        return tag

    def rm_get_realtime_push(self) -> tuple[int, dict[str, any]]:
        """
        查询 UDP 机械臂状态主动上报配置

        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                -dict[str,any] 返回 UDP 机械臂状态主动上报配置字典，键为rm_realtime_push_config_t结构体的字段名称
        """
        config = rm_realtime_push_config_t()
        tag = rm_get_realtime_push(self.handle, byref(config))
        return tag, config.to_dict()

    def rm_realtime_arm_state_call_back(self, arm_state_callback:rm_realtime_arm_state_callback_ptr):
        """
        注册UDP机械臂实时状态主动上报信息回调函数，该回调函数接收rm_realtime_arm_joint_state_t类型数据
        作为参数，没有返回值
        当使用三线程，并且UDP机械臂状态主动上报正确配置时，数据会以设定的周期返回

        Args:
            arm_state_callback (rm_realtime_arm_state_callback_ptr): 
                机械臂实时状态信息回调函数

        Notes:
            - 需确保打开三线程模式，仅在三线程模式会打开UDP接口接收数据
            - 需确保广播端口号、上报目标IP、是否主动上报等 UDP 机械臂状态主动上报配置正确
            - 需确保防火墙不会阻止数据的接收
        """
        rm_realtime_arm_state_call_back(arm_state_callback)


class TrajectoryManage:
    """
    轨迹管理
    @details 轨迹管理功能可以对机械臂的拖动示教轨迹进行管理，包括添加、删除、查询等操作。用户可以通过这些接口，实现对机械臂拖动示教轨迹的增删改查操作，
    从而实现对机械臂运动轨迹的管理和控制。
    """
    def rm_get_trajectory_file_list(self, page_num: int, page_size: int, vague_search: str) -> tuple[int, dict[str, any]]:
        """
        查询多个拖动示教轨迹
        Args:
            page_num (int): 页码
            page_size (int): 每页大小
            vague_search (str): 模糊搜索
        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -dict[str,any] 返回符合条件的拖动示教轨迹列表字典，键为rm_trajectory_list_t结构体的字段名称
        """
        trajectory_list = rm_trajectory_list_t()
        ret = rm_get_trajectory_file_list(
            self.handle, page_num, page_size, vague_search, byref(trajectory_list))
        return ret, trajectory_list.to_dict()

    def rm_set_run_trajectory(self, trajectory_name: str) -> int:
        """
        运行指定拖动示教轨迹
        Args:
            trajectory_name (str): 拖动示教轨迹名称
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_set_run_trajectory(self.handle, trajectory_name)
        return tag
    
    def rm_delete_trajectory_file(self, trajectory_name: str) -> int:
        """
        删除指定拖动示教轨迹
        Args:
            trajectory_name (str): 拖动示教轨迹名称
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_delete_trajectory_file(self.handle, trajectory_name)
        return tag

    def rm_save_trajectory_file(self, trajectory_name: str) -> int:
        """
        保存拖动示教轨迹
        Args:
            trajectory_name (str): 拖动示教轨迹名称
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_save_trajectory_file(self.handle, trajectory_name)
        return tag
    

class ModbusV4:
    """四代控制器Modbus接口类
    @details 四代控制器Modbus接口类，可通过该类提供的接口，实现对四代控制器的Modbus功能的控制。
    @attention 仅在四代控制器上可用。
    """
    def rm_add_modbus_tcp_master(self, modbus_tcp_master: rm_modbus_tcp_master_info_t) -> int:
        """
        添加Modbus TCP主站
        Args:
            modbus_tcp_master (rm_modbus_tcp_master_info_t): Modbus TCP主站配置结构体
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_add_modbus_tcp_master(self.handle, modbus_tcp_master)
        return tag
    
    def rm_update_modbus_tcp_master(self, master_name:str, modbus_tcp_master: rm_modbus_tcp_master_info_t) -> int:
        """
        更新Modbus TCP主站
        Args:
            master_name (str): Modbus TCP主站名称
            modbus_tcp_master (rm_modbus_tcp_master_t): 要修改的Modbus TCP主站信息
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_update_modbus_tcp_master(self.handle, master_name, modbus_tcp_master)
        return tag
    
    def rm_delete_modbus_tcp_master(self, master_name:str) -> int:
        """
        删除Modbus TCP主站
        Args:
            master_name (str): Modbus TCP主站名称
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_delete_modbus_tcp_master(self.handle, master_name)
        return tag

    def rm_get_modbus_tcp_master(self, master_name:str) -> tuple[int, dict[str, any]]:
        """
        查询Modbus TCP主站
        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -dict[str,any] 返回指定Modbus TCP主站信息字典，键为rm_modbus_tcp_master_info_t结构体的字段名称
        """
        master_info = rm_modbus_tcp_master_info_t()
        tag = rm_get_modbus_tcp_master(self.handle, master_name, byref(master_info))
        return tag, master_info.to_dict()
    
    def rm_get_modbus_tcp_master_list(self, page_num: int, page_size: int, vague_search: str) -> tuple[int, dict[str, any]]:
        """
        查询多个Modbus TCP主站
        Args:
            page_num (int): 页码
            page_size (int): 每页大小
            vague_search (str): 模糊搜索
        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -dict[str,any] 返回符合条件的Modbus TCP主站列表字典，键为rm_modbus_tcp_master_info_t结构体的字段名称
        """
        master_list = rm_modbus_tcp_master_list_t()
        tag = rm_get_modbus_tcp_master_list(self.handle, page_num, page_size, vague_search, byref(master_list))
        return tag, master_list.to_dict()
    
    def rm_set_controller_rs485_mode(self, mode:int, baudrate:int) -> int:
        """
        设置控制器RS485模式
        Args:
            mode (int): 0代表默认RS485串行通讯，1代表modbus-RTU主站模式，2-代表modbus-RTU从站模式。
            baudrate (int): 波特率(当前支持9600 19200 38400 57600 115200 230400 460800)
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_set_controller_rs485_mode(self.handle, mode, baudrate)
        return tag
    
    def rm_get_controller_rs485_mode_v4(self) -> tuple[int, dict[str, any]]:
        """
        获取控制器RS485模式
        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -dict[str,any]: 包含以下键值的字典:
                    -"mode" (int): 0代表默认RS485串行通讯，1代表modbus-RTU主站模式，2-代表modbus-RTU从站模式。
                    -"baudrate" (int): 波特率(当前支持9600 19200 38400 57600 115200 230400 460800)
        """
        mode = c_int()
        baudrate = c_int()
        tag = rm_get_controller_rs485_mode_v4(self.handle, byref(mode), byref(baudrate))
        return tag, {'mode':mode.value, 'baudrate':baudrate.value}
    
    def rm_set_tool_rs485_mode(self, mode:int, baudrate:int) -> int:
        """
        设置工具端RS485模式(四代控制器支持)
        Args:
            mode (int): 通讯端口，0-设置工具端RS485端口为RTU主站，1-设置工具端RS485端口为灵巧手模式，2-设置工具端RS485端口为夹爪模式。
            baudrate (int): 波特率(当前支持9600,115200,460800)
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_set_tool_rs485_mode(self.handle, mode, baudrate)
        return tag

    def rm_get_tool_rs485_mode_v4(self) -> tuple[int, dict[str, any]]:
        """
        查询工具端RS485模式(四代控制器支持)
        Returns:
            tuple[int,dict[str,any]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -dict[str,any]: 包含以下键值的字典:
                    -"mode" (int): 通讯端口，0-设置工具端RS485端口为RTU主站，1-设置工具端RS485端口为灵巧手模式，2-设置工具端RS485端口为夹爪模式。
                    -"baudrate" (int): 波特率(当前支持9600,115200,460800)
        """
        mode = c_int()
        baudrate = c_int()
        tag = rm_get_tool_rs485_mode_v4(self.handle, byref(mode), byref(baudrate))
        return tag, {'mode':mode.value, 'baudrate':baudrate.value}
    
    def rm_read_modbus_rtu_coils(self, param:rm_modbus_rtu_read_params_t) -> tuple[int, list[int]]:
        """
       Modbus RTU协议读线圈
        Args:
            param (rm_modbus_rtu_read_params_t): Modbus RTU读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读线圈数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_rtu_coils(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]
    
    def rm_write_modbus_rtu_coils(self, param:rm_modbus_rtu_write_params_t) -> int:
        """
        Modbus RTU协议写线圈
        Args:
            param (rm_modbus_rtu_write_params_t): Modbus RTU写入参数结构体
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_write_modbus_rtu_coils(self.handle, param)
        return tag

    def rm_read_modbus_rtu_input_status(self, param:rm_modbus_rtu_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus RTU协议读离散量输入
        Args:
            param (rm_modbus_rtu_read_params_t): Modbus RTU读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读离散量输入数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_rtu_input_status(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]

    def rm_read_modbus_rtu_holding_registers(self, param:rm_modbus_rtu_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus RTU协议读保持寄存器
        Args:
            param (rm_modbus_rtu_read_params_t): Modbus RTU读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读保持寄存器数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_rtu_holding_registers(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]
    
    def rm_write_modbus_rtu_registers(self, param:rm_modbus_rtu_write_params_t) -> int:
        """
        Modbus RTU协议写保持寄存器
        Args:
            param (rm_modbus_rtu_write_params_t): Modbus RTU写入参数结构体
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_write_modbus_rtu_registers(self.handle, param)
        return tag
    
    def rm_read_modbus_rtu_input_registers(self, param:rm_modbus_rtu_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus RTU协议读输入寄存器
        Args:
            param (rm_modbus_rtu_read_params_t): Modbus RTU读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读输入寄存器数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_rtu_input_registers(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)] 
    
    def rm_read_modbus_tcp_coils(self, param:rm_modbus_tcp_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus TCP协议读线圈
        Args:
            param (rm_modbus_tcp_read_params_t): Modbus TCP读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读线圈数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_tcp_coils(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]

    def rm_write_modbus_tcp_coils(self, param:rm_modbus_tcp_write_params_t) -> int:
        """
        Modbus TCP协议写线圈
        Args:
            param (rm_modbus_tcp_write_params_t): Modbus TCP写入参数结构体
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_write_modbus_tcp_coils(self.handle, param)
        return tag
    
    def rm_read_modbus_tcp_input_status(self, param:rm_modbus_tcp_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus TCP协议读离散量输入
        Args:
            param (rm_modbus_tcp_read_params_t): Modbus TCP读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读离散量输入数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_tcp_input_status(self.handle, param, data) 
        return tag, [data[i] for i in range(param.num)]
    
    def rm_read_modbus_tcp_holding_registers(self, param:rm_modbus_tcp_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus TCP协议读保持寄存器
        Args:
            param (rm_modbus_tcp_read_params_t): Modbus TCP读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读保持寄存器数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_tcp_holding_registers(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]

    def rm_write_modbus_tcp_registers(self, param:rm_modbus_tcp_write_params_t) -> int:
        """
        Modbus TCP协议写保持寄存器
        Args:
            param (rm_modbus_tcp_write_params_t): Modbus TCP写入参数结构体
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                - -4: 三代控制器不支持该接口
        """
        tag = rm_write_modbus_tcp_registers(self.handle, param)
        return tag

    def rm_read_modbus_tcp_input_registers(self, param:rm_modbus_tcp_read_params_t) -> tuple[int, list[int]]:
        """
        Modbus TCP协议读输入寄存器
        Args:
            param (rm_modbus_tcp_read_params_t): Modbus TCP读取参数结构体
        Returns:
            tuple[int,list[int]]: 包含两个元素的元组。
                -int 函数执行的状态码。
                    - 0: 成功。
                    - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                    - -1: 数据发送失败，通信过程中出现问题。
                    - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                    - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
                    - -4: 三代控制器不支持该接口
                -list[int] 返回读输入寄存器数据，数组大小为param.num
        """
        data = (c_int * param.num)()
        tag = rm_read_modbus_tcp_input_registers(self.handle, param, data)
        return tag, [data[i] for i in range(param.num)]
    

   
class Algo:
    """
    算法接口
    @details 针对睿尔曼机械臂，提供正逆解、各种位姿参数转换等工具接口。既可通过RoboticArm类连接机械臂使用该类中的成员函数，也可单独使用该类
    """

    def __init__(self, arm_model: rm_robot_arm_model_e, force_type: rm_force_type_e):
        """初始化算法依赖

        Args:
            arm_model (rm_robot_arm_model_e): 机械臂型号
            force_type (rm_force_type_e): 传感器类型
        """
        self.handle = rm_robot_handle()
        rm_algo_init_sys_data(arm_model, force_type)

        if arm_model == 1 or arm_model == 7:
            self.arm_dof = 7
        else:
            self.arm_dof = 6

    def rm_algo_version(self) -> str:
        """获取算法库版本

        Returns:
            str: 算法库版本号
        """
        return rm_algo_version()

    def rm_algo_set_angle(self, x: float, y: float, z: float) -> None:
        """设置安装角度

        Args:
            x (float): X轴安装角度 单位°
            y (float): Y轴安装角度 单位°
            z (float): z轴安装角度 单位°
        """
        rm_algo_set_angle(x, y, z)

    def rm_algo_get_angle(self) -> tuple[float, float, float]:
        """获取安装角度

        Returns:
            tuple[float,float,float]: 包含三个浮点数的元组，分别代表x、y和z轴的安装角度，单位：°
        """
        x = c_float()
        y = c_float()
        z = c_float()
        rm_algo_get_angle(x, y, z)

        return x.value, y.value, z.value

    def rm_algo_set_redundant_parameter_traversal_mode(self, mode: int) -> None:
        """
        设置逆解求解模式

        Args:
            mode (bool): 
                - true：遍历模式，冗余参数遍历的求解策略。适于当前位姿跟要求解的位姿差别特别大的应用场景，如MOVJ_P、位姿编辑等，耗时较长
                - false：单步模式，自动调整冗余参数的求解策略。适于当前位姿跟要求解的位姿差别特别小、连续周期控制的场景，如笛卡尔空间规划的位姿求解等，耗时短

        """
        rm_algo_set_redundant_parameter_traversal_mode(mode)

    def rm_algo_set_workframe(self, frame: rm_frame_t) -> None:
        """
        设置工作坐标系

        Args:
            frame (rm_frame_t): 坐标系数据
        """
        rm_algo_set_workframe(frame)

    def rm_algo_get_curr_workframe(self) -> dict[str, any]:
        """
        获取当前工作坐标系

        Returns:
            dict[str, any]: 返回当前工作坐标系字典，键为rm_frame_t结构体的字段名称
        """
        frame = rm_frame_t()
        rm_algo_get_curr_workframe(byref(frame))
        return frame.to_dictionary()

    def rm_algo_set_toolframe(self, frame: rm_frame_t) -> None:
        """
        设置工具坐标系

        Args:
            frame (rm_frame_t): 坐标系数据
        """

        rm_algo_set_toolframe(frame)

    def rm_algo_get_curr_toolframe(self) -> dict[str, any]:
        """
        获取算法当前工具坐标系

        Returns:
            dict[str, any]: 返回当前工具坐标系字典，键为rm_frame_t结构体的字段名称
        """
        frame = rm_frame_t()
        rm_algo_get_curr_toolframe(byref(frame))
        return frame.to_dictionary()

    def rm_algo_set_joint_max_limit(self, joint_limit: list[float]) -> None:
        """
        设置算法关节最大限位

        Args:
            joint_limit (list[float]): 关节最大限位数组，单位：°
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)(*joint_limit)
        else:
            joint_positions = (c_float * ARM_DOF)(*joint_limit)
        rm_algo_set_joint_max_limit(joint_positions)

    def rm_algo_get_joint_max_limit(self) -> list[float]:
        """
        获取算法关节最大限位

        Returns:
            list[float]: 关节最大限位数组，单位：°
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)()
        else:
            joint_positions = (c_float * ARM_DOF)()
        rm_algo_get_joint_max_limit(joint_positions)
        return list(joint_positions)

    def rm_algo_set_joint_min_limit(self, joint_limit: list[float]) -> None:
        """
        设置算法关节最小限位

        Args:
            joint_limit (list[float]): 关节最小限位数组，单位：°
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)(*joint_limit)
        else:
            joint_positions = (c_float * ARM_DOF)(*joint_limit)
        rm_algo_set_joint_min_limit(joint_positions)

    def rm_algo_get_joint_min_limit(self) -> list[float]:
        """
        获取算法关节最小限位

        Returns:
            list[float]: 关节最小限位数组，单位：°
        """
        if self.arm_dof != 0:
            joint_positions = (c_float * self.arm_dof)()
        else:
            joint_positions = (c_float * ARM_DOF)()
        rm_algo_get_joint_min_limit(joint_positions)
        return list(joint_positions)

    def rm_algo_set_joint_max_speed(self, joint_limit: list[float]) -> None:
        """
        设置算法关节最大速度

        Args:
            joint_limit (list[float]): 关节最大速度，单位：RPM
        """
        if self.arm_dof != 0:
            speed = (c_float * self.arm_dof)(*joint_limit)
        else:
            speed = (c_float * ARM_DOF)(*joint_limit)
        rm_algo_set_joint_max_speed(speed)

    def rm_algo_get_joint_max_speed(self) -> list[float]:
        """
        获取算法关节最大速度

        Returns:
            list[float]: 关节最大速度，单位：RPM
        """
        if self.arm_dof != 0:
            speed = (c_float * self.arm_dof)()
        else:
            speed = (c_float * ARM_DOF)()
        rm_algo_get_joint_max_speed(speed)
        return list(speed)

    def rm_algo_set_joint_max_acc(self, joint_limit: list[float]) -> None:
        """
        设置算法关节最大加速度

        Args:
            joint_limit (list[float]): 关节最大加速度，单位：RPM/s
        """
        if self.arm_dof != 0:
            acc = (c_float * self.arm_dof)(*joint_limit)
        else:
            acc = (c_float * ARM_DOF)(*joint_limit)
        rm_algo_set_joint_max_acc(acc)

    def rm_algo_get_joint_max_acc(self) -> list[float]:
        """
        获取算法关节最大加速度

        Returns:
            list[float]: 关节最大加速度，单位：RPM/s
        """
        if self.arm_dof != 0:
            acc = (c_float * self.arm_dof)()
        else:
            acc = (c_float * ARM_DOF)()
        rm_algo_get_joint_max_acc(acc)
        return list(acc)

    def rm_algo_inverse_kinematics(self, params: rm_inverse_kinematics_params_t) -> tuple[int, list[float]]:
        """
        逆解函数

        Args:
            params (rm_inverse_kinematics_params_t): 逆解输入参数结构体

        Returns:
            tuple[int,list[float]]: 包含两个元素的元组。
                -int 逆解结果
                    - 0: 逆解成功
                    - 1: 逆解失败
                    - -1: 上一时刻关节角度输入为空
                    - -2: 目标位姿四元数不合法
                -list[float] 输出的关节角度 单位°，长度为机械臂自由度
        """
        q_out = (c_float * ARM_DOF)()

        ret = rm_algo_inverse_kinematics(self.handle, params, q_out)
        out = list(q_out)
        return ret, out[:self.arm_dof]

    def rm_algo_inverse_kinematics_all(self, params:rm_inverse_kinematics_params_t) -> rm_inverse_kinematics_all_solve_t:
        """
        计算逆运动学全解(当前仅支持六自由度机器人)
        Args:
            params(rm_inverse_kinematics_params_t) 逆解输入参数结构体
        Returns:
            rm_inverse_kinematics_all_solve_t 逆解的全解结构体
        """
        ret = rm_inverse_kinematics_all_solve_t()
        ret = rm_algo_inverse_kinematics_all(self.handle, params)
        return ret


    def rm_algo_ikine_select_ik_solve(self, weight:list[float], params:rm_inverse_kinematics_all_solve_t) -> int:
        """
        从多解中选取最优解(当前仅支持六自由度机器人)
        Args:
            weight(list[float]) 权重,建议默认值为{1,1,1,1,1,1}
            params(rm_inverse_kinematics_all_solve_t) 待选解的全解结构体
        Returns:
            int 最优解索引，选解结果为ik_solve.q_solve[i] -1：当前机器人非六自由度，当前仅支持六自由度机器人
        """
        weight_c = (c_float * 6)(*weight)
        ret = rm_algo_ikine_select_ik_solve(weight_c, params)
        return ret


    def rm_algo_ikine_check_joint_position_limit(self, q_solve_i:list[float]) -> int:
        """
        检查逆解结果是否超出关节限位(当前仅支持六自由度机器人)
        Args:
            q_solve_i (list[float]) 一组解，即一组关节角度，单位:°
        Returns:
            0:表示未超限 i:表示关节i超限，优先报序号小的关节 -1：当前机器人非六自由度，当前仅支持六自由度机器人
        """
        ret = rm_algo_ikine_check_joint_position_limit(q_solve_i)
        return ret


    def rm_algo_ikine_check_joint_velocity_limit(self, dt:float, q_ref:list[float], q_solve_i:list[float]) -> int:
        """
        检查逆解结果是否超出速度限位(当前仅支持六自由度机器人)
        Args:
            dt 两帧数据之间的时间间隔，即控制周期，单位sec
            q_ref(list[float]) 参考关节角度或者第一帧数据角度，单位：°
            q_solve_i (list[float]) 一组解，即一组关节角度，单位:°
        Returns:
            int 0:表示未超限 i:表示关节i超限，优先报序号小的关节 -1：当前机器人非六自由度，当前仅支持六自由度机器人
        """
        q_ref_c = (c_float * 8)(*q_ref)
        q_solve_c = (c_float * 8)(*q_solve_i)
        
        ret = rm_algo_ikine_check_joint_velocity_limit(dt, q_ref_c, q_solve_c)
        return ret
    
    def rm_algo_calculate_arm_angle_from_config_rm75(self,q_ref:list[float]) -> tuple[int, float]:
        """
        根据参考位形计算臂角大小（仅支持RM75）
        Args:
            q_ref(list[float]),当前参考位形的关节角度，单位°
        Returns:
            int: - 0: 求解成功 - -1: 求解失败，或机型非RM75  - -2: q_ref 输入参数非法
            float: 计算结果，当前参考位形对应的臂角大小，单位°
        """
        q_ref_c = (c_float * ARM_DOF)(*q_ref)
        arm_angle = c_float()
        ret = rm_algo_calculate_arm_angle_from_config_rm75(q_ref_c, byref(arm_angle))
        return ret,arm_angle.value

    def rm_algo_inverse_kinematics_rm75_for_arm_angle(self,params:rm_inverse_kinematics_params_t,arm_angle:float) -> tuple[int,list[float]]:
        """
        臂角法求解RM75逆运动学
        Args:
            params:rm_inverse_kinematics_params_t,逆解参数结构体
            arm_angle:float,指定轴角大小,单位:°
        Returns:
            int 0: 求解成功
               -1: 求解失败
               -2: 求解结果超出限位
               -3: 机型非RM75
            list[float]: q_solve，求解结果,单位:°
        """
        q_solve = (c_float * ARM_DOF)()
        ret = rm_algo_inverse_kinematics_rm75_for_arm_angle(params,arm_angle,q_solve)
        out = list(q_solve)
        return ret, out[:self.arm_dof]


    def rm_algo_forward_kinematics(self, joint: list[float], flag: int = 1) -> list[float]:
        """
        正解算法接口

        Args:
            joint (list[float]): 关节角度，单位：°
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 解得目标位姿列表
        """
        if self.arm_dof != 0:
            joint = (c_float * self.arm_dof)(*joint)
        else:
            joint = (c_float * ARM_DOF)(*joint)
        pose = rm_algo_forward_kinematics(self.handle, joint)
        position = pose.position
        euler = pose.euler
        qua = pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # 保留三位小数
        # return [round(value, 3) for value in pose_eul] if flag else [round(value, 3) for value in pose_qua]

    def rm_algo_euler2quaternion(self, eul: list[float]) -> list[float]:
        """
        欧拉角转四元数

        Args:
            eul (list[float]): 欧拉角列表[rx.ry,rz]，单位：rad

        Returns:
            list[float]: 四元数列表[w,x,y,z]
        """
        eul = rm_euler_t(*eul)
        quat = rm_algo_euler2quaternion(eul)
        return [quat.w, quat.x, quat.y, quat.z]

    def rm_algo_quaternion2euler(self, quat: list[float]) -> list[float]:
        """
        四元数转欧拉角

        Args:
            quat (list[float]): 四元数列表[w,x,y,z]

        Returns:
            list[float]: 欧拉角列表[rx.ry,rz]，单位：rad
        """
        quat = rm_quat_t(*quat)
        eul = rm_algo_quaternion2euler(quat)
        return [eul.rx, eul.ry, eul.rz]

    def rm_algo_euler2matrix(self, eu: list[float]) -> rm_matrix_t:
        """
        欧拉角转旋转矩阵

        Args:
            eu (list[float]): 欧拉角列表[rx.ry,rz]，单位：rad

        Returns:
            rm_matrix_t: 旋转矩阵
        """
        eu = rm_euler_t(*eu)
        matrix = rm_algo_euler2matrix(eu)
        return matrix

    def rm_algo_pos2matrix(self, pose: list[float]) -> rm_matrix_t:
        """
        位姿转旋转矩阵

        Args:
            pose (list[float]): 位置姿态列表[x,y,z,rx,ry,rz]

        Returns:
            rm_matrix_t: 旋转矩阵
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*pose[:3])
        po1.euler = rm_euler_t(*pose[3:])
        matrix = rm_algo_pos2matrix(po1)
        return matrix

    def rm_algo_matrix2pos(self, matrix: rm_matrix_t, flag: int = 1) -> list[float]:
        """
        旋转矩阵转位姿

        Args:
            matrix (rm_matrix_t): 旋转矩阵
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 解得目标位姿
        """
        pose = rm_algo_matrix2pos(matrix)
        position = pose.position
        euler = pose.euler
        qua = pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return pose.to_dict()

    def rm_algo_base2workframe(self, matrix: rm_matrix_t, pose_in_base: rm_pose_t, flag: int = 1) -> list[float]:
        """
        基坐标系转工作坐标系

        Args:
            matrix (rm_matrix_t): 工作坐标系在基坐标系下的矩阵
            pose_in_base (rm_pose_t): 工具端坐标在基坐标系下位姿
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 基坐标系在工作坐标系下的位姿
        """
        pose_in_work = rm_algo_matrix2pos(matrix, pose_in_base)
        position = pose_in_work.position
        euler = pose_in_work.euler
        qua = pose_in_work.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return pose_in_work.to_dict()

    def rm_algo_workframe2base(self, matrix: rm_matrix_t, pose_in_work: rm_pose_t, flag: int = 1) -> list[float]:
        """
        工作坐标系转基坐标系

        Args:
            matrix (rm_matrix_t): 工具端坐标在工作坐标系下矩阵
            pose_in_work (rm_pose_t): 工具端坐标在工作坐标系下位姿
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 工作坐标系在基坐标系下的位姿
        """
        pose_in_base = rm_algo_workframe2base(matrix, pose_in_work)
        position = pose_in_base.position
        euler = pose_in_base.euler
        qua = pose_in_base.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return pose_in_base.to_dict()

    def rm_algo_end2tool(self, eu_end: rm_pose_t, flag: int = 1) -> list[float]:
        """
        末端位姿转成工具位姿

        Args:
            eu_end (rm_pose_t): 基于世界坐标系和默认工具坐标系的末端位姿
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 基于工作坐标系和工具坐标系的末端位姿
        """
        end_pose = rm_algo_end2tool(self.handle, eu_end)
        position = end_pose.position
        euler = end_pose.euler
        qua = end_pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return end_pose.to_dict()

    def rm_algo_tool2end(self, eu_tool: rm_pose_t, flag: int = 1) -> list[float]:
        """
        工具位姿转末端位姿

        Args:
            eu_tool (rm_pose_t): 基于工作坐标系和工具坐标系的末端位姿
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 基于世界坐标系和默认工具坐标系的末端位姿
        """
        end_pose = rm_algo_tool2end(self.handle, eu_tool)
        position = end_pose.position
        euler = end_pose.euler
        qua = end_pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return end_pose.to_dict()

    def rm_algo_rotate_move(self, curr_joint: list[float], rotate_axis: int, rotate_angle: float, choose_axis: rm_pose_t, flag: int = 1) -> list[float]:
        """
        计算环绕运动位姿

        Args:
            curr_joint (list[float]): 当前关节角度 单位°
            rotate_axis (int): 旋转轴: 1:x轴, 2:y轴, 3:z轴
            rotate_angle (float): 旋转角度: 旋转角度, 单位(度)
            choose_axis (rm_pose_t): 指定计算时使用的坐标系
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 目标位姿
        """
        if self.arm_dof != 0:
            curr_joint = (c_float * self.arm_dof)(*curr_joint)
        else:
            curr_joint = (c_float * ARM_DOF)(*curr_joint)
        pose = rm_algo_rotate_move(
            self.handle, curr_joint, rotate_axis, rotate_angle, choose_axis)
        position = pose.position
        euler = pose.euler
        qua = pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return pose.to_dict()

    def rm_algo_cartesian_tool(self, curr_joint: list[float], move_lengthx: float, move_lengthy: float, move_lengthz: float, flag: int = 1) -> list[float]:
        """
        计算沿工具坐标系运动位姿

        Args:
            curr_joint (list[float]): 当前关节角度，单位：度
            move_lengthx (float): 沿X轴移动长度，单位：米
            move_lengthy (float): 沿Y轴移动长度，单位：米
            move_lengthz (float): 沿Z轴移动长度，单位：米
            flag (int, optional): 选择姿态表示方式，默认欧拉角表示姿态
                - 0: 返回使用四元数表示姿态的位姿列表[x,y,z,w,x,y,z]
                - 1: 返回使用欧拉角表示姿态的位姿列表[x,y,z,rx,ry,rz]

        Returns:
            list[float]: 目标位姿
        """
        if self.arm_dof != 0:
            curr_joint = (c_float * self.arm_dof)(*curr_joint)
        else:
            curr_joint = (c_float * ARM_DOF)(*curr_joint)
        pose = rm_algo_cartesian_tool(
            self.handle, curr_joint, move_lengthx, move_lengthy, move_lengthz)
        position = pose.position
        euler = pose.euler
        qua = pose.quaternion
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        pose_qua = [position.x, position.y,
                    position.z, qua.w, qua.x, qua.y, qua.z]
        return pose_eul if flag else pose_qua
        # return pose.to_dict()

    def rm_algo_pose_move(self, poseCurrent: list[float], deltaPosAndRot: list[float], frameMode: int) -> list[float]:
        """
        计算Pos和Rot沿某坐标系有一定的位移和旋转角度后，所得到的位姿数据

        Args:
            poseCurrent (list[float]): 当前时刻位姿（欧拉角形式）
            deltaPosAndRot (list[float]): 移动及旋转数组，位置移动（单位：m），旋转（单位：度）
            frameMode (int): 坐标系模式选择 0:Work（work即可任意设置坐标系），1:Tool

        Returns:
            list[float]: 平移旋转后的位姿
        """
        po1 = rm_pose_t()
        po1.position = rm_position_t(*poseCurrent[:3])
        po1.euler = rm_euler_t(*poseCurrent[3:])

        deltaPosAndRot = (c_float * 6)(*deltaPosAndRot)

        pose = rm_algo_pose_move(
            self.handle, po1, deltaPosAndRot, frameMode)
        
        position = pose.position
        euler = pose.euler
        pose_eul = [position.x, position.y,
                    position.z, euler.rx, euler.ry, euler.rz]
        return pose_eul

    def rm_algo_set_dh(self, dh: rm_dh_t) -> None:
        """
        设置DH参数
        Args:
            dh (rm_dh_t): DH参数列表
        """
        rm_algo_set_dh(dh)

    def rm_algo_get_dh(self) -> rm_dh_t:
        """
        获取DH参数
        Returns:
            list[float]: DH参数列表
        """
        dh = rm_algo_get_dh()
        return dh.to_dict()

    def rm_algo_universal_singularity_analyse(self, q:list[float], singluar_value_limit:float) -> int:
        """
        通过分析雅可比矩阵最小奇异值, 判断机器人是否处于奇异状态
        Args:
            -q 要判断的关节角度（机械零位描述），单位：°
            -singluar_value_limit 最小奇异值阈值，若传NULL，则使用内部默认值，默认值为0.01（该值在0-1之间）
        Returns:
            int 
             0:在当前阈值条件下正常
             -1:表示在当前阈值条件下判断为奇异区
             -2:表示计算失败
        """
        q_c = (c_float * 7)(*q)
        # singluar_value_limit_c = (c_float * 6)(*singluar_value_limit)
        ret = rm_algo_universal_singularity_analyse(q_c, singluar_value_limit)
        return ret

    def rm_algo_kin_singularity_thresholds_init(self)-> None:
        """
        恢复初始阈值(仅适用于解析法分析机器人奇异状态),阈值初始化为：limit_qe=10deg,limit_qw=10deg,limit_d = 0.05m 
        """
        rm_algo_kin_singularity_thresholds_init()        

    def rm_algo_kin_set_singularity_thresholds(self,limit_qe:float,limit_qw:float, limit_d:float)-> None:
        """
        设置自定义阈值(仅适用于解析法分析机器人奇异状态)
        Args:
            limit_qe  肘部奇异区域范围设置(即J3接近0的范围,若为RML63，则是J3接近-9.68的范围),单位: °,default: 10°
            limit_qw  腕部奇异区域范围设置(即J5接近0的范围),单位: °,default: 10°
            limit_d 肩部奇异区域范围设置(即腕部中心点距离奇异平面的距离), 单位: m, default: 0.05
        Returns:
            None
        """
        rm_algo_kin_set_singularity_thresholds(limit_qe,limit_qw,limit_d)



    def rm_algo_kin_get_singularity_thresholds(self)-> tuple[float,float,float]:
        """
        获取自定义阈值(仅适用于解析法分析机器人奇异状态)
        Args:
            None
        Returns:
            limit_qe  肘部奇异区域范围设置(即J3接近0的范围,若为RML63，则是J3接近-9.68的范围),单位: °,default: 10°
            limit_qw  腕部奇异区域范围设置(即J5接近0的范围),单位: °,default: 10°
            limit_d 肩部奇异区域范围设置(即腕部中心点距离奇异平面的距离), 单位: m, default: 0.05
        """
        limit_qe = c_float()
        limit_qw = c_float()
        limit_d = c_float()
        rm_algo_kin_get_singularity_thresholds(byref(limit_qe),byref(limit_qw),byref(limit_d))
        return limit_qe.value,limit_qw.value,limit_d.value



    def rm_algo_kin_robot_singularity_analyse(self,q:list[float]) -> tuple[int,float]:
        """
        解析法判断机器人是否处于奇异位形（仅支持六自由度）
        Args:
            q:list[float] 要判断的关节角度,单位°
        Returns:
            tuple[int,float]: 包含两个元素的元组。
            - int: 0:正常 -1:肩部奇异 -2:肘部奇异 -3:腕部奇异
            - float: 返回腕部中心点到肩部奇异平面的距离，该值越接近0说明越接近肩部奇异,单位m
        """      
        q_c = (c_float * 6)(*q)
        distance_c = c_float()
        ret = rm_algo_kin_robot_singularity_analyse(q_c, byref(distance_c))
        return ret, distance_c.value

  
    def rm_algo_set_tool_envelope(self, toolSphere_i:int, data:rm_tool_sphere_t) -> None:
        """
        设置工具包络球参数
        Args:
            toolSphere_i 工具包络球编号 (0~4)
            data 工具包络球参数,注意其参数在末端法兰坐标系下描述
        """
        rm_algo_set_tool_envelope(toolSphere_i, data)


    def rm_algo_get_tool_envelope(self, toolSphere_i:int) -> rm_tool_sphere_t:
        """
        获取工具包络球参数
        Args:
            toolSphere_i 工具rm_get_tool_voltage包络球编号 (0~4)
        Returns:
            (rm_tool_sphere_t) 工具包络球参数,注意其参数在末端法兰坐标系下描述
        """
        tool_sphere_type = rm_tool_sphere_t()
        rm_algo_get_tool_envelope(toolSphere_i, byref(tool_sphere_type))
        return tool_sphere_type
        

    def rm_algo_safety_robot_self_collision_detection(self,joint_deg:list[float]) -> int:
        """
        自碰撞检测
        Args:
            joint_deg(list[float]) 要判断的关节角度，单位°
        Returns:
            int 
             -0: 无碰撞
             1: 发生碰撞,超出关节限位将被认为发生碰撞
        """
        joint_deg_c = (c_float * 7)(*joint_deg)
        ret = rm_algo_safety_robot_self_collision_detection(joint_deg_c)
        return ret

 

class RoboticArm(ArmState, MovePlan, JointConfigSettings, JointConfigReader, ArmTipVelocityParameters,
                 ToolCoordinateConfig, WorkCoordinateConfig, ArmTeachMove, ArmMotionControl, ControllerConfig,
                 CommunicationConfig, ControllerIOConfig, EffectorIOConfig, GripperControl, Force, DragTeach, HandControl, ModbusConfig, InstallPos,
                 ForcePositionControl, ProjectManagement, GlobalWaypointManage, ElectronicFenceConfig, SelfCollision,
                 UdpConfig, Algo, LiftControl, ExpandControl, TrajectoryManage, ModbusV4):
    """机械臂连接、断开、日志设置等操作
    """

    def __init__(self, mode: rm_thread_mode_e = None):
        """初始化线程模式

        Args:
            mode (rm_thread_mode_e): 
                    RM_SINGLE_MODE_E：单线程模式，单线程非阻塞等待数据返回；  
                    RM_DUAL_MODE_E：双线程模式，增加接收线程监测队列中的数据；  
                    RM_TRIPLE_MODE_E：三线程模式，在双线程模式基础上增加线程监测UDP接口数据；
        """
        if mode == None:
            return
        rm_init(mode)
        print("current c api version: ", rm_api_version())

    def rm_create_robot_arm(self, ip: str, port: int, level: int = 3, log_func: CFUNCTYPE = None) -> rm_robot_handle:
        """
        初始化RoboticArm类，创建机械臂连接控制句柄。

        Args:
            ip (str): 机械臂的IP地址。
            port (int): 机械臂的端口号。
            level (int, optional): 日志打印等级，默认为3。
                - 0: debug模式
                - 1: info模式
                - 2: warning模式
                - 3: error模式
            log_func (CFUNCTYPE, optional): 自定义日志打印函数（当前Python版本API暂不支持）。默认为None。

        Returns:
            rm_robot_handle: 机械臂句柄，其中包含机械臂id标识。
        """
        if log_func is None:
            rm_set_log_call_back(0, level)
        else:
            LOGCALLBACK = CFUNCTYPE(UNCHECKED(None), String, c_void_p)
            log_func = LOGCALLBACK(log_func)
            rm_set_log_call_back(log_func, level)

        # rm_init(thread_mode)
        self.handle = rm_create_robot_arm(ip, port)
        if self.handle.contents.id == -1:
            self.arm_dof = 0
            self.robot_controller_version = 4
        else:
            info = rm_robot_info_t()
            if rm_get_robot_info(self.handle, info) == 0:
                self.arm_dof = info.arm_dof
                self.robot_controller_version = info.robot_controller_version

        return self.handle.contents

    def rm_delete_robot_arm(self) -> int:
        """
        根据句柄删除机械臂

        Returns:
            int: 0 表示成功，非0 表示失败
        """
        return rm_delete_robot_arm(self.handle)

    @classmethod  
    def rm_destory(cls) -> int:
        """关闭所有机械臂连接，销毁所有线程
        Returns:
            int: 0 表示成功，非0 表示失败

        """
        return rm_destory()

    def rm_set_log_save(self, path) -> None:
        """保存日志到文件

        Args:
            path (string): 日志保存文件路径
        """
        rm_set_log_save(path)

    def rm_set_timeout(self,timeout: int) -> None:
        """
        设置全局超时时间
        Args:
            timeout(int):接收控制器返回指令超时时间，多数接口默认超时时间为500ms，单位ms
        """
        rm_set_timeout(timeout)

    def rm_set_arm_run_mode(self, mode: int) -> int:
        """设置真实/仿真模式

        Args:
            mode (int): 模式 0:仿真 1:真实

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
        """
        return rm_set_arm_run_mode(self.handle, mode)

    def rm_get_arm_run_mode(self) -> tuple[int, int]:
        """获取真实/仿真模式

        Returns:
            tuple[int, int]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - int: 模式 0:仿真 1:真实
        """
        mode = c_int()
        ret = rm_get_arm_run_mode(self.handle, byref(mode))
        return ret, mode.value

    def rm_set_arm_emergency_stop(self, state:bool) -> int:
        """设置机械臂急停状态
        Args:
            state (bool): 急停状态，true：急停，false：恢复

        Returns:
            int: 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 三代控制器不支持该接口。
        """
        return rm_set_arm_emergency_stop(self.handle, state)

    def rm_get_robot_info(self) -> tuple[int, dict[str, any]]:
        """获取机械臂基本信息
        Returns:
            tuple[int, dict[str, any]]: 包含两个元素的元组。
            - int: 函数执行的状态码。
                - 0: 成功。
                - -1: 未找到对应句柄,句柄为空或已被删除。
                - -2: 获取到的机械臂基本信息非法，检查句柄是否已被删除。
            - dict[str, any]: 返回机械臂基本信息字典，键为rm_robot_info_t结构体的字段名称。
        """
        info = rm_robot_info_t()
        ret = rm_get_robot_info(self.handle, info)
        return ret, info.to_dictionary() #返回字典，也可直接返回info

    def rm_get_arm_event_call_back(self, event_callback: rm_event_callback_ptr):
        """注册机械臂事件回调函数
        当机械臂返回运动到位指令或者文件运行结束指令时会有数据返回

        Args:
            event_callback (rm_event_callback_ptr): 机械臂事件回调函数，该回调函数接收rm_event_push_data_t类型的数据作为参数，没有返回值

        Notes:
            单线程无法使用该回调函数
        """
        rm_get_arm_event_call_back(event_callback)
