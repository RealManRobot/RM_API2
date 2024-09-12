#  末端控制夹爪示例

## **1. 项目介绍**

本项目使用睿尔曼提供的机械臂C语言开发包, 模拟进行物体抓取，可以进行在固定位置抓取物体，运动到指定位置，控制夹爪持续力夹取，夹取到位后，在通过运动到放置位，并控制松开，机械臂回到初始位姿。

## **2. 代码结构**

```
RMDemo_Gripper/
├── build/                  # CMake构建生成的输出目录
├── include/                # 自定义头文件存放目录
├── Robotic_Arm/               # 睿尔曼机械臂二次开发包
│   ├── include/
│   │   ├── rm_define.h        # 机械臂二次开发包头文件，包含了定义的数据类型、结构体
│   │   └── rm_interface.h     # 机械臂二次开发包头文件，声明了机械臂所有操作接口
│   └── lib/
│       ├── api_c.dll          # Windows 64bit 的 API 库
│       ├── api_c.lib          # Windows 64bit 的 API 库
│       └── libapi_c.so        # Linux x86 的 API 库
├── src/                     # 源文件存放目录
│   └── main.c               # 主要功能的源文件
├── run.bat                  # Windows快速运行脚本
├── run.sh                   # linux快速运行脚本
├── CMakeLists.txt           # 项目的CMake配置文件
└── README.md                # 项目说明文档
```

## **3.项目下载**

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\RMDemo_C`目录，可找到RMDemo_Gripper。

## **4. 环境配置**

在Windows和Linux环境下运行时需要的环境和依赖项：

| 项目      | Linux                                          | Windows                                          |
| :-------- | :--------------------------------------------- | :----------------------------------------------- |
| 系统架构  | x86架构                                        | -                                                |
| 编译器    | GCC 7.5或更高版本                              | MSVC2015或更高版本 64bit                         |
| CMake版本 | 3.10或更高版本                                 | 3.10或更高版本                                   |
| 特定依赖  | RMAPI Linux版本库（位于`Robotic_Arm/lib`目录） | RMAPI Windows版本库（位于`Robotic_Arm/lib`目录） |

### Linux环境配置

**1. 编译器（GCC）**
在大多数Linux发行版中，GCC是默认安装的，但可能版本不是最新的。如果需要安装特定版本的GCC（如7.5或更高版本），可以使用包管理器进行安装。以Ubuntu为例，可以使用以下命令安装或更新GCC：

```bash
# 检查GCC版本
gcc --version

sudo apt update
sudo apt install gcc-7 g++-7  
```

注意：如果系统默认安装的GCC版本已满足或高于要求，则无需进行额外安装。

**2. CMake**
CMake在大多数Linux发行版中也可以通过包管理器安装。以Ubuntu为例：

```bash
sudo apt update
sudo apt install cmake

# 检查CMake版本
cmake --version
```

### Windows环境配置

**1. 编译器（MSVC2015或更高版本）**
MSVC（Microsoft Visual C++）编译器通常随Visual Studio一起安装。可以按照以下步骤安装：

1. 访问[Visual Studio官网](https://visualstudio.microsoft.com/)下载并安装Visual Studio。
2. 在安装过程中，选择“使用C++的桌面开发”工作负载，这将包括MSVC编译器。
3. 根据需要选择其他组件，如CMake（如果尚未安装）。
4. 完成安装后，打开Visual Studio命令提示符（可在开始菜单中找到），输入`cl`命令检查MSVC编译器是否安装成功。

**2. CMake**
如果Visual Studio安装过程中未包含CMake，可以单独下载并安装CMake。

1. 访问[CMake官网](https://cmake.org/download/)下载适用于Windows的安装程序。
2. 运行安装程序，按照提示进行安装。
3. 安装完成后，将CMake的bin目录添加到系统的PATH环境变量中（通常在安装过程中会询问是否添加）。
4. 打开命令提示符或PowerShell，输入`cmake --version`检查CMake是否安装成功。

## **5. 使用指南**

### **5.1 快速运行**

按照以下步骤快速运行代码：

1. **配置机械臂IP地址**：打开 `demo_gripper.c` 文件，在 `main` 函数中修改 `robot_ip_address` 类的初始化参数为当前机械臂的IP地址，默认IP地址为 `"192.168.1.18"`。

    ```C
    const char *robot_ip_address = "192.168.1.18";
    int robot_port = 8080;
    rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
    ```

2. **linux 命令行运行**：
   在终端进入 `RMDemo_Gripper` 目录，输入以下命令运行C程序： 

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   运行结果如下：

3. **Windows 运行**： 双击run.bat脚本运行
   运行结果如下：

```bash
Run...
API Version: 1.0.0.
Robot handle created successfully: 1
请按任意键继续. . .
```

运行效果如下所示：
![demo_gripper](./grippers.gif)

### **5.2 关键代码说明**

下面是 `main.c` 文件的主要功能：

- **连接机械臂**
  连接到指定IP和端口的机械臂。

  ```C
  rm_robot_handle *robot_handle = rm_create_robot_arm(robot_ip_address, robot_port);
  ```

- **设置工具端电源输出**
  设置工具端电源输出24V

  ```C
  rm_set_tool_voltage(robot_handle, 3);
  ```

- **运动到夹取起始位置**
  调用movej控制机械臂运动到物料所在位置

  ```C
  float joint_angles_start[6] = {90.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
  result = rm_movej(robot_handle, joint_angles_start, 20, 0, 0, 1);
  ```

- **控制夹爪夹取物料**
  使用力控持续夹取功能，手爪夹取速度500，力控阈值200，阻塞进行抓取，超时时间30s

  ```C
  rm_set_gripper_pick_on(robot_handle, 500, 200, true, 30);
  ```

- **放置物料到目标位置**

  ```C
  float joint_angles_end[6] = {0.0f, 90.0f, 30.0f, 0.0f, 60.0f, 0.0f};
  // Perform movej motion End
  rm_movej(robot_handle, joint_angles_end, 20, 0, 1, 0);
  
  rm_set_gripper_release(robot_handle, 500, true, 30);
  ```

- **断开机械臂连接**

  ```C
  rm_delete_robot_arm(robot_handle);
  ```

## **6. 许可证信息**

- 本项目遵循MIT许可证。
