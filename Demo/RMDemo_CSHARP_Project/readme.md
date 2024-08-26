#  RMDemo_CSHARP_Project


## **1. 简介**
本项目是一个使用Microsoft Visual Studio开发的C#项目，旨在演示在使用C#语言时如何使用睿尔曼C语言版本的二次开发包的接口进行睿尔曼机械臂的控制。本Readme文档将指导用户如何配置环境、导入库文件、设置项目属性以及编译和运行项目。

## **2. 代码结构**
```
RMDemo_CSHARP_Project
├── RM_CSHARP_Demo.sln		# 解决方案文件
├── lib		# 存放项目依赖的外部文件
│   └── api_c.dll    # Windows 的 C版本API 库（默认release 64bit）
├── data		# 存放项目所需的数据文件
│   └── demo_trajectory.txt    # 睿尔曼RM65_B机械臂的在线编程文件，在程序运行时会被读取
├── RMDemo_CSHARP_Project		# 源代码文件夹
│   ├── bin				# 存放编译后生成的可执行文件和依赖库
│   ├── obj				# 存放编译过程中生成的中间文件
│   ├── Program.cs		# 项目的主程序文件，包含了程序的入口点（Main方法）和示例Demo
│   └── RMDemo_CSHARP_Project.csproj	# C#项目文件，包含了项目的配置信息
└── readme.md            # 项目说明文档
```

## 3. 环境准备

- **Visual Studio**：
  - 安装适合C#开发的Visual Studio版本（如Visual Studio Community），推荐最新版本。
  - 在安装时，选择安装.net桌面开发。
  - 本示例运行要求使用.net 6.0以上版本
- **睿尔曼二次开发包**：下载链接


## **4. 项目步骤**

#### 新建项目

1. **创建新的C#项目**：

   - 打开Visual Studio，选择“创建新项目”。
   - 在“创建新项目”对话框中，选择C#语言的 “控制台应用”或适合你需求的C#项目类型，然后点击“下一步”。
   - 填写项目名称、位置等信息，然后点击“创建”。

2. **包含睿尔曼二次开发包库文件**：

   将睿尔曼开发包动态库文件复制到项目目录中，并设置将 DLL 复制到包含可执行文件的目录中，作为生成过程的一部分。

   - 将`api_c.dll` 文件复制到项目目录，例如放置到项目目录lib文件夹下

   ![image-20240814111938106](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20240814111938106.png)

   - 右键点击项目，选择属性打开项目属性页，选择“生成”>“事件”>“生成后事件”。
   - 在输入框中输入以下命令：

   `xcopy /y /d "..\lib\api_c.dll" "$(OutDir)"`

   ![image-20240814101222383.png](https://github.com/RealManRobot/RM_API2/blob/main/Demo/RMDemo_CSHARP_Project/image-20240814101222383.png?raw=true)

3. 调用动态库中的接口。

   下面是一个使用 `DllImport` 调用 睿尔曼C语言版本的二次开发包 中的 `rm_init` 函数的示例，其他接口调用可打开本项目查看。

   ```
   using System.Runtime.InteropServices;
   using System.Text;
   
   partial class Program
   {
   	public enum rm_thread_mode_e
       {
           RM_SINGLE_MODE_E,       // 单线程模式，单线程非阻塞等待数据返回
           RM_DUAL_MODE_E,     // 双线程模式，增加接收线程监测队列中的数据
           RM_TRIPLE_MODE_E,       // 三线程模式，在双线程模式基础上增加线程监测UDP接口数据
       }
   
       // 引入 DllImport 特性，并指定 DLL 名称 api_c.dll，
       [DllImport("api_c.dll", EntryPoint = "rm_init", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
       public static extern int rm_init(rm_thread_mode_e mode);  
     
       static void Main()  
       {  
           // 调用C语言睿尔曼机械臂开发包动态库中的 rm_init 函数  
           // 初始化为三线程模式
           _ = rm_init(rm_thread_mode_e.RM_TRIPLE_MODE_E);
       }
   }
   ```

#### 编译与运行

- 在Visual Studio中，选择“生成”菜单下的“生成解决方案”来编译项目。
- 确保没有编译错误，并且项目能够正确链接到睿尔曼库（本示例中库为64bit Release版本）。
- 选择“调试”菜单下的“开始调试”或点击工具栏上的绿色播放按钮来运行你的应用程序。


## **5. 注意事项**

该Demo以RM65-B型号机械臂为例，请根据实际情况修改代码中的数据。


## **7. 许可证信息**

* 本项目遵循MIT许可证。
