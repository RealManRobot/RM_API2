#include <QCoreApplication>
#include "rm_interface.h"

rm_robot_handle *handle = NULL;
int arm_dof;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    // 初始化线程模式为双线程
    rm_init(RM_DUAL_MODE_E);
    rm_set_log_call_back(NULL, 3);

    // 获取API版本
    char *version = rm_api_version();
    printf("api version: %s\n", version);

    // 创建机械臂控制句柄
    handle = rm_create_robot_arm("192.168.1.18",8080);
    if( handle->id  == -1)
    {
        rm_delete_robot_arm(handle);
        printf("arm connect err...\n");
    }
    else
    {
        // 获取机械臂基本信息
        rm_robot_info_t info;
        rm_get_robot_info(handle, &info);
        arm_dof = info.arm_dof;
        printf("connect success,arm id %d, robot model:%d, force_type:%d\n",handle->id, info.arm_model, info.force_type);
    }

    int ret = 0;
    //获取型号以及版本信息
    rm_arm_software_version_t software_info;
    ret = rm_get_arm_software_info(handle,&software_info);
    if(ret != 0)
    {
        printf("[rm_get_arm_software_info] result : %d\n", ret);
        return ret;
    }
    else
    {
        printf("Arm Product_version: %s\n", software_info.product_version);
        printf("Arm Plan_version: %s\n", software_info.plan_info.version);
        printf("Plan Bulid_time: %s\n", software_info.plan_info.build_time);
    }

    int v = 20; // 速度
    int r = 0;  // 交融半径
    int trajectory_connect = 0; // 轨迹连接
    int block = 1; // 阻塞
    int loop = 0; // 圆弧运动圈数
    float c1[6] = {0.011,21.288,78.315,-0.024,80.397,0.015}; // 目标关节角度数组
    rm_pose_t c2, c3, c4, c5, c6, c7;   // 运动位姿
    c2.position.x = -0.320f;
    c2.position.y = 0.02f;
    c2.position.z = 0.3f;
    c2.euler.rx = 3.142f;
    c2.euler.ry = 0;
    c2.euler.rz = 0;

    c3.position.x = -0.330f;
    c3.position.y = 0.03f;
    c3.position.z = 0.3f;
    c3.euler.rx = 3.142f;
    c3.euler.ry = 0;
    c3.euler.rz = 0;

    c4.position.x = -0.330f;
    c4.position.y = -0.03f;
    c4.position.z = 0.3f;
    c4.euler.rx = 3.142f;
    c4.euler.ry = 0;
    c4.euler.rz = 0;

    c5.position.x = -0.270f;
    c5.position.y = 0.02f;
    c5.position.z = 0.3f;
    c5.euler.rx = 3.142f;
    c5.euler.ry = 0;
    c5.euler.rz = 0;

    c6.position.x = -0.260f;
    c6.position.y = 0.03f;
    c6.position.z = 0.3f;
    c6.euler.rx = 3.142f;
    c6.euler.ry = 0;
    c6.euler.rz = 0;

    c7.position.x = -0.260f;
    c7.position.y = -0.03f;
    c7.position.z = 0.3f;
    c7.euler.rx = 3.142f;
    c7.euler.ry = 0;
    c7.euler.rz = 0;
    ret = rm_movej(handle, c1, v, r, trajectory_connect, block);
    if(ret != 0)
    {
        printf("[rm_move_joint] result : %d\n", ret);
        return ret;
    }

    for(int i=0; i<2; i++)
    {
        ret = rm_movel(handle, c2, v, r, trajectory_connect, block);
        if(ret != 0)
        {
            printf("[rm_movel] result : %d\n", ret);
            return ret;
        }
        ret = rm_movec(handle, c3,c4, v,r,loop,trajectory_connect, block);
        if(ret != 0)
        {
            printf("[rm_movec] result : %d\n", ret);
            return ret;
        }

        ret = rm_movel(handle, c5, v, r, trajectory_connect, block);
        if(ret != 0)
        {
            printf("[rm_movel] result : %d\n", ret);
            return ret;
        }
        ret = rm_movec(handle, c6,c7, v,r,loop,trajectory_connect, block);
        if(ret != 0)
        {
            printf("[rm_movec] result : %d\n", ret);
            return ret;
        }
    }

    printf("The sample has been executed successfully ...\n");

    return a.exec();
}
