# 机械臂抓取示例

## 1. 项目介绍

本项目是一个使用睿尔曼Python开发包模拟进行物体抓取，可以进行在固定位置抓取物体，运动到指定位置，控制夹爪持续力夹取，夹取到位后，在通过运动到放置位，并控制松开，机械臂回到初始位姿。

## 2. 代码结构

```
RMDemo_Gripper/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_gripper.py      <- 模拟进行物体抓取，可以进行在固定位置抓取物体，运动到指定位置，控制夹爪持续力夹取，夹取到位后，在通过运动到放置位，并控制松开，机械臂回到初始位姿。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_Gripper。

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

该Demo需末端装配夹爪使用。

## 6. 使用指南

### 1. 快速运行

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_gripper.py` 文件，在 `main` 函数中修改 `RobotArmController` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```python
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```

2. **命令行运行**：在终端进入 `RMDemo_Gripper` 目录，输入以下命令运行Python脚本：

    ```bash
    python ./src/main.py
    ```
 
3. **运行结果**：

运行脚本后，输出结果如下所示：

```
Successfully connected to the robot arm: 1

API Version: V0.3.0

movej motion succeeded
Gripper continuous force control gripping succeeded
movej motion succeeded
Gripper release succeeded
movej motion succeeded

Successfully disconnected from the robot arm
```

### 2. 代码说明

下面是 `demo_gripper.py` 文件的主要功能：

- **连接机械臂**

    ```python
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```
    连接到指定IP和端口的机械臂。

- **获取API版本**

    ```python
    print("\nAPI Version: ", rm_api_version(), "\n")
    ```
    获取并显示API版本。

- **执行movej运动**

    ```python
    robot_controller.movej([90, 90, 30, 0, 60, 0])
    ```

- **夹爪持续力夹取**

    ```python
    robot_controller.set_gripper_pick_on(500, 200)
    ```

- **执行movej运动**

    ```python
    robot_controller.movej([0, 90, 30, 0, 60, 0])
    ```

- **释放夹爪**

    ```python
    robot_controller.set_gripper_release(500)
    ```

- **执行movej运动**

    ```python
    robot_controller.movej([90, 90, 30, 0, 60, 0])
    ```

- **断开机械臂连接**

    ```python
    robot_controller.disconnect()
    ```

## 7. 许可证信息

- 本项目遵循MIT许可证。
