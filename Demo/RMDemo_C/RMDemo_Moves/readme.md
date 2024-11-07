# 样条曲线运动示例

## **1. 项目介绍**

本项目演示了样条曲线运动的使用，项目基于Cmake构建，使用了睿尔曼提供的机械臂C语言开发包。

## **2. 代码结构**

```
RMDemo_Moves
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── include              # 自定义头文件存放目录
├── Robotic_Arm          # 睿尔曼机械臂二次开发包
│   ├── include
│   │   ├── rm_define.h  # 机械臂二次开发包头文件，包含了定义的数据类型、结构体
│   │   └── rm_interface.h # 机械臂二次开发包头文件，声明了机械臂所有操作接口
│   └── lib
│       ├── api_c.dll    # Windows 64bit 的 API 库
│       ├── api_c.lib    # Windows 64bit 的 API 库
│       └── libapi_c.so  # Linux x86 的 API 库
├── src
│   └── main.c           # 主函数
├── CMakeLists.txt       # 项目的顶层CMake配置文件
├── readme.md            # 项目说明文档
├── run.bat              # Windows快速运行脚本
└── run.sh               # linux快速运行脚本

```

## **3.项目下载**

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_C`目录，可找到RMDemo_Moves。

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
   在终端进入 `RMDemo_Moves` 目录，输入以下命令运行C程序：

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   运行结果如下：

```bash
API Version: 1.0.0.
Robot handle created successfully: 1
Trajectory Connect Value at Step 0: 1
Trajectory Connect Value at Step 1: 1
Trajectory Connect Value at Step 2: 1
Trajectory Connect Value at Step 3: 1
Trajectory Connect Value at Step 4: 0
moves operation succeeded
```

3. **Windows 运行**： 双击run.bat脚本运行
   运行结果如下：

```bash
Run...
API Version: 1.0.0.
Robot handle created successfully: 1
Trajectory Connect Value at Step 0: 1
Trajectory Connect Value at Step 1: 1
Trajectory Connect Value at Step 2: 1
Trajectory Connect Value at Step 3: 1
Trajectory Connect Value at Step 4: 0
moves operation succeeded
请按任意键继续. . .
```

### **5.2 关键代码说明**

下面是 `main.c` 文件的主要功能：
- **定义各型号机械臂初始化参数数组**

    ```C
    ArmModelData arm_data[9] = {
        [RM_MODEL_RM_65_E] = {
            .joint_angles = {0, 0, 0, 0, 0, 0}, 
            .pose = { .position = {-0.3, 0, 0.3}, .euler = {3.14, 0, 0}},
            .point_list = { {.position = {-0.3, 0, 0.3}, .euler = {3.14, 0, 0}},
                            {.position = {-0.27, -0.22,0.3}, .euler = {3.14, 0, 0}},
                            {.position = {-0.314, -0.25, 0.2}, .euler = {3.14, 0, 0}},
                            {.position = {-0.239, 0.166, 0.276}, .euler = {3.14, 0, 0}},
                            {.position = {-0.239, 0.264, 0.126}, .euler = {3.14, 0, 0}},}
        },
        [RM_MODEL_RM_75_E] = {
            .joint_angles = {0, 20, 0, 70, 0, 90, 0},  
            .pose = { .position = {0.297557, 0, 0.337061}, .euler = {3.142, 0, 3.142} } ,
            .point_list = { {.position = {0.3, 0.1, 0.337061}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.2, 0.3, 0.237061}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.2, 0.25, 0.037061}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.1, 0.3, 0.137061}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.2, 0.25, 0.337061}, .euler = {3.142, 0, 3.142}}, }
        }, 
        [RM_MODEL_RM_63_II_E] = {  
            .joint_angles = {0, 20, 70, 0, 90, 0},
            .pose = { .position = {0.448968, 0, 0.345083}, .euler = {3.14, 0, 3.142} },
            .point_list = { {.position = {0.3, 0.3, 0.345083}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.3, 0.4, 0.145083}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.3, 0.2, 0.045083}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.4, 0.1, 0.145083}, .euler = {3.142, 0, 3.142}},
                            {.position = {0.5, 0, 0.345083}, .euler = {3.142, 0, 3.142}}, }
        },
        [RM_MODEL_ECO_65_E] = {  
            .joint_angles = {0, 20, 70, 0, -90, 0},
            .pose = { .position = {0.352925, -0.058880, 0.327320}, .euler = {3.141, 0, -1.57} } ,
            .point_list = { {.position = {0.3, 0.3, 0.327320}, .euler = {3.141, 0, -1.57}},
                            {.position = {0.2, 0.4, 0.127320}, .euler = {3.141, 0, -1.57}},
                            {.position = {0.2, 0.2, 0.027320}, .euler = {3.141, 0, -1.57}},
                            {.position = {0.3, 0.1, 0.227320}, .euler = {3.141, 0, -1.57}},
                            {.position = {0.4, 0, 0.327320}, .euler = {3.141, 0, -1.57}}, }
        },
        [RM_MODEL_GEN_72_E] = {  
            .joint_angles = {0, 0, 0, -90, 0, 0, 0},
            .pose = { .position = {0.359500, 0, 0.426500}, .euler = {3.142, 0, 0} } ,
            .point_list = { {.position = {0.359500, 0, 0.426500}, .euler = {3.142, 0, 0}},
                            {.position = {0.2, 0.3, 0.426500}, .euler = {3.142, 0, 0}},
                            {.position = {0.2, 0.3, 0.3}, .euler = {3.142, 0, 0}},
                            {.position = {0.3, 0.3, 0.3}, .euler = {3.142, 0, 0}},
                            {.position = {0.3, -0.1, 0.4}, .euler = {3.142, 0, 0}} }
        },
        [RM_MODEL_ECO_63_E] = {  
            .joint_angles = {0, 20, 70, 0, -90, 0},
            .pose = { .position = {0.544228, -0.058900, 0.468274}, .euler = {3.142, 0, -1.571} },
            .point_list = { {.position = {0.3, 0.3, 0.468274}, .euler = {3.142, 0, -1.571}},
                            {.position = {0.3, 0.4, 0.168274}, .euler = {3.142, 0, -1.571}},
                            {.position = {0.3, 0.2, 0.268274}, .euler = {3.142, 0, -1.571}},
                            {.position = {0.4, 0.1, 0.368274}, .euler = {3.142, 0, -1.571}},
                            {.position = {0.5, 0, 0.468274}, .euler = {3.142, 0, -1.571}} }
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

- **执行movej运动**

    ```C
    rm_movej(robot_handle, arm_data[arm_info.arm_model].joint_angles, 20, 0, 0, 1);
    ```

- **执行movej_p运动**

    ```C
    rm_movej_p(robot_handle, arm_data[arm_info.arm_model].pose, 20, 0, 0, 1);
    ```

- **执行moves运动**

    ```C
    execute_moves(robot_handle, arm_data[arm_info.arm_model].point_list, POINT_NUM, 20, 1);
    ```
  
- 执行moves运动，沿多点轨迹进行样条曲线移动。 轨迹如下图所示
![Moves_trajectoryConnect](Moves_trajectoryConnect.png)

- 当 trajectory_connect 为 0时候 会如下：
![Moves_trajectory](Moves_trajectory.png)

- **断开机械臂连接**

    ```C
    disconnect_robot_arm(robot_handle);
    ```

## **6. 许可证信息**

- 本项目遵循MIT许可证。
