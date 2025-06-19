
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
        电流环开放控制
        Args:
            current (list[float]): 电流透传到CANFD，其中关节1和关节2的单位是2mA，其余关节的单位是1mA，精度：0.001mA
        Returns:
            int: 函数执行的状态码。
                - 0: 成功。
                - 1: 控制器返回false，参数错误或机械臂状态发生错误。
                - -1: 数据发送失败，通信过程中出现问题。
                - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
                - -3: 返回值解析失败，控制器返回的数据无法识别或不完整等情况。
        """
        tag = rm_current_canfd(self.handle, current)
        return tag