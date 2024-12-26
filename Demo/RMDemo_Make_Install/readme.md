#  Ubuntu下make install示例

## **1. 项目介绍**

本项目主要介绍如何将睿尔曼api2的库安装到系统路径中以及在工程的Cmakelists文件中如何引用。

## **2. 代码结构**

```
RMDemo_Make_Install/
├── build/                   # CMake构建生成的输出目录
├── install.sh               # 睿尔曼api2库文件安装脚本
├── run.sh             		 # 安装后运行脚本
├── main.c              	 # 示例源文件(c语言)
├── main.cpp              	 # 示例源文件(c++)
├── CMakeLists.txt           # CMake配置示例文件
└── README.md                # 项目说明文档
```

## **3.项目下载**

通过链接下载 `RM_API2` 到本地：[开发包下载](https://github.com/RealManRobot/RM_API2.git)，进入`RM_API2\Demo\`目录，可找到RMDemo_Make_Install。

## **4. 环境配置**

在Windows和Linux环境下运行时需要的环境和依赖项：

| 项目      | Linux                                                 |
| :-------- | :---------------------------------------------------- |
| 系统架构  | x86架构/ARM架构                                       |
| 编译器    | GCC 7.5或更高版本                                     |
| CMake版本 | 3.10或更高版本                                        |
| 特定依赖  | RMAPI Linux版本库（位于`RM_API2/C和RM_API2/C++`目录） |

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

## **5. 使用指南**

### **5.1 快速运行**

按照以下步骤快速运行代码：

1. **将api2的库文件安装到系统路径中，在终端中运行install.sh脚本**

    ```C
    sudo ./install.sh
    ```
    
2. **linux 命令行运行**：
   在终端进入 `RMDemo_Gripper` 目录，输入以下命令运行C程序： 

   ```bash
   ./run.sh
   ```
   

### **5.2 关键代码说明**

在CmakeLists.txt中：

- **查找已经安装的api2库**
  连接到指定IP和端口的机械臂。

  ```C
  find_package(rm_api2 1.0 REQUIRED)
  ```

- **添加可执行目标**
  
  ```C
  add_executable(MyApp main.c)
  ```
  
- **链接 rm_api2 库**
  调用movej控制机械臂运动到物料所在位置

  ```C
  target_link_libraries(MyApp PRIVATE rm_api2)
  ```

## **6. 许可证信息**

- 本项目遵循MIT许可证。
