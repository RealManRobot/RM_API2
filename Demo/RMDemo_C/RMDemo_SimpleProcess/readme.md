# Cmake项目基础搭建示例

## **1. 项目介绍**
本项目提供了一个基于Cmake构建，使用睿尔曼机械臂C语言开发包完成机械臂连接、机械臂版本获取、API 版本获取、Movej 运动、连接关闭等基本功能的示例，旨在帮助用户快速创建一个cmake构建的跨平台项目。

## **2. 代码结构**

```

RMDemo_SimpleProcess
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── include              # 自定义头文件存放目录
├── Robotic_Arm          # 睿尔曼机械臂二次开发包
│   ├── include
│   │   ├── rm_define.h  # 机械臂二次开发包头文件，包含了定义的数据类型、结构体
│   │   └── rm_interface.h # 机械臂二次开发包头文件，声明了机械臂所有操作接口
│   ├── lib
│   │   ├── api_c.dll    # Windows 64bit 的 API 库
│   │   ├── api_c.lib    # Windows 64bit 的 API 库
│   │   └── libapi_c.so  # Linux x86 的 API 库
├── src
│   ├── main.c           # 主函数
├── CMakeLists.txt       # 项目的顶层CMake配置文件
├── readme.md            # 项目说明文档
├── run.bat              # Windows快速运行脚本
└── run.sh               # linux快速运行脚本
```

## **3.项目下载**

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_C`目录，可找到RMDemo_SimpleProcess。

## **4. 环境配置**

在Windows和Linux环境下运行时需要的环境和依赖项：

| 项目      | Linux                                          | Windows                                          |
| :-------- | :--------------------------------------------- | :----------------------------------------------- |
| 系统架构  | x86架构                                        | -                                                |
| 编译器    | GCC 7.5或更高版本                              | MSVC2015或更高版本 64bit                         |
| CMake版本 | 3.10或更高版本                                 | 3.10或更高版本                                   |
| 特定依赖  | RMAPI Linux版本库（位于`Robotic_Arm/lib`目录） | RMAPI Windows版本库（位于`Robotic_Arm/lib`目录） |

### Linux环境配置

**1. 编译器（GCC）**
在大多数Linux发行版中，GCC是默认安装的，但可能版本不是最新的。如果需要安装特定版本的GCC（如7.5或更高版本），可以使用包管理器进行安装。以Ubuntu为例，可以使用以下命令安装或更新GCC：

```bash
# 检查GCC版本
gcc --version

sudo apt update
sudo apt install gcc-7 g++-7  
```

注意：如果系统默认安装的GCC版本已满足或高于要求，则无需进行额外安装。

**2. CMake**
CMake在大多数Linux发行版中也可以通过包管理器安装。以Ubuntu为例：

```bash
sudo apt update
sudo apt install cmake

# 检查CMake版本
cmake --version
```

### Windows环境配置

**1. 编译器（MSVC2015或更高版本）**
MSVC（Microsoft Visual C++）编译器通常随Visual Studio一起安装。可以按照以下步骤安装：

1. 访问[Visual Studio官网](https://visualstudio.microsoft.com/)下载并安装Visual Studio。
2. 在安装过程中，选择“使用C++的桌面开发”工作负载，这将包括MSVC编译器。
3. 根据需要选择其他组件，如CMake（如果尚未安装）。
4. 完成安装后，打开Visual Studio命令提示符（可在开始菜单中找到），输入`cl`命令检查MSVC编译器是否安装成功。

**2. CMake**
如果Visual Studio安装过程中未包含CMake，可以单独下载并安装CMake。

1. 访问[CMake官网](https://cmake.org/download/)下载适用于Windows的安装程序。
2. 运行安装程序，按照提示进行安装。
3. 安装完成后，将CMake的bin目录添加到系统的PATH环境变量中（通常在安装过程中会询问是否添加）。
4. 打开命令提示符或PowerShell，输入`cmake --version`检查CMake是否安装成功。

## **5. 使用指南**

### **5.1 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：
   打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

   ```C
   const char *robot_ip_address = "192.168.1.18";

   int robot_port = 8080;
   rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
   ```

2. **linux 命令行运行**：
   在终端进入 `RMDemo_SimoleProcess` 目录，输入以下命令运行C程序：

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   运行结果如下：

    ```bash
    API Version: 1.0.0.
    Robot handle created successfully: 1
    ================== Arm Software Information ==================
    Arm Model:  RM65-BI
    Algorithm Library Version:  1.4.4
    Control Layer Software Version:  V1.6.1
    Dynamics Version:  2
    Planning Layer Software Version:  V1.6.1
    ==============================================================
    ```

3. **Windows 运行**： 双击run.bat脚本运行
   运行结果如下：

```bash
API Version: 1.0.0.
Robot handle created successfully: 1
================== Arm Software Information ==================
Arm Model:  RM65-BI
Algorithm Library Version:  1.4.4
Control Layer Software Version:  V1.6.1
Dynamics Version:  2
Planning Layer Software Version:  V1.6.1
==============================================================
请按任意键继续...
```

### **5.2 关键代码说明**

下面是 `main.c` 文件的主要功能：
- **定义各型号机械臂参数数组**
    ```C
    ArmModelData arm_data[9] = {
        [RM_MODEL_RM_65_E] = {
            .joint_angles = {0, 20, 70, 0, 90, 0},
            .movej_pose1 = { .position = {0.3, 0, 0.3}, .euler = {3.14, 0, 0} },
            .movel_pose = { .position = {0.3, 0, 0.3}, .euler = {3.14, 0, 0} },
            .movej_pose2 = { .position = {0.3, 0, 0.3}, .euler = {3.14, 0, 0} },
            .movec_pose_via = { .position = {0.2, 0.05, 0.3}, .euler = {3.14, 0, 0} },
            .movec_pose_to = { .position = {0.2, -0.05, 0.3}, .euler = {3.14, 0, 0} }
        },
        [RM_MODEL_RM_75_E] = {
            .joint_angles = {0, 20, 0, 70, 0, 90, 0},  
            .movej_pose1 = { .position = {0.297557, 0, 0.337061}, .euler = {3.142, 0, 3.142} } ,
            .movel_pose = { .position = {0.097557, 0, 0.337061}, .euler = {3.142, 0, 3.142} } ,
            .movej_pose2 = { .position = {0.297557, 0, 0.337061}, .euler = {3.142, 0, 3.142} } ,
            .movec_pose_via = { .position = {0.257557, -0.08, 0.337061}, .euler = {3.142, 0, 3.142} } ,
            .movec_pose_to = { .position = {0.257557, 0.08, 0.337061}, .euler = {3.142, 0, 3.142} } 
        }, 
        [RM_MODEL_RM_63_II_E] = {  
            .joint_angles = {0, 20, 70, 0, 90, 0},  
            .movej_pose1 = { .position = {0.448968, 0, 0.345083}, .euler = {3.142, 0, 3.142} },
            .movel_pose = { .position = {0.248968, 0, 0.345083}, .euler = {3.142, 0, 3.142} },
            .movej_pose2 = { .position = {0.448968, 0, 0.345083}, .euler = {3.142, 0, 3.142} },
            .movec_pose_via = { .position = {0.408968, -0.1, 0.345083}, .euler = {3.142, 0, 3.142} },
            .movec_pose_to = { .position = {0.408968, 0.1, 0.345083}, .euler = {3.142, 0, 3.142} }
        },
        [RM_MODEL_ECO_65_E] = {  
            .joint_angles = {0, 20, 70, 0, -90, 0},  
            .movej_pose1 = { .position = {0.352925, -0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
            .movel_pose = { .position = {0.152925, -0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
            .movej_pose2 = { .position = {0.352925, -0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
            .movec_pose_via = { .position = {0.302925, -0.158880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
            .movec_pose_to = { .position = {0.302925, 0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } 
        },
        [RM_MODEL_GEN_72_E] = {  
            .joint_angles = {0, 0, 0, -90, 0, 0, 0},  
            .movej_pose1 = { .position = {0.1, 0, 0.4}, .euler = {3.14, 0, 0} } ,
            .movel_pose = { .position = {0.3, 0, 0.4}, .euler = {3.14, 0, 0} } ,
            .movej_pose2 = { .position = {0.3595, 0, 0.4265}, .euler = {3.14, 0, 0} } ,
            .movec_pose_via = { .position = {0.3595, 0.03, 0.4265}, .euler = {3.14, 0, 0} } ,
            .movec_pose_to = { .position = {0.3595, 0.03, 0.4665}, .euler = {3.14, 0, 0} } 
        },
        [RM_MODEL_ECO_63_E] = {  
            .joint_angles = {0, 20, 70, 0, -90, 0},  
            .movej_pose1 = { .position = {0.544228, -0.058900, 0.468274}, .euler = {3.14, 0, -1.571} },
            .movel_pose = { .position = {0.344228, -0.058900, 0.468274}, .euler = {3.14, 0, -1.571} },
            .movej_pose2 = { .position = {0.544228, -0.058900, 0.468274}, .euler = {3.14, 0, -1.571} },
            .movec_pose_via = { .position = {0.504228, -0.108900, 0.468274}, .euler = {3.14, 0, -1.571} },
            .movec_pose_to = { .position = {0.504228, -0.008900, 0.468274}, .euler = {3.14, 0, -1.571} }
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

## **6. 许可证信息**

- 本项目遵循MIT许可证。
