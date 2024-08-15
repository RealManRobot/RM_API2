#  RMDemo_OnlineProgram

## **1. 项目介绍**
本项目是一个使用睿尔曼C开发包,  演示了读取demo下的在线编程文件,将文件发送给机械臂运行,并实时检测在线编程文件运行的状态、行数、循环数等信息


## **2. 代码结构**
```
RMDemo_OnlineProgram
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

    gcc -I./Robotic_Arm/include -L./Robotic_Arm/lib -Wl,-rpath=./Robotic_Arm/lib -o RMDemo_OnlineProgram src/main.c -lapi_c

    
    # 检查编译是否成功
    if [ $? -eq 0 ]; then
    # 设置LD_LIBRARY_PATH环境变量
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./Robotic_Arm/lib
    
    # 运行编译后的可执行文件
    ./RMDemo_OnlineProgram
    else
    echo "编译失败"
    fi
   ```


## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**

### **6.1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```

2. **命令行运行**：在终端进入 `RMDemo_OnlineProgram` 目录，输入以下命令运行C程序：
   2.1 Linux下
* ```bash
    chmod +x run.sh
   ./run.sh
    ```

2.2  Windows下: 双击运行 run.bat


### **6.2. 代码说明**

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

    ```C
    start_drag_teach(robot_handle, 1);
    ```
  启动拖动示教模式，参数 `1` 表示记录轨迹。

- **保存轨迹**

    ```C
    // Save the trajectory
    const char *file_path_test = "TRAJECTORY_FILE_PATH";
    int timeout = 20;  // Wait for 20 seconds
    int lines = save_trajectory(robot_handle, file_path_test, timeout);
    ```
  保存记录的轨迹到指定文件。

- **拼接在线编程文件**

    ```C
    add_lines_to_file(robot_handle, file_path_test, lines);
    ```
  将特定行添加到轨迹文件中，形成在线编程文件。

- **下发在线编程文件**

    ```C
    send_project(robot_handle, file_path_test, 20, 0, 16, 0, 0);
    ```
  将在线编程文件发送到机械臂。

- **查询在线编程运行状态**

    ```C
    get_program_run_state(robot_handle, 1, 5);
    ```
  查询在线编程的运行状态，间隔 `1` 秒，最大查询次数为 `5`。

- **暂停机械臂**

    ```C
    set_arm_pause(robot_handle);
    ```
  暂停机械臂运行。

- **继续机械臂运行**

    ```C
    set_arm_continue(robot_handle);
    ```
  继续机械臂运行。

- **断开机械臂连接**

    ```C
    disconnect_robot_arm(robot_handle);
    ```
  断开与机械臂的连接。



### **6.3. 运行结果示例**

运行脚本后，输出结果如下所示：
```
API Version: 0.2.9.
Robot handle created successfully: 1
INFO: set_arm_dof: Operation successful
Current arm_dof: 6
INFO: start_drag_teach: Operation successful
Drag teaching started
Drag teaching has started, complete the drag operation and press Enter to continue...

Drag teaching stopped
Project sent and run successfully
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
INFO: set_arm_pause: Operation successful
Robot arm paused successfully
Program running state: 2
Program running state: 2
Program running state: 2
Program running state: 2
Program running state: 2
INFO: set_arm_continue: Operation successful
Robot arm continued successfully
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1
Program running state: 1

INFO: disconnect_robot_arm: Operation successful
```

* **支持渠道**：

  + 开发者论坛/社区：[链接地址](https://bbs.realman-robotics.cn)
  +

- API文档：详见`rm_interface.h`文件。


## **7. 许可证信息**

* 本项目遵循MIT许可证。

## **8. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。

- **Q:** 发送文件不成功 在示教器上http://192.168.1.18/#/ 的【数据管理】【图形化编程】里面看不到发送的轨迹文件？
  **A:**  请参考SDK里面的接口，int only_save;      ///< 0-运行文件，1-仅保存文件，不运行 设置为非0 就可以强制保存轨迹文件到 图形化编程里面


  