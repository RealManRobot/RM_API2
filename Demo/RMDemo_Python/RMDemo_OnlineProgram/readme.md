# 在线编程示例

## 1. 项目介绍

本项目是一个使用睿尔曼Python开发包demo实现拖动示教，将轨迹保存到文件夹下，并拼接为在线编程文件，再通过在线编程文件下发运动该轨迹，获得在线编程运动状态，暂停、继续在线编程。

## 2. 代码结构

```
RMDemo_OnlineProgram/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_online_program.py      <- demo实现拖动示教，将轨迹保存到文件夹下，并拼接为在线编程文件，再通过在线编程文件下发运动该轨迹，获得在线编程运动状态，暂停、继续在线编程。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_OnlineProgram。

## 4. 环境配置

在Windows和Linux环境下运行时需要的环境和依赖项：

| 项目         | Linux     | Windows   |
| :--          | :--       | :--       |
| 系统架构     | x86架构   | -         |
| python       | 3.9以上   | 3.9以上   |
| 特定依赖     | -         | -         |

### Linux环境配置

   1. 参考[python官网-linux](https://www.python.org/downloads/source/)下载安装python3.9。

   2. 进入项目目录后打开终端运行以下指令安装依赖：

```bash
pip install -r requirements.txt
```

### Windows环境配置

   1. 参考[python官网-Windows](https://www.python.org/downloads/windows/)下载安装python3.9。

   2. 进入项目目录后打开终端运行以下指令安装依赖：

```bash
pip install -r requirements.txt
```

## 5. 注意事项

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## 6. 使用指南

### 1. 快速运行

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_online_program.py` 文件，在 `main` 函数中修改 `RobotArmController` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。
    ```python
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```
2. **配置文件保存至在线编程列表的id号（默认为100）**：通过修改方法`demo_send_project`中的`save_id`参数修改文件保存至在线编程时的id。请检查在线编程列表，必要时修改该id号以确保在您的在线编程列表中该id为可用的。

3. **命令行运行**：在终端进入 `RMDemo_OnlineProgram` 目录，输入以下命令运行Python脚本：

    ```bash
    python ./src/main.py
    ```

4. **运行结果**：在终端中看到以下输出信息，即表示程序运行成功。

运行脚本后，输出结果如下所示：

```
current api version:  0.2.9

Successfully connected to the robot arm: 1

API Version:  0.2.9

Drag teaching started

Drag teaching has started, complete the drag operation and press Enter to continue...

Drag teaching stopped

Trajectory saved successfully, total number of points: 100

Project sent and run successfully

Program running state: 1

Program running state: 1

Program running state: 0
Program has ended

Robot arm paused successfully

Program running state: 0
Program has ended

Robot arm continued successfully

Program running state: 1

Program running state: 0
Program has ended

Successfully disconnected from the robot arm
```


### 2. 代码说明

下面是 `demo_online_program.py` 文件的主要功能：

- **连接机械臂**

    ```python
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```
    连接到指定IP和端口的机械臂。

- **获取API版本**

    ```python
    print("\nAPI Version:", rm_api_version(), "\n")
    ```
    获取并显示API版本。

- **拖动示教**

    ```python
    robot_controller.demo_drag_teach(1)
    ```
    启动拖动示教模式，参数 `1` 表示记录轨迹。

- **保存轨迹**

    ```python
    lines = robot_controller.demo_save_trajectory(file_path_test)
    ```
    保存记录的轨迹到指定文件。

- **拼接在线编程文件**

    ```python
    robot_controller.add_lines_to_file(file_path_test, lines)
    ```
    将特定行添加到轨迹文件中，形成在线编程文件。

- **下发在线编程文件**

    ```python
    robot_controller.demo_send_project(file_path_test)
    ```
    将在线编程文件发送到机械臂。

- **查询在线编程运行状态**

    ```python
    robot_controller.demo_get_program_run_state(1, max_retries=5)
    ```
    查询在线编程的运行状态，间隔 `1` 秒，最大查询次数为 `5`。

- **暂停机械臂**

    ```python
    robot_controller.demo_set_arm_pause()
    ```
    暂停机械臂运行。

- **继续机械臂运行**

    ```python
    robot_controller.demo_set_arm_continue()
    ```
    继续机械臂运行。

- **断开机械臂连接**

    ```python
    robot_controller.disconnect()
    ```
    断开与机械臂的连接。


## 7. 许可证信息

- 本项目遵循MIT许可证。