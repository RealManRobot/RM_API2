# RMDemo_CoordinateSystem

---

## **1. 项目介绍**
本项目是一个使用睿尔曼C++二次开发包，基于 Cmake 构建的项目，演示工作坐标系的新建、删除、修改、查询等功能。

## **2. 代码结构**
```
RMDemo_CoordinateSystem/
├── build/                  # CMake构建生成的输出目录
├── cmake/                  # Windows下CMake构建生成的输出目录
├── include/                # 自定义头文件存放目录
├── Robotic_Arm/               睿尔曼机械臂二次开发包
│   ├── include/
│   │   ├── rm_define.h        # 机械臂二次开发包头文件，包含了定义的数据类型、结构体
│   │   └── rm_interface.h     # 机械臂二次开发包头文件，声明了机械臂所有操作接口
│   └── lib/
│       ├── api_c.dll          # Windows 64bit 的 API 库(默认，如环境为32位需手动替换库)
│       ├── api_c.lib          # Windows 64bit 的 API 库(默认，如环境为32位需手动替换库)
│       └── libapi_c.so        # Linux x86 的 API 库(默认，如环境为Linux arm架构需手动替换库)
├── src/                     # 源文件存放目录
│   └── main.c               # 主要功能的源文件
├── run.bat                  # Windows快速运行脚本
├── run.sh                   # linux快速运行脚本
├── CMakeLists.txt           # 项目的CMake配置文件
├── README.md                # 项目说明文档

```

## **3. 环境与依赖**

在Windows和Linux环境下运行时需要的环境和依赖项：
|  | Linux | Windows |
| :--: | :--: | :--: |
| 编译器 | GCC/G++ 7.5或更高版本 | MSVC2015或更高版本 |
| CMake版本 | 3.10或更高版本 | 3.10或更高版本 |
| 特定依赖 | RMAPI Linux版本库（位于`Robotic_Arm/lib`目录） | RMAPI Windows版本库（位于`Robotic_Arm/lib`目录） |

## **4. 安装说明**

1. 配置环境：


- Linux 运行环境安装
  - 可以使用apt包管理器来安装gcc和g++。打开终端并输入以下命令：

  ```bash
  sudo apt update  
  sudo apt install build-essential
  ```
  - 安装cmake依赖：

  ```bash
  sudo apt-get update
  sudo apt-get install build-essential
  sudo apt-get install cmake
  ```

  - 检查和安装依赖项：

  ```
  gcc --version
  g++ --version
  cmake --version
  ```
  - 依赖库： 
  libapi_cpp.so：确保这些库文件存在于 Robotic_Arm/lib 目录中。
  确保项目中的 include 目录和其他源文件路径正确设置。

- Windows 运行环境安装
  - 安装CMake：确保已安装最新版本的 CMake。可以从 CMake官网 下载并安装。
  - 编译器：使用MSVC编译器以进行构建。从Visual Studio官网下载Visual Studio安装工具，可选择单独安装MSVC编译器或者直接安装完整的 Visual Studio。
  - 依赖库：
  api_cpp.dll 和 api_cpp.lib：确保这些库文件存在于 Robotic_Arm/lib 目录中。
  确保项目中的 include 目录和其他源文件路径正确设置。


2. 克隆项目到本地：

   ```
   
   ```


## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。

## **6. 使用指南**

### **6.1. 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：
    打开 `main.c` 文件，在 `main` 函数中修改 `robot_ip_address` 参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```

2. **linux 命令行运行**：
    在终端进入 `RMDemo_CoordinateSystem` 目录，输入以下命令运行C程序： 
   
    ```bash
    chmod +x run.sh
    ./run.sh
    ```
    
3. **Windows 运行**： 双击run.bat脚本运行

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

- **手动设置工作坐标系**

    ```C
    const char *workFrameName = "WorkTest";
    rm_pose_t initial_pose = {.position = {0, 0, 0}, .euler = {0, 0, 0}};
    rm_set_manual_work_frame(handle, workFrameName, initial_pose);
    ```
  手动设置名为 `"WorkTest"` 的工作坐标系，位姿为 `[0, 0, 0, 0, 0, 0]`。

- **更新工作坐标系**

    ```C
    rm_pose_t updated_pose = {.position = {0.3, 0, 0.3}, .euler = {3.142, 0, 0}};
    rm_update_work_frame(handle, workFrameName, updated_pose);
    ```
  更新名为 `"WorkTest"` 的工作坐标系，位姿为 `[0.3, 0, 0.3, 3.142, 0, 0]`。

- **查询指定工作坐标系**

    ```C
    rm_get_given_work_frame(handle, workFrameName);
    ```
  查询名为 `"WorkTest"` 的工作坐标系并显示结果。

## **7. 许可证信息**

* 本项目遵循MIT许可证。

## **8. 常见问题解答（FAQ）**


- **Q:** 如何解决编译错误？
  **A:** 请确保您的编译器版本和依赖库满足系统要求，并按照安装说明重新配置环境。

- **Q:** 如何连接机器人？
  **A:** 请参考示例代码中的连接步骤，确保机器人IP地址和端口正确配置。
