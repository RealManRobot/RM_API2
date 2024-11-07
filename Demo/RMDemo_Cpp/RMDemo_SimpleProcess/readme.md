#  RMDemo_SimpleProcess


## **1. 项目介绍**
本项目是一个使用睿尔曼C开发包,演示机械臂 API 使用cmake框架使用方式，演示项目中包含 readme.md 文件。该文件描述了项目在不同平台上支持的编译器版本和 VS 版本，并通过项目完成机械臂连接、机械臂版本获取、API 版本获取、Movej 运动、连接关闭等功能。

## **2. 代码结构**
```

RMDemo_SimpleProcess
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── cmake              # CMake模块和脚本的存放目录
│   ├── ...
├── data
│   └── robot_log.txt    # 日志、轨迹文件等数据文件目录（在执行过程中生成）
├── include              # 自定义头文件存放目录
├── Robotic_Arm          睿尔曼机械臂二次开发包
│   ├── include
│   │   ├── rm_define.h  # 机械臂的定义
│   │   └── rm_interface.h # 机械臂 API 的接口头文件
│   ├── lib
│   │   ├── api_c.dll    # Windows 的 API 库
│   │   ├── api_c.lib    # Windows 的 API 库
│   │   └── libapi_c.so  # Linux 的 API 库
├── src
│   ├── main.c           # 主函数
├── CMakeLists.txt       # 项目的顶层CMake配置文件
├── readme.md            # 为示例工程提供详细的文档
├── run.bat              # 快速运行脚本， Windows为bat脚本
└── run.sh               # 快速运行脚本， linux为shell脚本


```

## **3. 系统要求**

- 操作系统：Ubuntu 18.04或更高版本
- 编译器：GCC 7.5或更高版本 (或任何其他兼容的C编译器)
- 依赖库：
  - CMake 3.10或更高版本
  - RMAPI库(包含在 `Robotic_Arm/lib`目录中)
- 一台 Realman 机械臂
- 一台安装了 Visual Studio 的 Windows 系统


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

### **1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```
2. **命令行运行**：在终端进入 `RMDemo_SimpleProcess` 目录，输入以下命令运行 C程序：

2.1 Linux下
* ```bash
    chmod +x run.sh
   ./run.sh
    ```

2.2  Windows下: 双击运行 run.bat

### **2. 代码说明**

下面是 `main.c` 文件的主要功能：
- **定义各型号机械臂参数数组**
    ```C
    ArmModelData arm_data[9] = {
      {
          {0, 20, 70, 0, 90, 0},
          {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
          {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
          {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} },
          {{0.2, 0.05, 0.3}, {0,0,0,0},{3.14, 0, 0} },
          {{0.2, -0.05, 0.3}, {0,0,0,0},{3.14, 0, 0} }
      },
      {
          {0, 20, 0, 70, 0, 90, 0},  
          {{0.297557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
          {{0.097557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
          {{0.297557, 0, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
          {{0.257557, -0.08, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } ,
          {{0.257557, 0.08, 0.337061}, {0,0,0,0},{3.142, 0, 3.142} } 
      }, 
      {0},
      {  
          {0, 20, 70, 0, 90, 0},  
          {{0.448968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
          {{0.248968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
          {{0.448968, 0, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
          {{0.408968, -0.1, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} },
          {{0.408968, 0.1, 0.345083}, {0,0,0,0},{3.142, 0, 3.142} }
      },
      {0},
      {  
          {0, 20, 70, 0, -90, 0},  
          {{0.352925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
          {{0.152925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
          {{0.352925, -0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
          {{0.302925, -0.158880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } ,
          {{0.302925, 0.058880, 0.327320}, {0,0,0,0},{3.14, 0, -1.57} } 
      },
      {

      },
      {  
          {0, 0, 0, -90, 0, 0, 0},  
          {{0.1, 0, 0.4},{0,0,0,0}, {3.14, 0, 0} } ,
          {{0.3, 0, 0.4},{0,0,0,0}, {3.14, 0, 0} } ,
          {{0.3595, 0, 0.4265},{0,0,0,0}, {3.14, 0, 0} } ,
          {{0.3595, 0.03, 0.4265},{0,0,0,0}, {3.14, 0, 0} } ,
          {{0.3595, 0.03, 0.4665},{0,0,0,0}, {3.14, 0, 0} } 
      },
      {  
          {0, 20, 70, 0, -90, 0},  
          {{0.544228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
          {{0.344228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
          {{0.544228, -0.058900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
          {{0.504228, -0.108900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} },
          {{0.504228, -0.008900, 0.468274}, {0,0,0,0},{3.14, 0, -1.571} }
      }
    };
    ```

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


- **获取机械臂软件信息**

    ```C
    get_robot_software_info(robot_handle);
    ```
  获取并显示机械臂的基本信息，包括产品版本、算法库版本、控制层软件版本、动力学版本和规划层软件版本。

- **执行movej运动**

    ```C
    rm_movej(robot_handle, arm_data[arm_info.arm_model].joint_angles, 20, 0, 0, 1);
    ```

- **执行movej_p运动**

    ```C
    rm_movej_p(robot_handle, arm_data[arm_info.arm_model].movej_pose1, 20, 0, 0, 1);
    ```

- **执行movel运动**

    ```C
    rm_movel(robot_handle, arm_data[arm_info.arm_model].movel_pose, 20, 0, 0, 1);
    ```

- **执行movec运动**

    ```C
    rm_movec(robot_handle, arm_data[arm_info.arm_model].movec_pose_via, arm_data[arm_info.arm_model].movec_pose_to, 20, 2, 0, 0, 1);
    ```

- **断开机械臂连接**

    ```C
    disconnect_robot_arm(robot_handle);
    ```

### **3. 运行结果示例**

运行脚本后，输出结果如下所示：

```
API Version: 0.3.0.
Robot handle created successfully: 1
INFO: get_robot_software_info: Operation successful
Get arm software version succeeded
================== Arm Software Information ==================
Arm Model:  RM65-BI
Algorithm Library Version:  1.3.4
Control Layer Software Version:  V1.5.6
Dynamics Version:  2
Planning Layer Software Version:  V1.5.6
==============================================================

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
