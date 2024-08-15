# 机械臂API快速开始

## 1.引言

本开发包旨在为睿尔曼机械臂的二次开发提供便捷的接口。通过本开发包，用户能够实现对机械臂的控制、路径规划、状态监控等一系列功能，从而加速机械臂相关应用的开发过程。

## 2.目标受众

- **机械臂开发者**：对于希望利用Python、C、C++、C#等语言进行睿尔曼机械臂编程和调试的机器人开发者来说，本开发包提供了丰富的API和示例代码，方便快速上手。
- **自动化系统集成商**：在自动化系统中集成睿尔曼机械臂功能时，本开发包能够简化集成过程，提高开发效率。
- **科研人员**：科研人员可以利用本开发包进行睿尔曼机械臂相关算法的研究和实验，如路径规划、力控制等。
- **教育用户**：对于机器人教育领域的用户，本开发包可用于睿尔曼机械臂的教学和实验，帮助学生更好地理解和应用机械臂技术。

## 3.Python包使用说明

### 1.支持的操作系统与软件版本

#### 操作系统

- **Windows（64位和32位）**：支持Windows操作系统下的64位和32位版本，方便Windows用户进行机械臂开发。
- **Linux（x86和arm）**：支持Linux操作系统的x86架构和arm架构，满足不同硬件环境的需求。

#### 软件版本

- **Python 3.9以上**：本开发包基于Python 3.9及以上版本进行开发，确保与最新Python版本的兼容性。

### 2.安装与使用

#### 安装

用户可以通过pip命令进行安装：

```bash
pip install Robotic_Arm
```

或者本地下载二次开发包：：

```bash
git clone https://github.com/RealManRobot/RM_API2.git
```

#### 使用

安装完成后，用户可以在Python脚本中导入开发包并使用相关API接口进行机械臂的开发工作。以下是一个简单的使用机械臂Python开发包连接机械臂并查询机械臂版本的示例代码：

```python
from Robotic_Arm.rm_robot_interface import *

robot = RoboticArm(rm_thread_mode_e.RM_TRIPLE_MODE_E)
handle = robot.rm_create_robot_arm("192.168.1.18", 8080)
print("机械臂ID：", handle.id)

software_info = robot.rm_get_arm_software_info()
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
```

输出结果如下所示：

![输出结果图片](https://github.com/RealManRobot/RM_API2/blob/main/运行截图.png)


## 4.C/C++开发包使用说明

### 4.1 Windows环境使用说明

#### 4.1.1 支持的编译器

- **MSVC2015 或更高版本**：Microsoft Visual C++ 2015（MSVC2015）或更新的版本是推荐的编译器，它与Windows系统兼容性良好，且支持最新的C语言标准。使用MSVC可以方便地编译和调试C语言编写的睿尔曼机械臂控制程序。

#### 4.1.2 开发包说明

- **头文件**：C语言开发包含以下头文件：
  
  - `rm_define.h`：机械臂自定义头文件，包含了定义的数据类型、结构体。
  - `rm_interface.h`：机械臂自定义头文件，声明了C语言机械臂操作接口。
  
  如果是C++开发，则额外包含以下头文件：
  
  - `rm_service.h`：机械臂自定义头文件，声明了C++语言机械臂操作接口。
  - `rm_service_global.h`：机械臂自定义头文件，定义编译Windows C++版本库时导出宏。
  
- **动态链接库（DLLs）**：包含了控制机械臂所需的函数和接口。用户需要在项目中正确配置这些DLLs的路径及版本，以便编译器能够找到并链接它们。包含以下版本：

  - `32bit`：对应Windows 32位编译器（例如MSVC2017 32bit）使用的库，分为`release`版本
  - `64bit`：对应Windows 64位编译器（例如MSVC2017 64bit）使用的库，分为`release`版本

### 4.2 Linux 环境使用说明

#### 4.2.1 支持的架构

- **x86**：标准的Intel和AMD处理器架构。
- **ARM**：支持基于ARM架构的处理器。

#### 4.2.2 编译器

- **GCC**：GNU Compiler Collection（GCC）是Linux下广泛使用的开源编译器集合。编译器要求GCC 7.5以上版本，以确保最佳的性能和兼容性。

#### 4.2.3 开发包说明

- **头文件**：与Windows 头文件相同，详见Windows环境的开发包说明
- **共享库（.so 文件）**：包含了控制机械臂所需的函数和接口。用户需要确保这些库文件在编译和运行时都能被系统找到。包含以下版本的库：
  - `linux_x86_release`版本
  - `linux_arm_release`版本

### 4.3 使用示例

提供的Demo中包含`RMDemo_VisualStudio_Project`、`RMDemo_QtExample_C`、`RMDemo_SimpleProcess`等使用Qt、VS以及使用Cmake的项目示例，为用户提供多种工具多种环境的使用指导，包括配置环境、导入库文件、配置项目属性以及编译和运行项目等流程。

