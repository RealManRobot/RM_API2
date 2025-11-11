#ifndef MYCLASS_INTERNAL_H
#define MYCLASS_INTERNAL_H

#ifdef __cplusplus  
extern "C" {
#endif  
  
#include "rm_service.h"  
#include "rm_interface_internal.h"  

#ifdef __cplusplus  
}  

class RM_Internal : public RM_Service {  
public:

/**
 * @brief 设置电流环控制功能使能状态
 * 
 * @param handle 机械臂控制句柄 
 * @param enable 设置电流环是否使能，true为使能，false为禁使能
 * @return int 函数执行的状态码。  
            - 0: 成功。  
            - 1: 控制器返回false，传递参数错误或机械臂状态发生错误。  
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。  
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
 */
RM_INTERFACE_EXPORT int rm_set_current_canfd_enable(rm_robot_handle *handle, bool enable);

/**
 * @brief 获取电流环控制功能使能状态
 *
 * @param handle 机械臂控制句柄
 * @param enable 获取电流环是否使能，true为使能，false为禁使能
 * @return int 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，传递参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
 */
RM_INTERFACE_EXPORT int rm_get_current_canfd_enable(rm_robot_handle *handle, bool *enable);

/**
 * @brief 电流环开放控制
 *
 * @param handle 机械臂控制句柄
 * @param current 电流透传到CANFD，其中关节1和关节2的单位是2mA，其余关节的单位是1mA，精度：0.001mA
 * @return int 函数执行的状态码。
            - 0: 成功。
            - 1: 控制器返回false，传递参数错误或机械臂状态发生错误。
            - -1: 数据发送失败，通信过程中出现问题。
            - -2: 数据接收失败，通信过程中出现问题或者控制器超时没有返回。
            - -3: 返回值解析失败，接收到的数据格式不正确或不完整。
            - -4: 电流环控制功能使能状态未打开。
 */
RM_INTERFACE_EXPORT int rm_current_canfd(rm_robot_handle *handle, float *current);

};
#endif


#endif  // MYCLASS_INTERNAL_H