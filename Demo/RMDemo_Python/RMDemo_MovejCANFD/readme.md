# 角度透传示例

## 1. 项目介绍

本项目是一个使用睿尔曼Python开发包完成工程完成读取demo下的关节角度轨迹文件，按照10ms的周期进行透传，机械臂可以稳定运行，不同型号机械臂的透传轨迹文件，注册机械臂实时状态的回调函数，透传过程中，可以实时获取机械臂当前角度。

## 2. 代码结构

```
RMDemo_MovejCANFD/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_movej_canfd.py      <- 读取demo下的关节角度轨迹文件，按照10ms的周期进行透传，机械臂可以稳定运行，不同型号机械臂的透传轨迹文件，注册机械臂实时状态的回调函数，透传过程中，可以实时获取机械臂当前角度的示例。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_MovejCANFD。

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

1. 该Demo支持机械臂RM65、RM75、ECO65、RML63-Ⅱ；
2. 数据均只支持低跟随，不支持高跟随，高跟随需要自行规划合适轨迹。
3. UDP数据推送接口收不到数据，检查线程模式、是否使能推送数据、IP以及防火墙。

## 6. 使用指南

### 1. 快速运行

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_movej_canfd.py` 文件，在 `main` 函数中修改 `RobotArmController` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```python
    # Create a robot arm controller instance and connect to the robot arm
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```

2. **命令行运行**：在终端进入 `RMDemo_MovejCANFD` 目录，输入以下命令运行Python脚本：

    ```bash
    python ./src/main.py
    ```
   
4. **运行结果**：

运行脚本后，输出结果如下所示：

```
current api version:  0.2.9

Successfully connected to the robot arm: 1

API Version:  0.2.9

Total points: 100

Moving to point 0: [0, 0, 0, 0, 0, 0]

...

Pass-through completed

movej_cmd joint movement 1: 0

Successfully disconnected from the robot arm
```

### 2. 代码说明

下面是 `demo_movej_canfd.py` 文件的主要功能：

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

- **配置实时推送**

    ```python
    config = rm_realtime_push_config_t(1, True, 8098, 0, '192.168.1.88')
    robot_controller.robot.rm_set_realtime_push(config)
    ```

- **读取关节角度轨迹文件并进行透传**

    ```python
    robot_controller.demo_movej_canfd()
    ```

- **断开机械臂连接**

    ```python
    robot_controller.disconnect()
    ```

## 7. 许可证信息

- 本项目遵循MIT许可证。
