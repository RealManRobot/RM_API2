#  在线编程示例

## **1. 项目介绍**

本项目演示了读取demo下的在线编程文件，将文件发送给机械臂运行，并实时检测在线编程文件运行的状态、行数、循环数等信息。项目基于Cmake构建，使用了睿尔曼提供的机械臂C语言开发包。

## **2. 代码结构**

```
RMDemo_OnlineProgram
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── data
│   ├── trajectory.txt  # 拖动示教保存的轨迹文件（在执行过程中生成）
│   └── project.txt     # 拖动示教轨迹文件生成的在线编程文件（在执行过程中生成）
├── include              # 自定义头文件存放目录
├── Robotic_Arm          睿尔曼机械臂二次开发包
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

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_C`目录，可找到RMDemo_OnlineProgram。

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
   在终端进入 `RMDemo_OnlineProgram` 目录，输入以下命令运行C程序：

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   运行结果如下：

    ```bash
    API Version: 1.0.0.
    Robot handle created successfully: 1
    Drag teaching started
    Drag teaching has started, complete the drag operation and press Enter to continue...
   
    Please enter a Save ID for this teaching session: 50
    Save ID { 50 } for this teaching session saved to the controller
    Drag teaching stopped
    Trajectory saved successfully, total number of points: 3
    Project sent and run successfully
    Program running state: 0
    Program has ended
    Program running state: 0
    Program has ended
    Program running state: 0
    Program has ended
    ```

3. **Windows 运行**： 双击run.bat脚本运行
   运行结果如下：

```bash
Run...
API Version: 1.0.0.
Robot handle created successfully: 1
Drag teaching started
Drag teaching has started, complete the drag operation and press Enter to continue...

Please enter a Save ID for this teaching session: 1
Save ID { 1 } for this teaching session saved to the controller
Drag teaching stopped
Trajectory saved successfully, total number of points: 1805
Project sent and run successfully
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Reached maximum query attempts, exiting
Program running state: 2
Program running state: 2
Program running state: 2
Program running state: 2
Program running state: 2
Reached maximum query attempts, exiting
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Reached maximum query attempts, exiting
请按任意键继续...
```

### **5.2. 代码说明**

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

- **拖动示教**
  启动拖动示教模式，参数 `1` 表示记录轨迹。

    ```C
    start_drag_teach(robot_handle, 1);
    ```

- **保存轨迹**
  保存记录的轨迹到指定文件。

    ```C
    int lines;
    result = rm_save_trajectory(robot_handle, TRAJECTORY_FILE_PATH, &lines);
    ```

- **拼接在线编程文件**
  将特定行添加到轨迹文件中，形成在线编程文件。

    ```C
    add_lines_to_file(robot_handle, file_path_test, lines);
    ```

- **下发在线编程文件**
  将在线编程文件发送到机械臂。

    ```C
    send_project(robot_handle, PROJECT_FILE_PATH, 20, 0, save_id, 0, 0, 0);
    ```

- **查询在线编程运行状态**
  查询在线编程的运行状态，间隔 `1` 秒，最大查询次数为 `5`。

    ```C
    get_program_run_state(robot_handle, 1, 5);
    ```

- **暂停机械臂**
  暂停机械臂运行。

    ```C
    set_arm_pause(robot_handle);
    ```

- **继续机械臂运行**
  继续机械臂运行。

    ```C
    set_arm_continue(robot_handle);
    ```

- **断开机械臂连接**
  断开与机械臂的连接。

    ```C
    disconnect_robot_arm(robot_handle);
    ```

## **6. 许可证信息**

- 本项目遵循MIT许可证。
