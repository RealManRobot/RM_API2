# 算法示例

## 1. 项目介绍

本项目是一个使用睿尔曼Python开发包完成工程完成不连接机械臂，独立使用算法，进行算法初始化、机械臂型号设置、坐标系设置，运动学正解、运动学逆解，欧拉角转四元数、四元数转欧拉角。

## 2. 代码结构

```
RMDemo_AlgoInterface/
│
├── README.md        <- 项目的核心文档
├── requirements.txt    <- 项目的依赖列表
├── setup.py        <- 项目的安装脚本
│
├── src/          <- 项目的源代码
│  ├── main.py       <- 程序的主入口
│  └── core/        <- 核心功能或业务逻辑代码
│    └── demo_algo_interface.py      <- 完成不连接机械臂，独立使用算法，进行算法初始化、机械臂型号设置、坐标系设置，运动学正解、运动学逆解，欧拉角转四元数、四元数转欧拉角。
└── Robotic_Arm/      <- 睿尔曼机械臂二次开发包
```

## 3.项目下载

    通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_Python`目录，可找到RMDemo_AlgoInterface。

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

按照以下步骤快速运行代码：

1. **参数配置**

   打开`demo_algo_interface.py` 文件，在main函数中可修改以下配置：

   - 配置机械臂及末端版本（默认为RM65标准版机械臂）：如果需要调用其它型号机械臂的算法，可配置`AlgoController`类的初始化参数。
     - `arm_model`参数指定了机械臂的型号，例如RM75机械臂则修改为：`rm_robot_arm_model_e.RM_MODEL_RM_65_E`。
     - `force_type`参数指定了机械臂末端版本，例如六维力版本则修改该参数为`rm_force_type_e.RM_MODEL_RM_SF_E`。
   - 配置基座安装角度（默认为正装）：通过`set_angle`方法设置机械臂的初始安装姿态
   - 配置工作坐标系（不设置则按照出厂默认的参数进行计算）：通过`set_workframe`方法修改工作坐标系。
   - 配置工具坐标系（不设置则按照出厂默认的参数进行计算）：通过`set_toolframe`方法修改工具坐标系。

2. **命令行运行**：

   在终端进入RMDemo_AlgoInterface目录，输入以下命令运行Python脚本：

   ```
   python ./src/main.py
   ```

3. **运行结果**：

运行脚本后，输出结果如下所示：

```
Algorithm initialized, handle ID:  0

API Version:  0.3.0 

installation pose set successfully

Work frame set successfully

Tool frame set successfully

Forward Kinematics (flag=1): [-4.2137777711559465e-08, 0.0, 0.8505000472068787, 0.0, 8.742277657347586e-08, 3.1415927410125732]

Forward Kinematics (flag=0): [-4.2137777711559465e-08, 0.0, 0.8505000472068787, 0.0, -4.371138828673793e-08, 0.0, 1.0]

Inverse Kinematics: [0.04380200430750847, -21.288101196289062, -78.31494903564453, -0.09254305809736252, -80.39703369140625, 0.05924007669091225]

Euler to Quaternion: [0.0002963105798698962, 0.9999999403953552, 0.0, 0.0]

Quaternion to Euler: [0.0, -0.0, 3.1415927410125732]
```

### **5.2 代码说明**

下面是 `demo_algo_interface.py` 文件的主要功能：
- **各型号机械臂初始化参数字典**
    ```python
    arm_models_to_points = {  
        "RM_65": [  
            rm_robot_arm_model_e.RM_MODEL_RM_65_E,
            rm_force_type_e.RM_MODEL_RM_B_E,
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 正解关节角度
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 逆解上一时刻关节角度
            [0.3, 0.0, 0.3, 3.14, 0.0, 0.0] # 逆解目标位姿
        ],  
        "RM_75": [  
            rm_robot_arm_model_e.RM_MODEL_RM_75_E,
            rm_force_type_e.RM_MODEL_RM_B_E,
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.3, 3.14, 0.0, 3.14]
        ], 
        "RML_63": [ 
            rm_robot_arm_model_e.RM_MODEL_RM_63_II_E,  
            rm_force_type_e.RM_MODEL_RM_B_E, 
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.3, 3.14, 0.0, 0.0]  
        ], 
        "ECO_65": [  
            rm_robot_arm_model_e.RM_MODEL_ECO_65_E,  
            rm_force_type_e.RM_MODEL_RM_B_E, 
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.3, 3.14, 0.0, 0.0]  
        ],
        "GEN_72": [  
            rm_robot_arm_model_e.RM_MODEL_GEN_72_E,
            rm_force_type_e.RM_MODEL_RM_B_E,
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.3, 3.14, 0.0, 0.0]
        ],
        "ECO_63": [  
            rm_robot_arm_model_e.RM_MODEL_ECO_63_E,  
            rm_force_type_e.RM_MODEL_RM_B_E, 
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.3, 3.14, 0.0, 0.0]  
        ],
    }
    ```

- **设置机械臂型号同时初始化算法**

    ```python
    # 设置机械臂型号
    arm_model = "RM_65"
    datas = arm_models_to_points.get(arm_model, [])

    arm_model = datas[0]  
    force_type = datas[1]  
    # 初始化算法
    algo_controller = AlgoController(arm_model, force_type)
    ```
    初始化算法，不连接机械臂。

- **获取API版本**

    ```python
    print("\nAPI Version: ", rm_api_version(), "\n")
    ```
    获取并显示API版本。

- **设置基座安装角度**

    ```python
    algo_controller.set_angle(0, 0, 0)
    ```
    设置基座的安装角度。

- **设置工作坐标系**

    ```python
    algo_controller.set_workframe((0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    ```
    设置工作坐标系。

- **设置工具坐标系**

    ```python
    algo_controller.set_toolframe((0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 0, 0, 0, 0)
    ```
    设置工具坐标系。

- **运动学正解**

    ```python
    algo_controller.forward_kinematics(joint, flag_eul)  # Euler angles
    algo_controller.forward_kinematics(joint, flag_qua)  # Quaternion
    ```
    使用给定的关节角度进行正向运动学计算。

- **运动学逆解**

    ```python
    algo_controller.inverse_kinematics(q_in_joint, q_in_pose, flag_eul)
    ```
    使用给定的末端位姿进行逆向运动学计算。

- **欧拉角转四元数**

    ```python
    algo_controller.euler2quaternion(eul)
    ```
    将欧拉角转换为四元数。

- **四元数转欧拉角**

    ```python
    algo_controller.quaternion2euler(qua)
    ```
    将四元数转换为欧拉角。

## 6. 许可证信息

- 本项目遵循MIT许可证。
