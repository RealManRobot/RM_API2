# 升降机控制示例

## 1. 项目介绍

本项目是一个使用睿尔曼Python开发包完成控制升降机运动到指定高度，采用非阻塞方式运行，同时控制机械臂运动到预备抓取动作，机械臂movel向前运动一段距离，控制夹爪持续力夹取，夹取到位后，机械臂movel向后运动一段距离，回到预备动作，控制升降机运动到另一高度，采用阻塞方式运行，运动到位后，机械臂movel向前运动一段距离，控制夹爪松开力夹取，夹取到位后，机械臂movel向后运动一段距离，回到预备动作。

## 2. 代码结构

```
RMDemo_Lift/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_lift.py      <- 完成控制升降机运动到指定高度，采用非阻塞方式运行，同时控制机械臂运动到预备抓取动作，机械臂movel向前运动一段距离，控制夹爪持续力夹取，夹取到位后，机械臂movel向后运动一段距离，回到预备动作，控制升降机运动到另一高度，采用阻塞方式运行，运动到位后，机械臂movel向前运动一段距离，控制夹爪松开力夹取，夹取到位后，机械臂movel向后运动一段距离，回到预备动作。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_Lift。

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

1. 安装角度必须为侧装，以及搭配升降机设备。

## **6. 使用指南**

### 1. 快速运行

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_lift.py` 文件，在 `main` 函数中修改 `RobotArmController` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```python
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```

2. **命令行运行**：在终端进入 `RMDemo_Lift` 目录，输入以下命令运行Python脚本：

    ```bash
    python ./src/main.py
    ```
3. **运行结果**：

运行脚本后，输出结果如下所示：

```
current api version:  0.2.9

Successfully connected to the robot arm: 1

API Version:  0.2.9

Change work frame:  0

Lift motion succeeded

movej_p motion succeeded

movel motion succeeded

Gripper continuous force control gripping succeeded

movel motion succeeded

Lift motion succeeded

movel motion succeeded

Gripper release succeeded

movel motion succeeded

Successfully disconnected from the robot arm
```

### 2. 代码说明

下面是 `demo_lift.py` 文件的主要功能：

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

- **切换工作坐标系**

    ```python
    ret = robot_controller.robot.rm_change_work_frame("Base")
    print("\nChange work frame: ", ret, "\n")
    ```

- **控制升降机运动**

    ```python
    robot_controller.set_lift_height(20, 500, False)
    ```

- **执行movej_p运动**

    ```python
    robot_controller.movej_p([0.1, 0, 0.7, 0, 0, 3.141])
    ```

- **执行movel运动**

    ```python
    robot_controller.movel([0.1, 0, 0.8, 0, 0, 3.141])
    ```

- **控制夹爪持续力夹取**

    ```python
    robot_controller.set_gripper_pick_on(500, 200)
    ```

- **再次执行movel运动**

    ```python
    robot_controller.movel([0.1, 0, 0.7, 0, 0, 3.141])
    ```

- **再次控制升降机运动**

    ```python
    robot_controller.set_lift_height(20, 200)
    ```

- **控制夹爪松开**

    ```python
    robot_controller.set_gripper_release(500)
    ```

- **断开机械臂连接**

    ```python
    robot_controller.disconnect()
    ```

## 7. 许可证信息

- 本项目遵循MIT许可证。
