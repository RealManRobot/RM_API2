#  机械臂关节角度透传示例

## **1. 项目介绍**

本项目演示如何将已规划好的关节角度点位透传给机械臂，并在机械臂运动过程中通过回调函数接收并处理机械臂UDP主动上报的状态数据。本项目基于Cmake构建，使用了睿尔曼提供的机械臂C语言开发包。

## **2. 代码结构**

```
RMDemo_MovejCANFD
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── data               # 包含各型号机械臂可用的透传轨迹文件
│   ├── RM65&RM63_canfd_data.txt    
│   ├── ECO65_canfd_data.txt
│   └── ...
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

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_C`目录，可找到RMDemo_MovejCANFD。

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

### **5.1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：
   打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

   ```C
   const char *robot_ip_address = "192.168.1.18";

   int robot_port = 8080;
   rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
   ```

2. **linux 命令行运行**：
   在终端进入 `RMDemo_MovejCANFD` 目录，输入以下命令运行C程序： 

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   运行结果如下：

3. **Windows 运行**： 双击run.bat脚本运行
   运行结果如下：

### **5.2 关键代码说明**

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


- **配置实时推送**

    ```C
    rm_realtime_push_config_t config = {5, true, 8089, 0, "192.168.1.88"};
    int result = rm_set_realtime_push(robot_handle, config);
    ```

- **读取关节角度轨迹文件并进行透传**

    ```C
    demo_movej_canfd(robot_handle)
    ```

- **断开机械臂连接**

    ```C
    disconnect_robot_arm(robot_handle);
    ```

### **5.3 运行结果示例**

运行脚本后，输出结果如下所示：

```bash
Run...
API Version: 1.0.0.
Robot handle created successfully: 1
Joint positions:
0.02 -25.82 -38.03 -0.04 -116.15 -0.00
Joint positions:
...
Joint positions:
0.02 -25.82 -38.03 -0.03 -116.15 0.00
Joint positions:
0.02 -25.82 -38.03 -0.03 -116.15 0.00
Joint positions:
0.02 -25.82 -38.03 -0.03 -116.15 0.00
Successfully set realtime push configuration.
Trying to open file: C:/Users/realman/830/RM_API2-main/RM_API2-main/Demo/RMDemo_C/RMDemo_MovejCANFD/data/RM65&RM63_canfd_data.txt
Total points: 3600
The motion is complete, the arm is in place.
Motion result: 1
Current device: 0
Is the next trajectory connected: 0
Moving to point 0
Moving to point 3598
Moving to point 3599
Pass-through completed
The motion is complete, the arm is in place.
Motion result: 1
Current device: 0
Is the next trajectory connected: 0
movej_cmd joint movement 1: 0
请按任意键继续...
```

运行脚本后，运行轨迹从上至下如下图所示：

![moveCANFD](moveCANFD.gif)

## **6. 许可证信息**

- 本项目遵循MIT许可证。
