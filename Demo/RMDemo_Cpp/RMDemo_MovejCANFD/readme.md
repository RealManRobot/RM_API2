#  RMDemo_MovejCANFD

## **1. 项目介绍**
本项目是一个使用睿尔曼C开发包,完成工程完成读取demo下的关节角度轨迹文件，按照10ms的周期进行透传，机械臂可以稳定运行，不同型号机械臂的透传轨迹文件，注册机械臂实时状态的回调函数，透传过程中，可以实时获取机械臂当前角度。

## **2. 代码结构**
```
RMDemo_MovejCANFD
├── build              # CMake构建生成的输出目录（如Makefile、构建文件等）
├── cmake              # CMake模块和脚本的存放目录
│   ├── ...
├── data
│   └── robot_log.txt    # 日志、轨迹文件等数据文件目录（在执行过程中生成）
├── include              # 自定义头文件存放目录
├── Robotic_Arm          睿尔曼机械臂二次开发包
│   ├── include
│   │   ├── rm_define.h  # 机械臂的定义
│   │   └── rm_interface.h # 机械臂 API 的接口头文件
│   ├── lib
│   │   ├── api_c.dll    # Windows 的 API 库
│   │   ├── api_c.lib    # Windows 的 API 库
│   │   └── libapi_c.so  # Linux 的 API 库
├── src
│   ├── main.c           # 主函数
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

1. 克隆项目到本地：

   ```bash

   ```

2. 构建项目：
   Linux下：
   cmake:
   ```bash
   mkdir build
   cd build
   cmake ..
   make
   
   ```

   如果是GC编译的话 ：
   ```bash
   #!/bin/bash
    # 编译并链接
    gcc -I./include -I./Robotic_Arm/include -L./Robotic_Arm/lib -Wl,-rpath=./Robotic_Arm/lib -DDATA_FILE_PATH=\"$(pwd)/data/RM65\&RM63_canfd_data.txt\" -o RMDemo_MovejCANFD  src/main.c -lapi_c
    
    # 检查编译是否成功
    if [ $? -eq 0 ]; then
    # 设置LD_LIBRARY_PATH环境变量
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./Robotic_Arm/lib
    
    # 运行编译后的可执行文件
    ./RMDemo_MovejCANFD
    else
    echo "编译失败"
    fi
   ```


## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**

### **1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```
2. **命令行运行**：在终端进入 `RMDemo_MovejCANFD` 目录，输入以下命令运行 C程序：

2.1 Linux下
* ```bash
    chmod +x run.sh
   ./run.sh
    ```

2.2  Windows下: 双击运行 run.bat

2.3  **选择对应型号轨迹文件**：
- 在方法中`demo_movej_canfd`中：
    ```C
    void demo_movej_canfd(rm_robot_handle* handle) {
    printf("Trying to open file: %s\n", DATA_FILE_PATH);

    FILE* file = fopen(DATA_FILE_PATH, "r");
    if (!file) {
        perror("Failed to open file");
        return;
    }

    float points[MAX_POINTS][ARM_DOF];
    int point_count = 0;
    while (fscanf(file, "%f,%f,%f,%f,%f,%f,%f",
                  &points[point_count][0], &points[point_count][1], &points[point_count][2],
                  &points[point_count][3], &points[point_count][4], &points[point_count][5],
                  &points[point_count][6]) == ARM_DOF) {
        point_count++;
    }
    
    ```
    - ECO65：ECO65_canfd_data.txt
    - RM65&RML63-Ⅱ：RM65&RM63_canfd_data.txt
    - RM75：RM75_canfd_data.txt
    - DATA_FILE_PATH 为了跨平台在[CMakeLists.txt](CMakeLists.txt) 里面通过 # 将数据文件路径定义为预处理器宏
      add_definitions(-DDATA_FILE_PATH="${CMAKE_CURRENT_SOURCE_DIR}/data/RM65&RM63_canfd_data.txt")
    - 


### **2. 代码说明**

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

### **3. 运行结果示例**

运行脚本后，输出结果如下所示：

```
API Version: 0.3.0.
Robot handle created successfully: 1
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Joint positions:
0.01 -21.32 -78.51 -0.03 -80.17 0.02
Successfully set realtime push configuration.
Current state: -53.000
Current angles: 0.013 -21.323 -78.511 -0.034 -80.170 0.020
Current state: 0
Current state: 0
Error Code: 0
Arm IP: 192.168.1.18
Arm Error: 0
Joint Position:
 0.013
 -21.323
 -78.511
 -0.034
 -80.170
 0.020
Force Sensor:
  Coordinate: 888729056
System Error: 0
Waypoint:
  Euler: [3.141, 0.000, 0.000]
  Position: [0.300, -0.000, 0.299]
  Quat: [0.000, 1.000, -0.000, -0.000]
  ....
  176.12 -128.64 133.60 176.12 126.63 356.12
Pass-through completed

The motion is complete, the arm is in place.
Motion result: 1
Current device: 0
Is the next trajectory connected: 0
movej_cmd joint movement 1: 0
...
Joint positions:
-0.00 0.00 0.00 0.00 0.00 -0.00
INFO: disconnect_robot_arm: Operation successful

```
#### 2）运行脚本后，运行轨迹从上至下如下图所示：

![moveCANFD](moveCANFD.gif)


## **6. 许可证信息**

* 本项目遵循MIT许可证。

## **7. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。

- **Q:** UDP数据推送接口收不到数据？
  **A:** 检查线程模式、是否使能推送数据、IP以及防火墙

- - **Q:** Trying to open file: C:/Users/dell/Videos/710/RMDemo_MovejCANFD/data/RM65&RM63_canfd_data.txt No valid points data found in file？
    **A:** #define ARM_DOF 6 在 RMDemo_MovejCANFD\include\utils.h 下是否未定义



