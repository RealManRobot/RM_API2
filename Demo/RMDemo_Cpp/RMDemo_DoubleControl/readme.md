## **1. 项目介绍**
本项目使用睿尔曼C++开发包完成多机械臂连接、机械臂版本获取、API版本获取、movej运动、moveL运动、关闭连接。

## **2. 代码结构**
```
RMDemo_DoubleControl
├── build/                  # CMake构建生成的输出目录（如Makefile、构建文件等）
├── data/
│   └── robot_log.txt          # 日志、轨迹文件等数据文件目录（在执行过程中生成）
├── Robotic_Arm/               睿尔曼机械臂二次开发包
│   ├── include/
│   │   ├── rm_define.h        # 机械臂的定义
│   │   └── rm_interface.h     # 机械臂 API 的接口头文件
│   └── lib/
│       ├── api_cpp.dll          # Windows 的 API 库
│       ├── api_cpp.lib          # Windows 的 API 库
│       └── libapi_cpp.so        # Linux x86 的 API 库
├── src/                     # 源文件存放目录
│   ├── main.c               # 主要功能的源文件
├── run.bat                   # 快速运行脚本， Windows为bat脚本
├── run.sh                   # 快速运行脚本， linux为shell脚本
├── CMakeLists.txt           # 项目的顶层CMake配置文件
├── README.md                # 为示例工程提供详细的文档

```
## **3. 系统要求**

- 操作系统：Ubuntu 24.04或更高版本
- 编译器：GCC 13.3.0或更高版本 (或任何其他兼容的C编译器)
- 依赖库：
  - CMake 3.28.3或更高版本
  - RMAPI库(包含在 `Robotic_Arm/lib`目录中)

    
## **4. 安装说明**

1. 克隆项目到本地：

   ```bash

   ```

2. 构建项目：
   Linux下：
   cmake:
   ```bash
   mkdir build
   cd build
   cmake ..
   make
   
   ```



## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**

### **6.1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `RMDemo_DoubleControl` 文件，在 `main.cpp` 函数中修改 `ip1`和`ip2` 的初始化参数为当前机械臂的IP地址。

    ```C
       // 机械臂地址
    const char* ip1 = "192.168.1.18";
    int port1 = 8080;
    const char* ip2 = "192.168.1.21";
    int port2 = 8080;
    ```

2. **命令行运行**：在终端进入 `RMDemo_DoubleControl` 目录，输入以下命令运行C程序：
   2.1 Linux下
* ```bash
    chmod +x run.sh
    ./run.sh
    ```

2.2  Windows下: 双击运行 run.bat


### **6.2. 代码说明**


- 6.2.1 设置**IP地址**和**端口号**
```
    const char* ip1 = "192.168.1.18"; //具体IP地址根据实际情况填写
    int port1 = 8080; 
    const char* ip2 = "192.168.1.21";
    int port2 = 8080;
```
- 6.2.2启动线程（分别传入task_id=1和task_id=2）
```
    std::thread arm1_thread(arm_task, ip1, port1, 1);  // 机械臂1执行第一套动作
    std::thread arm2_thread(arm_task, ip2, port2, 2);  // 机械臂2执行第二套动作
```
- 6.2.3 定义两套动作的参数
```
    // 第一套动作参数
    float temp_joint1[ARM_DOF] = { 0.0f, 0.5f, 0.3f, 0.0f, 0.2f, 0.0f, 0.1f };
    memcpy(joint_angles, temp_joint1, sizeof(temp_joint1));
    start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
    target_pose = { {0.2f, 0.1f, 0.3f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
    loop_count = 2;
    move_speed = 20;

    // 第二套动作参数（task_id=2）
    float temp_joint2[ARM_DOF] = { 0.2f, -0.3f, 0.1f, 0.5f, -0.2f, 0.3f, 0.0f };
    memcpy(joint_angles, temp_joint2, sizeof(temp_joint2));
    start_pose = { {0.3f, 0.1f, 0.4f}, {0.0f, 0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
    target_pose = { {0.25f, -0.1f, 0.35f}, {0.0f, 0.0f, 0.0f}, {3.141f, 0.0f, 0.0f} };
    loop_count = 3;
    move_speed = 15;
```
- 6.2.4 根据任务选择不同的运动函数
```
        if (task_id == 1) {
            // 第一套动作：
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
        else {
            // 第二套动作：
            result = arm_service.rm_movel(robot_handle, target_pose, move_speed + 10, 0, 0, 1);
        }
```
- 6.2.5 断开与两个机械臂的连接
```
 result = arm_service.rm_delete_robot_arm(robot_handle);
 check_result(result, "Failed to disconnect the robot arm");
 printf("Task %d completed for %s:%d\n", task_id, ip, port);
 ```


### **6.3. 运行结果示例**

运行脚本后，输出结果如下所示：

```
API Version for 192.168.1.18:8080: 1.0.7.
Connecting to 192.168.1.18:8080...
API Version for 192.168.1.21:8080: 1.0.7.
Connecting to 192.168.1.21:8080...
Connected to 192.168.1.18:8080 (handle id: 1)
Connected to 192.168.1.21:8080 (handle id: 2)
Task 1 completed for 192.168.1.18:8080
Task 2 completed for 192.168.1.21:8080
All robot tasks completed
```




* **支持渠道**：

    + 开发者论坛/社区：[链接地址](https://bbs.realman-robotics.cn)
    + 

- API文档：详见`rm_interface.h`文件。


## **7. 许可证信息**

* 本项目遵循MIT许可证。

## **8. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。

- **Q:** 如何获取更多帮助？
  **A:** 请在GitHub项目页面提交Issue或联系维护者。
