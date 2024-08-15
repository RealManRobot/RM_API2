#  RMDemo_Gripper

## **1. 项目介绍**
本项目是一个使用睿尔曼C开发包, 模拟进行物体抓取，可以进行在固定位置抓取物体，运动到指定位置，控制夹爪持续力夹取，夹取到位后，在通过运动到放置位，并控制松开，机械臂回到初始位姿。

## **2. 代码结构**
```
RMDemo_Gripper/
├── build/                  # CMake构建生成的输出目录（如Makefile、构建文件等）
├── cmake/                  # CMake模块和脚本的存放目录
│   ├── FindMyLib.cmake     # 自定义的Find模块，用于查找外部库
├── data/
│   └── robot_log.txt          # 日志、轨迹文件等数据文件目录（在执行过程中生成）
├── include/                # 自定义头文件存放目录
├── Robotic_Arm/               睿尔曼机械臂二次开发包
│   ├── include/
│   │   ├── rm_define.h        # 机械臂的定义
│   │   └── rm_interface.h     # 机械臂 API 的接口头文件
│   └── lib/
│       ├── api_c.dll          # Windows 的 API 库
│       ├── api_c.lib          # Windows 的 API 库
│       └── libapi_c.so        # Linux 的 API 库
├── src/                     # 源文件存放目录
│   ├── main.c # 主要功能的源文件
├── run.bat                   # 快速运行脚本， Windows为bat脚本
├── run.sh                   # 快速运行脚本， linux为shell脚本
├── CMakeLists.txt           # 项目的顶层CMake配置文件
├── README.md                # 为示例工程提供详细的文档

```
## **3. 系统要求**

- 操作系统：Ubuntu 18.04或更高版本
- 编译器：GCC 7.5或更高版本 (或任何其他兼容的C编译器)
- 依赖库：
  - CMake 3.10或更高版本
  - RMAPI库(包含在 `Robotic_Arm/lib`目录中)

    
## **4. 安装说明**

以Linux为例，项目的安装说明如下所示：
4.1. 配置环境：


- Linux 安装cmake依赖：

  ```bash
  sudo apt-get update
  sudo apt-get install build-essential
  sudo apt-get install cmake
  ```

  检查和安装依赖项：

  ```
  gcc --version
  cmake --version
  Windows 安装cmake依赖
  ```
  CMake：确保已安装最新版本的 CMake。可以从 CMake官网 下载并安装。
  编译器：安装 MinGW 或 Visual Studio (MSVC) 以进行构建。MinGW 是一个开源编译器套件，可以从 MinGW官网 下载。Visual Studio 包含 MSVC，可以从 Visual Studio官网 下载并安装。
  依赖库：
  api_c.dll 和 api_c.lib：确保这些库文件存在于 Robotic_Arm/lib 目录中。
  确保项目中的 include 目录和其他源文件路径正确设置。
  ```

4.2. 克隆项目到本地：

   ```
   
   ```
   

## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**

### **6.1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_gripper.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```

2. **命令行运行**：在终端进入 `RMDemo_Gripper` 目录，输入以下命令运行C程序：
   2.1 Linux下
* ```bash
    chmod +x run.sh
   ./run.sh
    ```

2.2  Windows下: 双击运行 run.bat


### **6.2. 代码说明**

下面是 `main.c` 文件的主要功能：

- **连接机械臂**

    ```C
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```
  连接到指定IP和端口的机械臂。

- **获取API版本**

    ```C
    char *api_version = rm_api_version();
    printf("API Version: %s.\n", api_version);
    ```
  获取并显示API版本。


- **切换工作坐标系**

    ```C
    rm_change_work_frame(robot_handle, "Base");
    ```
- **末端控制 设置工具端电源输出 夹爪 24v**

    ```C
    rm_set_tool_voltage(robot_handle, 3);
    ```


- **执行 movej 运动**

    ```C
    float joint_angles_start[6] = {90.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
    float joint_angles_end[6] = {0.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
    // Perform movej motion Start
    result = rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
    ```

- **控制夹爪持续力夹取**

    ```C
    rm_set_gripper_pick_on(robot_handle, 500, 200, true, 30);
    ```

- **再次执行  movel运动**

    ```C
    float joint_angles_end[6] = {0.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
    // Perform movej motion End
    rm_movej(robot_handle, joint_angles_start, 20, 0, 1, 0);
    ```


- **控制夹爪松开**

    ```C
    rm_set_gripper_release(robot_handle, 500, true, 30);
    ```

- **断开机械臂连接**

    ```C
    rm_delete_robot_arm(robot_handle);
    ```


### **6.3. 运行结果示例**

运行脚本后，输出结果如下所示：
```
API Version: 0.3.0.
Robot handle created successfully: 1
Change work frame: 0
INFO: movej: Operation successful
INFO: set_gripper_pick_on: Operation successful
INFO: movej: Operation successful
INFO: set_gripper_release: Operation successful
INFO: movej: Operation successful
Successfully disconnected from the robot arm


Linux：
chmod +x run.sh

./run.sh
./run.sh
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- RMAN_API_LIB: /home/cloud/v4/RMDemo_Gripper/Robotic_Arm/lib/libapi_c.so
-- Configuring done
-- Generating done
-- Build files have been written to: /home/cloud/v4/RMDemo_Gripper/build
[ 25%] Building C object CMakeFiles/demo_gripper.dir/src/demo_gripper.c.o
[ 50%] Building C object CMakeFiles/demo_gripper.dir/src/utils.c.o
[ 75%] Building C object CMakeFiles/demo_gripper.dir/src/main.c.o
[100%] Linking C executable demo_gripper
[100%] Built target demo_gripper
API Version: 0.3.0.
Robot handle created successfully: 1
Change work frame: 0
INFO: movej: Operation successful
INFO: set_gripper_pick_on: Operation successful
INFO: movej: Operation successful
INFO: set_gripper_release: Operation successful
INFO: movej: Operation successful
Successfully disconnected from the robot arm
```

运行脚本后，运行如下图所示：
![demo_gripper](demo_gripper.gif)

  
* **支持渠道**：

    + 开发者论坛/社区：[链接地址](https://bbs.realman-robotics.cn)
    + 

- API文档：详见`rm_interface.h`文件。


## **6. 许可证信息**

* 本项目遵循MIT许可证。

## **7. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。

- **Q:** 执行的时候卡顿？
  **A:** 检查夹爪连接是否正常 【扩展】【末端控制】里面的工具端电源输出 夹爪状态是否正常。 如果出现 ERROR: set_gripper_pick_on 或者 set_gripper_release: Current device verification failed, device not a joint, Error code: -4
 