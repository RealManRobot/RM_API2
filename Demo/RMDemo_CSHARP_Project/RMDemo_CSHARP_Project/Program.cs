using System.Reflection.Metadata;
using System.Runtime.InteropServices;
using System.Text;
using static System.Runtime.CompilerServices.RuntimeHelpers;

partial class Program
{
    public const int ARM_DOF = 7;

    public enum rm_thread_mode_e
    {
        RM_SINGLE_MODE_E,       // 单线程模式，单线程非阻塞等待数据返回
        RM_DUAL_MODE_E,     // 双线程模式，增加接收线程监测队列中的数据
        RM_TRIPLE_MODE_E,       // 三线程模式，在双线程模式基础上增加线程监测UDP接口数据
    }

    public enum rm_robot_arm_model_e
    {
        RM_MODEL_RM_65_E,       // RM_65
        RM_MODEL_RM_75_E,       // RM_75
        RM_MODEL_RM_63_I_E,     // RML_63(已弃用)
        RM_MODEL_RM_63_II_E,        // RML_63
        RM_MODEL_RM_63_III_E,       // RML_63(已弃用)
        RM_MODEL_ECO_65_E,      // ECO_65
        RM_MODEL_ECO_62_E,      // ECO_62
        RM_MODEL_GEN_72_E,      // GEN_72
        RM_MODEL_ECO_63_E       // ECO63
    }

    public enum rm_force_type_e
    {
        RM_MODEL_RM_B_E,    // 标准版
        RM_MODEL_RM_ZF_E,   // 一维力版
        RM_MODEL_RM_SF_E,   // 六维力版 
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_robot_info_t
    {
        public int ArmDof; // 机械臂自由度  
        public rm_robot_arm_model_e ArmModel; // 机械臂型号  
        public rm_force_type_e ForceType; // 末端力传感器版本  
    }

    // 事件类型  
    public enum rm_event_type_e
    {
        RM_NONE_EVENT_E,
        RM_CURRENT_TRAJECTORY_STATE_E,
        RM_PROGRAM_RUN_FINISH_E
    }

    // 机械臂当前规划类型  
    public enum rm_arm_current_trajectory_e
    {
        RM_NO_PLANNING_E,
        RM_JOINT_SPACE_PLANNING_E,
        RM_CARTESIAN_LINEAR_PLANNING_E,
        RM_CARTESIAN_ARC_PLANNING_E,
        RM_TRAJECTORY_REPLAY_PLANNING_E
    }

    // 设备类型枚举  
    public enum rm_device_type_e
    {
        RM_DEVICE_JOINT_E,         // 关节  
        RM_DEVICE_GRIPPER_E,       // 夹爪  
        RM_DEVICE_DEXTEROUS_HAND_E, // 灵巧手  
        RM_DEVICE_LIFTER_E,        // 升降机构  
        RM_DEVICE_EXTENDED_JOINT_E, // 扩展关节  
        RM_DEVICE_RESERVED_E       // 其他：保留  
    }

    // 事件信息  
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_event_push_data_t
    {
        public int handle_id;
        public rm_event_type_e event_type;
        public bool trajectory_state;
        public rm_device_type_e device; 
        public int trajectory_connect; 
        public int program_id;
    }
    // 机械臂主动上报自定义项
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_udp_custom_config_t
    {
        public int joint_speed;   ///< 关节速度。1：上报；0：关闭上报；-1：不设置，保持之前的状态
        public int lift_state;    ///< 升降关节信息。1：上报；0：关闭上报；-1：不设置，保持之前的状态
        public int expand_state;  ///< 扩展关节信息（升降关节和扩展关节为二选一，优先显示升降关节）1：上报；0：关闭上报；-1：不设置，保持之前的状态
    }

    // 机械臂主动上报接口配置  
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_realtime_push_config_t
    {
        public int cycle; // 广播周期  
        public bool enable; // 使能  
        public int port; // 广播的端口号  
        public int force_coordinate; // 系统外受力数据的坐标系  
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 28)] 
        public string ip; // 自定义的上报目标IP地址  
        public rm_udp_custom_config_t custom_config;    // 自定义项内容
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_quat_t
    {
        public float w;
        public float x;
        public float y;
        public float z;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_position_t
    {
        public float x; // 单位：m  
        public float y;
        public float z;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_euler_t
    {
        public float rx; // 单位：rad  
        public float ry;
        public float rz;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_pose_t
    {
        public rm_position_t position;     // 位置，单位：m  
        public rm_quat_t quaternion;       // 四元数  
        public rm_euler_t euler;           // 欧拉角，单位：rad 

        public override string ToString()
        {
            // 使用StringBuilder来构建字符串，因为它在处理大量字符串连接时更高效  
            StringBuilder sb = new StringBuilder();
            sb.AppendLine();
            sb.AppendFormat("  position: {0}, {1}, {2}", position.x, position.y, position.z);
            sb.AppendLine(); // AppendFormat 不包含换行，所以需要手动添加  
            sb.AppendFormat("  quaternion: {0}, {1}, {2}, {3}", quaternion.w, quaternion.x, quaternion.y, quaternion.z);
            sb.AppendLine();
            sb.AppendFormat("  euler: {0}, {1}, {2}", euler.rx, euler.ry, euler.rz);
            sb.AppendLine(); // 最后一行也添加换行，以保持格式一致  

            return sb.ToString();
        }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_frame_name_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public byte[] name;

        // 提供一个辅助属性来方便地将byte数组转换为string  
        public string NameAsString
        {
            get
            {
                return System.Text.Encoding.ASCII.GetString(name).TrimEnd('\0');
            }
            set
            {
                var bytes = System.Text.Encoding.ASCII.GetBytes(value);
                Array.Copy(bytes, name, Math.Min(bytes.Length, name.Length));
                // 填充剩余的空间为null字符（如果需要）  
                for (int i = bytes.Length; i < name.Length; i++)
                {
                    name[i] = 0;
                }
            }
        }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)] // 根据需要调整对齐方式  
    public struct rm_frame_t
    {
        public rm_frame_name_t frame_name;    // 坐标系名称  
        public rm_pose_t pose;              // 坐标系位姿  
        public float payload;             // 坐标系末端负载重量，单位：kg  
        public float x;                   // 坐标系末端负载质心位置，单位：m  
        public float y;                   // 坐标系末端负载质心位置，单位：m  
        public float z;                   // 坐标系末端负载质心位置，单位：m  
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_ctrl_version_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        public byte[] build_time; // 编译时间  

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public byte[] version; // 版本号  

        // 提供辅助方法将byte数组转换为string  
        public string BuildTimeAsString => System.Text.Encoding.UTF8.GetString(build_time).TrimEnd('\0');
        public string VersionAsString => System.Text.Encoding.UTF8.GetString(version).TrimEnd('\0');
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_dynamic_version_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 5)]
        public byte[] model_version; // 动力学模型版本号  

        public string ModelVersionAsString => System.Text.Encoding.UTF8.GetString(model_version).TrimEnd('\0');
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_planinfo_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        public byte[] build_time; // 编译时间  

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public byte[] version; // 版本号  

        // 提供辅助方法将byte数组转换为string  
        public string BuildTimeAsString => System.Text.Encoding.UTF8.GetString(build_time).TrimEnd('\0');
        public string VersionAsString => System.Text.Encoding.UTF8.GetString(version).TrimEnd('\0');
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_algorithm_version_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        public byte[] version; // 算法库版本号  

        public string VersionAsString => System.Text.Encoding.UTF8.GetString(version).TrimEnd('\0');
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_arm_software_version_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public byte[] product_version; // 机械臂型号  

        public rm_algorithm_version_t algorithm_info; // 算法库信息  
        public rm_ctrl_version_t ctrl_info; // ctrl 层软件信息  
        public rm_dynamic_version_t dynamic_info; // 动力学版本  
        public rm_planinfo_t plan_info; // plan 层软件信息  

        // 提供辅助方法将byte数组转换为string  
        public string ProductVersionAsString => System.Text.Encoding.UTF8.GetString(product_version).TrimEnd('\0');
    }


    [StructLayout(LayoutKind.Sequential, Pack = 8)] // 根据需要调整对齐方式  
    public struct rm_current_arm_state_t
    {
        public rm_pose_t pose; // 机械臂当前位姿  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint; // 机械臂当前关节角度  
        public byte arm_err; // 机械臂错误代码  
        public byte sys_err; // 控制器错误代码  
    }

    public struct rm_joint_status_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_current;               // 关节电流，单位mA  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public byte[] joint_en_flag;                // 当前关节使能状态  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public ushort[] joint_err_code;             // 当前关节错误码  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_position;              // 关节角度，单位°  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_temperature;           // 当前关节温度，单位℃  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_voltage;               // 当前关节电压，单位V  

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();

            // Joint Current  
            sb.AppendLine();
            sb.AppendLine("  Joint Current (mA):");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1:F2} mA\n", i + 1, joint_current[i]);
            }

            // Joint Enable Flag  
            sb.AppendLine("  Joint Enable Flag:");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1}\n", i + 1, joint_en_flag[i]);
            }

            // Joint Error Code  
            sb.AppendLine("  Joint Error Code:");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1}\n", i + 1, joint_err_code[i]);
            }

            // Joint Position  
            sb.AppendLine("  Joint Position (°):");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1:F2} °\n", i + 1, joint_position[i]);
            }

            // Joint Temperature  
            sb.AppendLine("  Joint Temperature (℃):");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1:F2} ℃\n", i + 1, joint_temperature[i]);
            }

            // Joint Voltage  
            sb.AppendLine("  Joint Voltage (V):");
            for (int i = 0; i < ARM_DOF; i++)
            {
                sb.AppendFormat("    Joint {0}: {1:F2} V\n", i + 1, joint_voltage[i]);
            }

            return sb.ToString();
        }
    }

    public enum rm_pos_teach_type_e
    {
        RM_X_DIR_E,        // 位置示教，x轴方向  
        RM_Y_DIR_E,        // 位置示教，y轴方向  
        RM_Z_DIR_E         // 位置示教，z轴方向  
    }

    public enum rm_ort_teach_type_e
    {
        RM_RX_ROTATE_E,    // 姿态示教，绕x轴旋转  
        RM_RY_ROTATE_E,    // 姿态示教，绕y轴旋转  
        RM_RZ_ROTATE_E     // 姿态示教，绕z轴旋转  
    }

    public struct rm_arm_all_state_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_current;           // 关节电流，单位mA  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public int[] joint_en_flag;            // 关节使能状态  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_temperature;       // 关节温度,单位℃  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint_voltage;           // 关节电压，单位V  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public int[] joint_err_code;            // 关节错误码  
        public int sys_err;                     // 机械臂错误代码  

    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_wifi_net_t
    {
        public int channel;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 16)]
        public string ip;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 18)]
        public string mac;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 16)]
        public string mask;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 5)]
        public string mode;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 16)]
        public string password;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
        public string ssid;
    }


    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_gripper_state_t
    {
        public int enable_state;
        public int status;
        public int error;
        public int mode;
        public int current_force;
        public int temperature;
        public int actpos;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_force_data_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] force_data;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] zero_force_data;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] work_zero_force_data;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] tool_zero_force_data;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fz_data_t
    {
        public float Fz;
        public float zero_Fz;
        public float work_zero_Fz;
        public float tool_zero_Fz;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_peripheral_read_write_params_t
    {
        public int port;
        public int address;
        public int device;
        public int num;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_expand_state_t
    {
        public int pos;
        public int current;
        public int err_flag;
        public int mode;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_send_project_t
    {
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 300)] // 使用MarshalAs属性来确保字符串的固定大小  
        public string project_path;      // 下发文件路径文件名
        public int project_path_len;   // 名称长度
        public int plan_speed;     // 规划速度比例系数
        public int only_save;      // 0-运行文件，1-仅保存文件，不运行
        public int save_id;        // 保存到控制器中的编号
        public int step_flag;      // 设置单步运行方式模式，1-设置单步模式 0-设置正常运动模式
        public int auto_start;     // 设置默认在线编程文件，1-设置默认  0-设置非默认
        public int project_type;           // 下发文件类型。0-在线编程文件，1-拖动示教轨迹文件
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_trajectory_data_t
    {
        public int id;     // 在线编程文件id
        public int size;   // 文件大小
        public int speed;  // 默认运行速度
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)] // 使用MarshalAs属性来确保字符串的固定大小  
        public string trajectory_name;   // 文件名称
    }


    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_program_trajectorys_t
    {
        public int page_num;       // 页码
        public int page_size;       // 每页大小
        public int list_size;   //返回总数量
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 32)]
        public string vague_search;  // 模糊搜索
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 100)]
        public rm_trajectory_data_t trajectory_list;   // 符合的在线编程列表
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_program_run_state_t
    {
        public int run_state;  // 运行状态 0 未开始 1运行中 2暂停中
        public int id;         // 运行轨迹编号
        public int edit_id;    // 上次编辑的在线编程编号 id
        public int plan_num;   // 运行到的行数
        public int total_loop;     // 循环指令数量
        public int step_mode;      // 单步模式，1 为单步模式，0 为非单步模式
        public int plan_speed;     // 全局规划速度比例 1-100
        public int[] loop_num;        // 循环指令行数
        public int[] loop_cont;       // 循环指令行数对应的运行次数
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_waypoint_t
    {
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 20)]
        public char[] point_name;    // 路点名称
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] joint;   // 关节角度
        public rm_pose_t pose;     // 位姿信息
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] work_frame;    // 工作坐标系名称
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] tool_frame;    // 工具坐标系名称
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public char[] time;      //  路点新增或修改时间
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_waypoint_list_t
    {
        public int page_num;       // 页码
        public int page_size;      // 每页大小
        public int total_size;     // 列表长度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] vague_search;  // 模糊搜索 
        public int list_len;       // 返回符合的全局路点列表长度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100)]
        public rm_waypoint_t[] points_list;   // 返回符合的全局路点列表
    }


    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_config_cube_t
    {
        public float x_min_limit;      // 长方体基于世界坐标系 X 方向最小位置，单位 m
        public float x_max_limit;      // 长方体基于世界坐标系 X 方向最大位置，单位 m
        public float y_min_limit;      // 长方体基于世界坐标系 Y 方向最小位置，单位 m
        public float y_max_limit;      // 长方体基于世界坐标系 Y 方向最大位置，单位 m
        public float z_min_limit;      // 长方体基于世界坐标系 Z 方向最小位置，单位 m
        public float z_max_limit;      // 长方体基于世界坐标系 Z 方向最大位置，单位 m
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_config_plane_t
    {
        public float x1, y1, z1;       // 点面矢量平面三点法中的第一个点坐标，单位 m
        public float x2, y2, z2;       // 点面矢量平面三点法中的第二个点坐标，单位 m
        public float x3, y3, z3;       // 点面矢量平面三点法中的第三个点坐标，单位 m
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_config_sphere_t
    {
        public float x;        // 表示球心在世界坐标系 X 轴的坐标，单位 m
        public float y;        // 表示球心在世界坐标系 Y 轴的坐标，单位 m
        public float z;        // 表示球心在世界坐标系 Z 轴的坐标，单位 m
        public float radius;       // 表示半径，单位 m
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_config_t
    {
        public int form;       // 形状，1 表示长方体，2 表示点面矢量平面，3 表示球体
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] name;  // 电子围栏名称，不超过 10 个字节，支持字母、数字、下划线
        public rm_fence_config_cube_t cube;    // 长方体参数
        public rm_fence_config_plane_t plan;    // 点面矢量平面参数
        public rm_fence_config_sphere_t sphere;    // 球体参数
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_names_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] name;    // 几何模型名称,不超过10个字符
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_fence_config_list_t
    {
        // 使用Marshal.SizeOf来计算rm_fence_config_t的大小，并乘以10  
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public rm_fence_config_t[] config;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_envelopes_ball_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] name;            // 工具包络球体的名称，1-10 个字节，支持字母数字下划线
        public float radius;           // 工具包络球体的半径，单位 0.001m
        public float x;        // 工具包络球体球心基于末端法兰坐标系的 X 轴坐标，单位 m
        public float y;        // 工具包络球体球心基于末端法兰坐标系的 Y 轴坐标，单位 m
        public float z;        // 工具包络球体球心基于末端法兰坐标系的 Z 轴坐标，单位 m
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_envelope_balls_list_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 5)]
        public rm_envelopes_ball_t[] balls;// 包络参数列表，每个工具最多支持 5 个包络球，可以没有包络
        public int size;   // 包络球数量
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 12)]
        public char[] tool_name;// 控制器中已存在的工具坐标系名称，如果不存在该字段，则为临时设置当前包络参数
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_electronic_fence_enable_t
    {
        public bool enable_state;  // 电子围栏/虚拟墙使能状态，true 代表使能，false 代表禁使能
        public int in_out_side;    // 0-机器人在电子围栏/虚拟墙内部，1-机器人在电子围栏外部
        public int effective_region;   // 0-电子围栏针对整臂区域生效，1-虚拟墙针对末端生效
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_force_sensor_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] force;         // 当前力传感器原始数据，0.001N或0.001Nm
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public float[] zero_force;        // 当前力传感器系统外受力数据，0.001N或0.001Nm
        public int coordinate;         // 系统外受力数据的坐标系，0为传感器坐标系 1为当前工作坐标系 2为当前工具坐标系
    }


    /***
     * 扩展关节数据
     *
     */
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_udp_expand_state_t
    {
        public float pos;            ///< 当前角度  精度 0.001°，单位：°
        public int current;        ///< 当前驱动电流，单位：mA，精度：1mA
        public int err_flag;       ///< 驱动错误代码，错误代码类型参考关节错误代码
        public int en_flag;        ///< 当前关节使能状态 ，1 为上使能，0 为掉使能
        public int joint_id;       ///< 关节id号
        public int mode;           ///< 当前升降状态，0-空闲，1-正方向速度运动，2-正方向位置运动，3-负方向速度运动，4-负方向位置运动
    }

    /***
     * 升降机构状态
     *
     */
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_udp_lift_state_t
    {
        public int height;         ///< 当前升降机构高度，单位：mm，精度：1mm
        public float pos;            ///< 当前角度  精度 0.001°，单位：°
        public int current;        ///< 当前驱动电流，单位：mA，精度：1mA
        public int err_flag;       ///< 驱动错误代码，错误代码类型参考关节错误代码
        public int en_flag;        ///< 当前关节使能状态 ，1 为上使能，0 为掉使能
    } 

    /***
     * 灵巧手状态
     *
     */
    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_udp_hand_state_t
    {
        public int hand_pos;         ///< 表示灵巧手自由度大小，0-1000，无量纲
        public float hand_force;            ///< 表示灵巧手自由度电流，单位mN
        public int hand_state;        ///< 表示灵巧手自由度状态
        public int hand_err;       ///< 表示灵巧手系统错误
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_realtime_arm_joint_state_t
    {
        public int errCode;        // 数据解析错误码，-3为数据解析错误，代表推送的数据不完整或格式不正确
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public char[] arm_ip;       // 推送数据的机械臂的IP地址
        public ushort arm_err;       // 机械臂错误码
        public rm_joint_status_t joint_status;     // 关节状态
        public rm_force_sensor_t force_sensor;       // 力数据（六维力或一维力版本支持）
        public ushort sys_err;       // 系统错误码
        public rm_pose_t waypoint;         // 当前路点信息
        rm_udp_lift_state_t liftState;      // 升降关节数据
        rm_udp_expand_state_t expandState;      // 扩展关节数据
        rm_udp_hand_state_t hand_state;         // 灵巧手状态
        public override string ToString()
        {
            // 将IP地址转换为字符串  
            string ipAddress = new string(arm_ip).TrimEnd('\0'); // 移除末尾的null字符  

            // 使用StringBuilder来构建字符串，因为它在处理大量字符串连接时更高效  
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("rm_realtime_arm_joint_state_t:");
            sb.AppendLine("  errCode: " + errCode);
            sb.AppendLine("  arm_ip: " + ipAddress);
            sb.AppendLine("  arm_err: " + arm_err);
            sb.AppendLine("  sys_err: " + sys_err);

            sb.AppendLine("  waypoint: " + waypoint.ToString());
            sb.AppendLine("  joint_status: " + joint_status.ToString());
            return sb.ToString();
        }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_inverse_kinematics_params_t
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public float[] q_in;   // 上一时刻关节角度，单位°
        public rm_pose_t q_pose;      // 目标位姿
        public byte flag;           // 姿态参数类别：0-四元数；1-欧拉角
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_matrix_t
    {
        public short irow;
        public short iline;
        public float[,] data;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 8)]
    public struct rm_robot_handle
    {
        public int id;
    }
    // 不使用如下修饰，会导致C#在调用完后，释放pData内容，导致C程序崩溃；所以在声明代理的时候，说明是C回调，不会收里面资源 
    [System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute(System.Runtime.InteropServices.CallingConvention.Cdecl)]
    public delegate void CallbackDelegate(int handler, int nKey, [MarshalAs(UnmanagedType.LPArray, SizeConst = 1024)] char[] sData, int len);

    [DllImport("api_c.dll", EntryPoint = "rm_api_version", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern IntPtr rm_api_version();

    // 暂不支持自定义日志回调函数，可传入null使用默认日志函数
    [DllImport("api_c.dll", EntryPoint = "rm_set_log_call_back", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_set_log_call_back(CallbackDelegate? log, int level);

    [DllImport("api_c.dll", EntryPoint = "rm_init", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_init(rm_thread_mode_e mode);

    [DllImport("api_c.dll", EntryPoint = "rm_destory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_destory();

    // 创建连接句柄，IntPtr代替指针类型
    [DllImport("api_c.dll", EntryPoint = "rm_create_robot_arm", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern IntPtr rm_create_robot_arm([MarshalAs(UnmanagedType.LPStr)] string ip, int arm_prot);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_robot_arm", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_robot_arm(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_run_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_run_mode(IntPtr handle, ref int mode);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_run_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_run_mode(IntPtr handle, int mode);

    [DllImport("api_c.dll", EntryPoint = "rm_get_robot_info", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_robot_info(IntPtr handle, ref rm_robot_info_t robot_info);

    // 定义回调函数的委托类型
    [System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute(System.Runtime.InteropServices.CallingConvention.Cdecl)]
    public delegate void rm_event_callback_ptr(rm_event_push_data_t data);

    [DllImport("api_c.dll", CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_get_arm_event_call_back(rm_event_callback_ptr event_callback);

    // 定义回调函数的委托类型
    [System.Runtime.InteropServices.UnmanagedFunctionPointerAttribute(System.Runtime.InteropServices.CallingConvention.Cdecl)]
    public delegate void rm_realtime_arm_state_callback_delegate(rm_realtime_arm_joint_state_t data);

    [DllImport("api_c.dll", EntryPoint = "rm_realtime_arm_state_call_back", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_realtime_arm_state_call_back(rm_realtime_arm_state_callback_delegate realtime_callback);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_max_speed(IntPtr handle, int joint_num, float max_speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_max_acc(IntPtr handle, int joint_num, float max_acc);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_min_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_min_pos(IntPtr handle, int joint_num, float min_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_max_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_max_pos(IntPtr handle, int joint_num, float max_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_drive_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_drive_max_speed(IntPtr handle, int joint_num, float max_speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_drive_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_drive_max_acc(IntPtr handle, int joint_num, float max_acc);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_drive_min_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_drive_min_pos(IntPtr handle, int joint_num, float min_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_drive_max_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_drive_max_pos(IntPtr handle, int joint_num, float max_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_en_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_en_state(IntPtr handle, int joint_num, int en_state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_zero_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_zero_pos(IntPtr handle, int joint_num);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_clear_err", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_clear_err(IntPtr handle, int joint_num);

    [DllImport("api_c.dll", EntryPoint = "rm_auto_set_joint_limit", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_auto_set_joint_limit(IntPtr handle, int limit_mode);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_max_speed(IntPtr handle, [In, Out] float[] max_speed);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_max_acc(IntPtr handle, [In, Out] float[] max_acc);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_min_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_min_pos(IntPtr handle, [In, Out] float[] min_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_max_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_max_pos(IntPtr handle, [In, Out] float[] max_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_drive_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_drive_max_speed(IntPtr handle, [In, Out] float[] max_speed);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_drive_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_drive_max_acc(IntPtr handle, [In, Out] float[] max_acc);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_drive_min_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_drive_min_pos(IntPtr handle, [In, Out] float[] min_pos);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_drive_max_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_drive_max_pos(IntPtr handle, [In, Out] float[] max_pos);

    [DllImport("api_c.dll", CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_en_state(IntPtr handle, [In, Out] byte[] state);

    [DllImport("api_c.dll", CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_err_flag(IntPtr handle, [In, Out] UInt16[] state, [In, Out] UInt16[] bstate);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_max_line_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_max_line_speed(IntPtr handle, float speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_max_line_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_max_line_acc(IntPtr handle, float acc);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_max_angular_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_max_angular_speed(IntPtr handle, float speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_max_angular_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_max_angular_acc(IntPtr handle, float acc);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_tcp_init", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_tcp_init(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_collision_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_collision_state(IntPtr handle, int collision_stage);

    [DllImport("api_c.dll", EntryPoint = "rm_get_collision_stage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_collision_stage(IntPtr handle, ref int collision_stage);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_max_line_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_max_line_speed(IntPtr handle, ref float speed);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_max_line_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_max_line_acc(IntPtr handle, ref float acc);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_max_angular_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_max_angular_speed(IntPtr handle, ref float speed);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_max_angular_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_max_angular_acc(IntPtr handle, ref float acc);

    [DllImport("api_c.dll", EntryPoint = "rm_set_auto_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_auto_tool_frame(IntPtr handle, int point_num);

    [DllImport("api_c.dll", EntryPoint = "rm_generate_auto_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_generate_auto_tool_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, float payload, float x, float y, float z);

    [DllImport("api_c.dll", EntryPoint = "rm_set_manual_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_manual_tool_frame(IntPtr handle, rm_frame_t frame);

    [DllImport("api_c.dll", EntryPoint = "rm_change_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_change_tool_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string tool_name);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_tool_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string tool_name);

    [DllImport("api_c.dll", EntryPoint = "rm_update_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_update_tool_frame(IntPtr handle, rm_frame_t frame);

    [DllImport("api_c.dll", EntryPoint = "rm_get_total_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_total_tool_frame(IntPtr handle, ref rm_frame_name_t frame_names, ref int len);

    [DllImport("api_c.dll", EntryPoint = "rm_get_given_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_given_tool_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, ref rm_frame_t frame);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_tool_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_tool_frame(IntPtr handle, ref rm_frame_t tool_frame);

    [DllImport("api_c.dll", EntryPoint = "rm_set_tool_envelope", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_tool_envelope(IntPtr handle, rm_envelope_balls_list_t envelope);

    [DllImport("api_c.dll", EntryPoint = "rm_get_tool_envelope", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_tool_envelope(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string tool_name, ref rm_envelope_balls_list_t envelope);

    [DllImport("api_c.dll", EntryPoint = "rm_set_auto_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_auto_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string workname, int point_num);

    [DllImport("api_c.dll", EntryPoint = "rm_set_manual_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_manual_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string work_name, rm_pose_t pose);

    [DllImport("api_c.dll", EntryPoint = "rm_change_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_change_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string work_name);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string work_name);

    [DllImport("api_c.dll", EntryPoint = "rm_update_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_update_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string work_name, rm_pose_t pose);

    [DllImport("api_c.dll", EntryPoint = "rm_get_total_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_total_work_frame(IntPtr handle, ref rm_frame_name_t frame_names, ref int len);

    [DllImport("api_c.dll", EntryPoint = "rm_get_given_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_given_work_frame(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, ref rm_pose_t pose);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_work_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_work_frame(IntPtr handle, ref rm_frame_t work_frame);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_arm_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_arm_state(IntPtr handle, ref rm_current_arm_state_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_joint_temperature", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_joint_temperature(IntPtr handle, [In, Out] float[] temperature);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_joint_current", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_joint_current(IntPtr handle, [In, Out] float[] current);

    [DllImport("api_c.dll", EntryPoint = "rm_get_current_joint_voltage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_current_joint_voltage(IntPtr handle, [In, Out] float[] voltage);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_degree", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_degree(IntPtr handle, [In, Out] float[] joint);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_all_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_all_state(IntPtr handle, ref rm_arm_all_state_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_init_pose", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_init_pose(IntPtr handle, [In, Out] float[] joint);

    [DllImport("api_c.dll", EntryPoint = "rm_get_init_pose", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_init_pose(IntPtr handle, [In, Out] float[] joint);

    [DllImport("api_c.dll", EntryPoint = "rm_movej", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movej(IntPtr handle, [In, Out] float[] joint, int v, int r, int trajectory_connect, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_movel", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movel(IntPtr handle, rm_pose_t pose, int v, int r, int trajectory_connect, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_movec", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movec(IntPtr handle, rm_pose_t pose_via, rm_pose_t pose_to, int v, int r, int loop, int trajectory_connect, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_movej_p", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movej_p(IntPtr handle, rm_pose_t pose, int v, int r, int trajectory_connect, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_movej_canfd", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movej_canfd(IntPtr handle, [In, Out] float[] joint, bool follow, float expand);

    [DllImport("api_c.dll", EntryPoint = "rm_movep_canfd", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_movep_canfd(IntPtr handle, rm_pose_t pose, bool follow);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_slow_stop", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_slow_stop(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_stop", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_stop(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_pause", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_pause(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_continue", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_continue(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_delete_current_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_delete_current_trajectory(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_delete_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_delete_trajectory(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_current_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_current_trajectory(IntPtr handle, ref rm_arm_current_trajectory_e type, [In, Out] float[] data);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_step", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_step(IntPtr handle, int joint_num, float step, int v, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_set_pos_step", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_pos_step(IntPtr handle, rm_pos_teach_type_e type, float step, int v, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_set_ort_step", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_ort_step(IntPtr handle, rm_ort_teach_type_e type, float step, int v, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_set_teach_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_teach_frame(IntPtr handle, int frame_type);

    [DllImport("api_c.dll", EntryPoint = "rm_get_teach_frame", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_teach_frame(IntPtr handle, ref int frame_type);

    [DllImport("api_c.dll", EntryPoint = "rm_set_joint_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_joint_teach(IntPtr handle, int joint_num, int direction, int v);

    [DllImport("api_c.dll", EntryPoint = "rm_set_pos_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_pos_teach(IntPtr handle, rm_pos_teach_type_e type, int direction, int v);

    [DllImport("api_c.dll", EntryPoint = "rm_set_ort_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_ort_teach(IntPtr handle, rm_ort_teach_type_e type, int direction, int v);

    [DllImport("api_c.dll", EntryPoint = "rm_set_stop_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_stop_teach(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_controller_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_controller_state(IntPtr handle, ref float voltage, ref float current, ref float temperature, ref int err_flag);

    [DllImport("api_c.dll", EntryPoint = "rm_set_arm_power", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_arm_power(IntPtr handle, int arm_power);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_power_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_power_state(IntPtr handle, ref int power_state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_system_runtime", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_system_runtime(IntPtr handle, ref int day, ref int hour, ref int min, ref int sec);

    [DllImport("api_c.dll", EntryPoint = "rm_clear_system_runtime", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_clear_system_runtime(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_odom", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_odom(IntPtr handle, [In, Out] float[] joint_odom);

    [DllImport("api_c.dll", EntryPoint = "rm_clear_joint_odom", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_clear_joint_odom(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_NetIP", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_NetIP(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string ip);

    [DllImport("api_c.dll", EntryPoint = "rm_clear_system_err", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_clear_system_err(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_arm_software_info", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_arm_software_info(IntPtr handle, ref rm_arm_software_version_t software_info);

    [DllImport("api_c.dll", EntryPoint = "rm_get_controller_RS485_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_controller_RS485_mode(IntPtr handle, ref int mode, ref int baudrate, ref int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_get_tool_RS485_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_tool_RS485_mode(IntPtr handle, ref int mode, ref int baudrate, ref int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_get_joint_software_version", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_joint_software_version(IntPtr handle, ref int version);

    [DllImport("api_c.dll", EntryPoint = "rm_get_tool_software_version", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_tool_software_version(IntPtr handle, ref int version);

    [DllImport("api_c.dll", EntryPoint = "rm_set_wifi_ap", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_wifi_ap(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string wifi_name, [MarshalAs(UnmanagedType.LPStr)] string password);

    [DllImport("api_c.dll", EntryPoint = "rm_set_wifi_sta", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_wifi_sta(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string router_name, [MarshalAs(UnmanagedType.LPStr)] string password);

    [DllImport("api_c.dll", EntryPoint = "rm_set_RS485", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_RS485(IntPtr handle, int baudrate);

    [DllImport("api_c.dll", EntryPoint = "rm_get_wired_net", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_wired_net(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string ip, [MarshalAs(UnmanagedType.LPStr)] string mask, [MarshalAs(UnmanagedType.LPStr)] string mac);

    [DllImport("api_c.dll", EntryPoint = "rm_get_wifi_net", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_wifi_net(IntPtr handle, ref rm_wifi_net_t wifi_net);

    [DllImport("api_c.dll", EntryPoint = "rm_set_net_default", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_net_default(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_wifi_close", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_wifi_close(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_IO_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_IO_mode(IntPtr handle, int io_num, int io_mode);

    [DllImport("api_c.dll", EntryPoint = "rm_set_DO_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_DO_state(IntPtr handle, int io_num, int state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_IO_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_IO_state(IntPtr handle, int io_num, ref int state, ref int mode);

    [DllImport("api_c.dll", EntryPoint = "rm_get_IO_input", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_IO_input(IntPtr handle, ref int DI_state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_IO_output", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_IO_output(IntPtr handle, ref int DO_state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_voltage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_voltage(IntPtr handle, int voltage_type);

    [DllImport("api_c.dll", EntryPoint = "rm_get_voltage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_voltage(IntPtr handle, ref int voltage_type);

    [DllImport("api_c.dll", EntryPoint = "rm_set_tool_DO_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_tool_DO_state(IntPtr handle, int io_num, int state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_tool_IO_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_tool_IO_mode(IntPtr handle, int io_num, int io_mode);

    [DllImport("api_c.dll", EntryPoint = "rm_get_tool_IO_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_tool_IO_state(IntPtr handle, ref int mode, ref int state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_tool_voltage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_tool_voltage(IntPtr handle, int voltage_type);

    [DllImport("api_c.dll", EntryPoint = "rm_get_tool_voltage", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_tool_voltage(IntPtr handle, ref int voltage_type);

    [DllImport("api_c.dll", EntryPoint = "rm_set_gripper_route", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_gripper_route(IntPtr handle, int min_limit, int max_limit);

    [DllImport("api_c.dll", EntryPoint = "rm_set_gripper_release", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_gripper_release(IntPtr handle, int speed, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_set_gripper_pick", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_gripper_pick(IntPtr handle, int speed, int force, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_set_gripper_pick_on", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_gripper_pick_on(IntPtr handle, int speed, int force, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_set_gripper_position", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_gripper_position(IntPtr handle, int position, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_get_gripper_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_gripper_state(IntPtr handle, ref rm_gripper_state_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_force_data", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_force_data(IntPtr handle, ref rm_force_data_t data);

    [DllImport("api_c.dll", EntryPoint = "rm_clear_force_data", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_clear_force_data(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_force_sensor", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_force_sensor(IntPtr handle, bool block);

    [DllImport("api_c.dll", EntryPoint = "rm_manual_set_force", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_manual_set_force(IntPtr handle, int count, [In, Out] float[] joint, bool block);

    [DllImport("api_c.dll", EntryPoint = "rm_stop_set_force_sensor", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_stop_set_force_sensor(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_get_Fz", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_Fz(IntPtr handle, ref rm_fz_data_t data);

    [DllImport("api_c.dll", EntryPoint = "rm_clear_Fz", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_clear_Fz(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_auto_set_Fz", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_auto_set_Fz(IntPtr handle, bool block);

    [DllImport("api_c.dll", EntryPoint = "rm_manual_set_Fz", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_manual_set_Fz(IntPtr handle, [In, Out] float[] joint1, [In, Out] float[] joint2, bool block);

    [DllImport("api_c.dll", EntryPoint = "rm_start_drag_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_start_drag_teach(IntPtr handle, int trajectory_record);

    [DllImport("api_c.dll", EntryPoint = "rm_stop_drag_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_stop_drag_teach(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_start_multi_drag_teach", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_start_multi_drag_teach(IntPtr handle, int mode, int singular_wall);

    [DllImport("api_c.dll", EntryPoint = "rm_drag_trajectory_origin", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_drag_trajectory_origin(IntPtr handle, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_run_drag_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_run_drag_trajectory(IntPtr handle, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_pause_drag_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_pause_drag_trajectory(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_continue_drag_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_continue_drag_trajectory(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_stop_drag_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_stop_drag_trajectory(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_save_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_save_trajectory(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, ref int num);

    [DllImport("api_c.dll", EntryPoint = "rm_set_force_position", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_force_position(IntPtr handle, int sensor, int mode, int direction, float N);

    [DllImport("api_c.dll", EntryPoint = "rm_stop_force_position", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_stop_force_position(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_hand_posture", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_hand_posture(IntPtr handle, int posture_num, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_set_hand_seq", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_hand_seq(IntPtr handle, int seq_num, bool block, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_set_hand_angle", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_hand_angle(IntPtr handle, int hand_angle);

    [DllImport("api_c.dll", EntryPoint = "rm_set_hand_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_hand_speed(IntPtr handle, int speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_hand_force", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_hand_force(IntPtr handle, int hand_force);

    [DllImport("api_c.dll", EntryPoint = "rm_set_modbus_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_modbus_mode(IntPtr handle, int port, int baudrate, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_close_modbus_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_close_modbus_mode(IntPtr handle, int port);

    [DllImport("api_c.dll", EntryPoint = "rm_set_modbustcp_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_modbustcp_mode(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string ip, int port, int timeout);

    [DllImport("api_c.dll", EntryPoint = "rm_close_modbustcp_mode", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_close_modbustcp_mode(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_read_coils", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_coils(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_read_input_status", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_input_status(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_read_holding_registers", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_holding_registers(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_read_input_registers", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_input_registers(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_write_single_coil", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_write_single_coil(IntPtr handle, rm_peripheral_read_write_params_t param, int data);

    [DllImport("api_c.dll", EntryPoint = "rm_write_single_register", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_write_single_register(IntPtr handle, rm_peripheral_read_write_params_t param, int data);

    [DllImport("api_c.dll", EntryPoint = "rm_write_registers", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_write_registers(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_write_coils", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_write_coils(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_read_multiple_coils", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_multiple_coils(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_read_multiple_holding_registers", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_read_multiple_holding_registers(IntPtr handle, rm_peripheral_read_write_params_t param, ref int data);

    [DllImport("api_c.dll", EntryPoint = "rm_set_install_pose", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_install_pose(IntPtr handle, float x, float y, float z);

    [DllImport("api_c.dll", EntryPoint = "rm_get_install_pose", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_install_pose(IntPtr handle, ref float x, ref float y, ref float z);

    [DllImport("api_c.dll", EntryPoint = "rm_start_force_position_move", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_start_force_position_move(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_stop_force_position_move", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_stop_force_position_move(IntPtr handle);

    [DllImport("api_c.dll", EntryPoint = "rm_force_position_move_joint", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_force_position_move_joint(IntPtr handle, [In, Out] float[] joint, int sensor, int mode, int dir, float force, bool follow);

    [DllImport("api_c.dll", EntryPoint = "rm_force_position_move_pose", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_force_position_move_pose(IntPtr handle, rm_pose_t pose, int sensor, int mode, int dir, float force, bool follow);

    [DllImport("api_c.dll", EntryPoint = "rm_set_lift_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_lift_speed(IntPtr handle, int speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_lift_height", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_lift_height(IntPtr handle, int speed, int height);

    [DllImport("api_c.dll", EntryPoint = "rm_get_lift_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_lift_state(IntPtr handle, ref rm_expand_state_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_expand_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_expand_state(IntPtr handle, ref rm_expand_state_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_expand_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_expand_speed(IntPtr handle, int speed);

    [DllImport("api_c.dll", EntryPoint = "rm_set_expand_pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_expand_pos(IntPtr handle, int speed, int pos);

    [DllImport("api_c.dll", EntryPoint = "rm_send_project", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_send_project(IntPtr handle, rm_send_project_t project, ref int errline);

    [DllImport("api_c.dll", EntryPoint = "rm_set_plan_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_plan_speed(IntPtr handle, int speed);

    [DllImport("api_c.dll", EntryPoint = "rm_get_program_trajectory_list", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_program_trajectory_list(IntPtr handle, int page_num, int page_size, [MarshalAs(UnmanagedType.LPStr)] string vague_search, ref rm_program_trajectorys_t trajectorys);

    [DllImport("api_c.dll", EntryPoint = "rm_set_program_id_run", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_program_id_run(IntPtr handle, int id, int speed, int block);

    [DllImport("api_c.dll", EntryPoint = "rm_get_program_run_state", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_program_run_state(IntPtr handle, ref rm_program_run_state_t run_state);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_program_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_program_trajectory(IntPtr handle, int id);

    [DllImport("api_c.dll", EntryPoint = "rm_update_program_trajectory", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_update_program_trajectory(IntPtr handle, int id, int speed, [MarshalAs(UnmanagedType.LPStr)] string name);

    [DllImport("api_c.dll", EntryPoint = "rm_set_default_run_program", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_default_run_program(IntPtr handle, int id);

    [DllImport("api_c.dll", EntryPoint = "rm_get_default_run_program", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_default_run_program(IntPtr handle, ref int id);

    [DllImport("api_c.dll", EntryPoint = "rm_add_global_waypoint", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_add_global_waypoint(IntPtr handle, rm_waypoint_t waypoint);

    [DllImport("api_c.dll", EntryPoint = "rm_update_global_waypoint", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_update_global_waypoint(IntPtr handle, rm_waypoint_t waypoint);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_global_waypoint", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_global_waypoint(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string point_name);

    [DllImport("api_c.dll", EntryPoint = "rm_get_given_global_waypoint", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_given_global_waypoint(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, ref rm_waypoint_t point);

    [DllImport("api_c.dll", EntryPoint = "rm_get_global_waypoints_list", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_global_waypoints_list(IntPtr handle, int page_num, int page_size, [MarshalAs(UnmanagedType.LPStr)] string vague_search, ref rm_waypoint_list_t point_list);

    [DllImport("api_c.dll", EntryPoint = "rm_set_realtime_push", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_realtime_push(IntPtr handle, rm_realtime_push_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_get_realtime_push", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_realtime_push(IntPtr handle, ref rm_realtime_push_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_add_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_add_electronic_fence_config(IntPtr handle, rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_update_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_update_electronic_fence_config(IntPtr handle, rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_delete_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_delete_electronic_fence_config(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string form_name);

    [DllImport("api_c.dll", EntryPoint = "rm_get_electronic_fence_list_names", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_electronic_fence_list_names(IntPtr handle, ref rm_fence_names_t names, ref int len);

    [DllImport("api_c.dll", EntryPoint = "rm_get_given_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_given_electronic_fence_config(IntPtr handle, [MarshalAs(UnmanagedType.LPStr)] string name, ref rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_get_electronic_fence_list_infos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_electronic_fence_list_infos(IntPtr handle, ref rm_fence_config_list_t config_list, ref int len);

    [DllImport("api_c.dll", EntryPoint = "rm_set_electronic_fence_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_electronic_fence_enable(IntPtr handle, rm_electronic_fence_enable_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_electronic_fence_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_electronic_fence_enable(IntPtr handle, ref rm_electronic_fence_enable_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_electronic_fence_config(IntPtr handle, rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_get_electronic_fence_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_electronic_fence_config(IntPtr handle, ref rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_set_virtual_wall_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_virtual_wall_enable(IntPtr handle, rm_electronic_fence_enable_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_virtual_wall_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_virtual_wall_enable(IntPtr handle, ref rm_electronic_fence_enable_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_set_virtual_wall_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_virtual_wall_config(IntPtr handle, rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_get_virtual_wall_config", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_virtual_wall_config(IntPtr handle, ref rm_fence_config_t config);

    [DllImport("api_c.dll", EntryPoint = "rm_set_self_collision_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_set_self_collision_enable(IntPtr handle, bool state);

    [DllImport("api_c.dll", EntryPoint = "rm_get_self_collision_enable", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_get_self_collision_enable(IntPtr handle, ref bool state);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_init_sys_data", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_init_sys_data(rm_robot_arm_model_e Mode, rm_force_type_e Type);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_angle", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_angle(float x, float y, float z);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_angle", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_angle(ref float x, ref float y, ref float z);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_workframe", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_workframe(ref rm_frame_t coord_work);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_curr_workframe", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_curr_workframe(ref rm_frame_t coord_work);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_toolframe", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_toolframe(ref rm_frame_t coord_tool);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_curr_toolframe", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_curr_toolframe(ref rm_frame_t coord_tool);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_joint_max_limit", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_joint_max_limit([In, Out] float[] joint_limit);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_joint_max_limit", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_joint_max_limit([In, Out] float[] joint_limit);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_joint_min_limit", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_joint_min_limit([In, Out] float[] joint_limit);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_joint_min_limit", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_joint_min_limit([In, Out] float[] joint_limit);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_joint_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_joint_max_speed([In, Out] float[] joint_slim_max);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_joint_max_speed", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_joint_max_speed([In, Out] float[] joint_slim_max);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_set_joint_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_set_joint_max_acc([In, Out] float[] joint_alim_max);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_get_joint_max_acc", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern void rm_algo_get_joint_max_acc([In, Out] float[] joint_alim_max);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_inverse_kinematics", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern int rm_algo_inverse_kinematics(IntPtr handle, rm_inverse_kinematics_params_t param, [Out] float[] q_out);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_forward_kinematics", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_forward_kinematics(IntPtr handle, [In, Out] float[] joint);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_euler2quaternion", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_quat_t rm_algo_euler2quaternion(rm_euler_t eu);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_quaternion2euler", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_euler_t rm_algo_quaternion2euler(rm_quat_t qua);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_euler2matrix", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_matrix_t rm_algo_euler2matrix(rm_euler_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_pos2matrix", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_matrix_t rm_algo_pos2matrix(rm_pose_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_matrix2pos", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_matrix2pos(rm_matrix_t matrix);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_base2workframe", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_base2workframe(rm_matrix_t matrix, rm_pose_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_workframe2base", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_workframe2base(rm_matrix_t matrix, rm_pose_t state);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_RotateMove", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_RotateMove(IntPtr handle, [In, Out] float[] curr_joint, int rotate_axis, float rotate_angle, rm_pose_t choose_axis);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_cartesian_tool", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_cartesian_tool(IntPtr handle, [In, Out] float[] curr_joint, float move_lengthx, float move_lengthy, float move_lengthz);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_end2tool", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_end2tool(IntPtr handle, rm_pose_t eu_end);

    [DllImport("api_c.dll", EntryPoint = "rm_algo_tool2end", CharSet = CharSet.Auto, CallingConvention = CallingConvention.Cdecl)]
    public static extern rm_pose_t rm_algo_tool2end(IntPtr handle, rm_pose_t eu_tool);


    //static IntPtr robotHandlePtr;

    private static int Demo_Move_Cmd(IntPtr robotHandlePtr)
    {
        int ret;

        int v = 20; // 速度
        int r = 0;  // 交融半径
        int trajectory_connect = 0; // 轨迹连接
        int block = 1; // 阻塞
        int loop = 0; // 圆弧运动圈数
        float[] c1 = { 0.011f, 21.288f, 78.315f, -0.024f, 80.397f, 0.015f }; // 目标关节角度数组
        rm_pose_t c2 = new();   // 运动位姿
        c2.position.x = -0.320f;
        c2.position.y = 0.02f;
        c2.position.z = 0.3f;
        c2.euler.rx = 3.142f;
        c2.euler.ry = 0;
        c2.euler.rz = 0;

        rm_pose_t c3 = new();   // 运动位姿
        c3.position.x = -0.330f;
        c3.position.y = 0.03f;
        c3.position.z = 0.3f;
        c3.euler.rx = 3.142f;
        c3.euler.ry = 0;
        c3.euler.rz = 0;

        rm_pose_t c4 = new();   // 运动位姿
        c4.position.x = -0.330f;
        c4.position.y = -0.03f;
        c4.position.z = 0.3f;
        c4.euler.rx = 3.142f;
        c4.euler.ry = 0;
        c4.euler.rz = 0;

        rm_pose_t c5 = new();
        c5.position.x = -0.270f;
        c5.position.y = 0.02f;
        c5.position.z = 0.3f;
        c5.euler.rx = 3.142f;
        c5.euler.ry = 0;
        c5.euler.rz = 0;

        rm_pose_t c6 = new();
        c6.position.x = -0.260f;
        c6.position.y = 0.03f;
        c6.position.z = 0.3f;
        c6.euler.rx = 3.142f;
        c6.euler.ry = 0;
        c6.euler.rz = 0;

        rm_pose_t c7 = new();
        c7.position.x = -0.260f;
        c7.position.y = -0.03f;
        c7.position.z = 0.3f;
        c7.euler.rx = 3.142f;
        c7.euler.ry = 0;
        c7.euler.rz = 0;

        // 机械臂以20%的速度、立即规划关节阻塞运动到目标关节角度
        ret = rm_movej(robotHandlePtr, c1, 20, 0, 0, 1);
        if (ret != 0)
        {
            Console.WriteLine("[rm_move_joint] Error occurred: " + ret);
            return ret;
        }
        else
        {
            Console.WriteLine("[rm_move_joint] Success");
        }

        for (int i = 0; i < 3; i++)
        {
            ret = rm_movel(robotHandlePtr, c2, v, r, trajectory_connect, block);
            if (ret != 0)
            {
                Console.WriteLine("[rm_movel] result :" + ret);
                return ret;
            }
            ret = rm_movec(robotHandlePtr, c3, c4, v, r, loop, trajectory_connect, block);
            if (ret != 0)
            {
                Console.WriteLine("[rm_movec] result :" + ret);
                return ret;
            }

            ret = rm_movel(robotHandlePtr, c5, v, r, trajectory_connect, block);
            if (ret != 0)
            {
                Console.WriteLine("[rm_movel] result :" + ret);
                return ret;
            }
            ret = rm_movec(robotHandlePtr, c6, c7, v, r, loop, trajectory_connect, block);
            if (ret != 0)
            {
                Console.WriteLine("[rm_movec] result :" + ret);
                return ret;
            }
        }

        return ret;
    }

    private static void Demo_Send_Project(IntPtr robotHandlePtr)
    {
        // 获取可执行文件所在目录，轨迹文件放在该目录下
        string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;

        rm_send_project_t project = new();
        project.project_path = currentDirectory + "demo_trajectory.txt";
        project.plan_speed = 20;
        project.only_save = 0;
        project.save_id = 4;
        project.project_path_len = project.project_path.Length;
        project.project_type = 0;
        Console.WriteLine("trajectory file path:" + project.project_path);
        int err_line = new();
        int ret = rm_send_project(robotHandlePtr, project, ref err_line);
        if (ret != 0)
        {
            Console.WriteLine("send trajectory file err:" + ret + ", err_line: " + err_line);
        }
        else
        {
            Console.WriteLine("send trajectory file success!");
        }
    }

    static void Demo_Callback_ArmState(IntPtr robotHandlePtr)
    {
        // 注册回调函数
        rm_realtime_arm_state_callback_delegate callback = new(Arm_State_Realtime_Callback);
        rm_realtime_arm_state_call_back(callback);
    }
    // udp数据回调函数
    static void Arm_State_Realtime_Callback(rm_realtime_arm_joint_state_t state)
    {
        Console.WriteLine("rm_realtime_arm_joint_state:" + state.ToString());
    }


    static void Main(string[] args)
    {
        Console.WriteLine("this is RM-ROBOT!");
        // 获取当前API版本
        IntPtr versionPtr = rm_api_version();
        string? version = Marshal.PtrToStringAnsi(versionPtr);
        Console.WriteLine("api version: " + version);

        // 设置日志打印等级为warning
        rm_set_log_call_back(null, 3);

        // 初始化为三线程模式
        _ = rm_init(rm_thread_mode_e.RM_TRIPLE_MODE_E);

        // 创建机械臂控制句柄
        IntPtr robotHandlePtr = rm_create_robot_arm("192.168.1.18", 8080);
        // 获取句柄id
        rm_robot_handle robotHandle = (rm_robot_handle)Marshal.PtrToStructure(robotHandlePtr, typeof(rm_robot_handle))!;
        if (robotHandlePtr != IntPtr.Zero && robotHandle.id > 0)
        {
            Console.WriteLine("[rm_create_robot_arm] connect success, handle id:{0}", robotHandle.id);
        }
        else
        {
            Console.WriteLine("[rm_create_robot_arm] connect error:{0}", robotHandle.id);
        }

        // 在线编程文件下发
        //Demo_Send_Project(robotHandlePtr);


        // 调用movej、moveL、moveC运动控制指令画8字示例
        int ret = Demo_Move_Cmd(robotHandlePtr);
        if (ret == 0)
        {
            _ = rm_destory();
            Console.WriteLine("Demo_Move_Cmd Completely! Robotic arm disconnect!");
        }
        else
        {
            _ = rm_destory();
            Console.WriteLine("Demo_Move_Cmd execution failed!");
        }

    }

}