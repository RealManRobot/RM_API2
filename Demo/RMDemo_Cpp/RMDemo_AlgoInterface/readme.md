## **1. 项目介绍**
本项目是一个使用睿尔曼C++二次开发包，基于 Cmake 构建的项目，演示不连接机械臂,独立使用算法,进行算法初始化、机械臂型号设置、坐标系设置、运动学正解、运动学逆解,欧拉角转四元数、四元数转欧拉角等功能。




## **2. 代码结构**
```
RMDemo_AlgoInterface
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── cmake              # CMake模块和脚本的存放目录
│   ├── ...
├── data
├── include              # 自定义头文件存放目录
├── Robotic_Arm          睿尔曼机械臂二次开发包
│   ├── include
│   │   ├── rm_define.h  # 机械臂的定义
│   │   └── rm_interface.h # 机械臂 API 的接口头文件
│   ├── lib
│   │   ├── api_cpp.dll    # Windows 的 API 库
│   │   ├── api_cpp.lib    # Windows 的 API 库
│   │   └── libapi_cpp.so  # Linux 的 API 库
├── src
│   ├── main.cpp           # 主函数
├── CMakeLists.txt       # 项目的顶层CMake配置文件
├── readme.md            # 为示例工程提供详细的文档
├── run.bat              # 快速运行脚本， Windows为bat脚本
└── run.sh               # 快速运行脚本， linux为shell脚本
```

## **3. 系统要求**

- 操作系统：Ubuntu 18.04或更高版本
- 编译器：GCC 7.5或更高版本 (或任何其他兼容的C编译器)
- 依赖库：
  - CMake 3.10或更高版本
  - RMAPI库(包含在 `Robotic_Arm/lib`目录中)


## **4. 安装说明**

以Linux为例，项目的安装说明如下所示：
4.1. 配置环境：


- Linux 安装cmake依赖：

  ```bash
  sudo apt-get update
  sudo apt-get install build-essential
  sudo apt-get install cmake
  ```

  检查和安装依赖项：

  ```
  gcc --version
  cmake --version
  Windows 安装cmake依赖
  ```
  CMake：确保已安装最新版本的 CMake。可以从 CMake官网 下载并安装。
  编译器：安装 MinGW 或 Visual Studio (MSVC) 以进行构建。MinGW 是一个开源编译器套件，可以从 MinGW官网 下载。Visual Studio 包含 MSVC，可以从 Visual Studio官网 下载并安装。
  依赖库：
  api_cpp.dll 和 api_cpp.lib：确保这些库文件存在于 Robotic_Arm/lib 目录中。
  确保项目中的 include 目录和其他源文件路径正确设置。
  
  ```
  
  ```

4.2. 克隆项目到本地：

   ```
   
   ```

## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**
1. **参数配置**

   打开`main.c` 文件，在main函数中可修改以下配置：

  - 配置机械臂及末端版本（默认为RM65标准版机械臂）：如果需要调用其它型号机械臂的算法，可配置`rm_algorithm_init`的初始化参数。
    - `rm_robot_arm_model_e`参数指定了机械臂的型号，例如RM65机械臂则修改为：`RM_MODEL_RM_65_E`。
    - `rm_force_type_e`参数指定了机械臂末端版本，例如六维力版本则修改该参数为`rm_force_type_e Type = RM_MODEL_RM_B_E;`。
  - 配置基座安装角度（默认为正装）：通过`rm_algo_set_angle`方法设置机械臂的初始安装姿态
  - 配置工作坐标系（不设置则按照出厂默认的参数进行计算）：通过`rm_algo_set_workframe`方法修改工作坐标系。
  - 配置工具坐标系（不设置则按照出厂默认的参数进行计算）：通过`rm_algo_set_toolframe`方法修改工具坐标系。
  - 

### **1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```
2. **命令行运行**：在终端进入 `RMDemo_SimpleProcess` 目录，输入以下命令运行 C程序：

2.1 Linux下
* ```bash
    chmod +x run.sh
   ./run.sh
   ```

2.2  Windows下: 双击运行 run.bat

### **2. 代码说明**

下面是 `main.c` 文件的主要功能：
- **机械臂各型号初始化参数数组**
  
  ```c
  ArmModelData arm_data[9] = {
    {
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} }
    },
    {
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 3.14} } 
    }, 
    {

    },
    {  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} }
    },
    {

    },
    {  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f}, 
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} } 
    },
    {

    },
    {  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} } 
    },
    {  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f},  
        {{0.3, 0, 0.3}, {0,0,0,0},{3.14, 0, 0} }
    }
  };
  ```

- **手动设置工作坐标系**

    ```C
    rm_frame_t coord_work;
    coord_work.pose.position.x = 0.0f;
    coord_work.pose.position.y = 0.0f;
    coord_work.pose.position.z = 0.0f;
    coord_work.pose.quaternion.w = 0.0f;
    coord_work.pose.quaternion.x = 0.0f;
    coord_work.pose.quaternion.y = 0.0f;
    coord_work.pose.quaternion.z = 0.0f;
    coord_work.pose.euler.rx = 0.0f;
    coord_work.pose.euler.ry = 0.0f;
    coord_work.pose.euler.rz = 0.0f;
    coord_work.payload = 0.0f;
    rm_algo_set_workframe(&coord_work);
    ```
  手动设置名为 `"WorkTest"` 的工作坐标系，位姿为 `[0, 0, 0, 0, 0, 0]`。


- **逆解函数**
    ```C
    rm_inverse_kinematics_params_t inverse_params;
    float q_in_pose[6] = {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f};
    memcpy(inverse_params.q_in, q_in_joint, sizeof(q_in_joint));
    inverse_params.q_pose = arm_data[Mode].pose;
    inverse_params.flag = 1;
    result = rm_algo_inverse_kinematics(&handle, inverse_params, q_in_pose);
    ```

### **6.3. 运行结果示例**

运行脚本后，输出结果如下所示：
```
API Version: 0.3.0.
Test initialization of algorithm dependency data...
Set robot arm model to 0, sensor model to 0: Success
Installation pose set successfully
Work frame set successfully
Set work frame pose: [0.00, 0.00, 0.00]
Tool frame set successfully
Set tool frame pose: [0.00, 0.00, 0.00]
Forward kinematics calculation: Success
Joint angles: [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
End effector pose: Position(-0.00, 0.00, 0.85), Quaternion(0.00, -0.00, 0.00, 1.00), Euler angles(0.00, 0.00, 3.14)

Inverse Kinematics: [0.043802, -21.288101, -78.314949, -0.092543, -80.397034, 0.059240]
Euler to Quaternion:: [w: 0.000296, x: 1.000000, y: 0.000000, z: 0.000000]
Quaternion to Euler: [rx: 0.000000, ry: -0.000000, rz: 3.141593]
```

* **支持渠道**：

  + 开发者论坛/社区：[链接地址](https://bbs.realman-robotics.cn)
  +

- API文档：详见`rm_interface.h`文件。


## **6. 许可证信息**

* 本项目遵循MIT许可证。

## **7. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。

- **Q:** 需要连接真实机械臂吗 有啥前置条件？
  **A:** 算法接口有两种用法，一种连机械臂用、一种不连。基于这两个用法去测，连接机械臂后可以直接调用正逆解计算接口，会自动获取机械臂当前坐标系、安装角度进行计算。
- 不连接机械臂时，需要调用algo_init_sys_data以及其他其他设置坐标系等接口之后，再去计算


