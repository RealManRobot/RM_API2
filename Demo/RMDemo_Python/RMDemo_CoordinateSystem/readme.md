# 坐标系操作示例

## 1. 项目介绍

本项目演示了RM65-B机械臂工作坐标系的新建、删除、修改、查询等接口的使用，实现机械臂新工作坐标系的设定。项目基于Python构建，使用了睿尔曼提供的机械臂Python语言开发包。

## 2. 代码结构

```
RMDemo_CoordinateSystem/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_coordinate_system.py      <- 演示坐标系的新建、删除、修改、查询。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_CoordinateSystem。

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

## 5. 使用指南

### 5.1 快速运行

1. **配置机械臂IP地址**：打开 `demo_coordinate_system.py` 文件，在 `main` 函数中修改 `RobotArmController` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```python
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```

2. **命令行运行**：在终端进入 `RMDemo_CoordinateSystem` 目录，输入以下命令运行Python脚本：

    ```bash
    python ./src/main.py
    ```

3. **运行结果示例及说明**

    ```python
    current api version:  0.2.9
    //API版本号
    Successfully connected to the robot arm: 1
    //机械臂连接成功
    API Version:  0.2.9 
    //API版本号
    Manually set work frame succeeded
    //
    Update work frame succeeded
    //
    Get work frame succeeded:  [0.30000001192092896, 0.0, 0.30000001192092896, 3.1419999599456787, 0.0, 0.0] 
    //
    Delete work frame succeeded
    //
    Successfully disconnected from the robot arm
    //
    ```

    **运行结果说明：**


### 5.2 关键代码说明

下面是 `demo_coordinate_system.py` 文件的主要功能：

- **连接机械臂**
连接到指定IP和端口的机械臂。

    ```python
    robot_controller = RobotArmController("192.168.1.18", 8080, 3)
    ```

- **获取API版本**
获取并显示API版本。

    ```python
    print("\nAPI Version: ", rm_api_version(), "\n")
    ```

- **手动设置工作坐标系**
手动设置名为 `"test"` 的工作坐标系，位姿为 `[0, 0, 0, 0, 0, 0]`。

    ```python
    robot_controller.set_manual_work_frame("test", [0, 0, 0, 0, 0, 0])
    ```

- **更新工作坐标系**
更新名为 `"test"` 的工作坐标系，位姿为 `[0.3, 0, 0.3, 3.142, 0, 0]`。

    ```python
    robot_controller.update_work_frame("test", [0.3, 0, 0.3, 3.142, 0, 0])
    ```

- **查询指定工作坐标系**
查询名为 `"test"` 的工作坐标系并显示结果。

    ```python
    robot_controller.get_given_work_frame("test")
    ```

- **删除工作坐标系**
删除名为 `"test"` 的工作坐标系。

    ```python
    robot_controller.delete_work_frame("test")
    ```

- **断开机械臂连接**
断开与机械臂的连接。

    ```python
    robot_controller.disconnect()
    ```

## 6. 许可证信息

- 本项目遵循MIT许可证。
