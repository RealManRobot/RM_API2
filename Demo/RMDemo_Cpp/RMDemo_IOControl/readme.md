#  RMDemo_IOControl

## **1. 项目介绍**
本项目是一个使用睿尔曼C开发包, 本演示程序演示了如何使用 RM 接口库对机械臂进行 IO 控制。该程序支持 Windows 和 Linux 平台，并提供设置和控制 IO 模式和状态的功能。
演示程序包括以下功能：
- 设置 IO 模式为输入或输出
- 控制数字输出 (DO) 状态
- 检测数字输入 (DI) 状态
- 日志记录和错误处理
- 

## **2. 代码结构**
```
RMDemo_IOControl
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

- 操作系统：Ubuntu 18.04或更高版本  或 一台运行 Windows 操作系统的电脑
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
    gcc -I./Robotic_Arm/include -I./include -L./Robotic_Arm/lib -Wl,-rpath=./Robotic_Arm/lib -o RMDemo_IOControl src/main.c -lapi_c

    
    # 检查编译是否成功
    if [ $? -eq 0 ]; then
    # 设置LD_LIBRARY_PATH环境变量
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./Robotic_Arm/lib
    
    # 运行编译后的可执行文件
    ./RMDemo_IOControl
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

2. **命令行运行**：在终端进入 `RMDemo_IOControl` 目录，输入以下命令运行C程序：
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


4. **通过IO复用模式控制该轨迹文件的运行、暂停、继续、急停**

   程序运行结束后，拖动示教保存的轨迹文件已经保存到指定id的在线编程程序列表，并且设置为IO 默认运行的在线编程文件。此时，控制器IO设置为：

   	IO1：表示开始运行在线编程文件；

   	IO2：表示暂停运行在线编程文件；

   	IO3：表示继续运行在线编程文件；

   	IO4：表示急停功能；



### **6.3. 运行结果示例**


```

```



* **支持渠道**：

  + 开发者论坛/社区：[链接地址](https://bbs.realman-robotics.cn)
  + [RM 接口文档](https://bbs.realman-robotics.cn/question/323.html https://bbs.realman-robotics.cn/question/134.html)
  + [Realman 机械臂用户手册](https://bbs.realman-robotics.cn/question/117.html)
- API文档：详见`rm_interface.h`文件。


## **7. 许可证信息**

* 本项目遵循MIT许可证。

## **8. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。


  

## 控制器和末端接口图

### 控制器IO接口图1
![控制器_IO接口图1](Controller_IO_Interface_Diagram1.png)

### 控制器IO接口图2
![控制器_IO接口图2](Controller_IO_Interface_Diagram2.png)

### 末端IO接口图
![末端_IO接口图](End_Effector_IO_Interface_Diagram.png)