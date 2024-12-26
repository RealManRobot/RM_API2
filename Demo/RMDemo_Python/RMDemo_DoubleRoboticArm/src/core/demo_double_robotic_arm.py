from src.Robotic_Arm.rm_robot_interface import *
import threading


def demo_movej(robot, joint=None, v=20, r=0, connect=0, block=1):
    """
    Perform movej motion.

    Args:
        robot (RoboticArm): Instance of the RoboticArm.
        joint (list of float, optional): Joint positions. Defaults to [0, 0, 0, 0, 0, 0].
        v (float, optional): Speed of the motion. Defaults to 20.
        connect (int, optional): Trajectory connection flag. Defaults to 0.
        block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
        r (float, optional): Blending radius. Defaults to 0.

    Returns:
        None
    """
    if joint is None:
        joint = [0, 0, 0, 0, 0, 0]
    movej_result = robot.rm_movej(joint, v, r, connect, block)
    if movej_result == 0:
        print("\nmovej motion succeeded\n")
    else:
        print("\nmovej motion failed, Error code: ", movej_result, "\n")


def demo_movel(robot, pose, v=20, r=0, connect=0, block=1):
    """
    Perform movel motion.

    Args:
        robot (RoboticArm): Instance of the RoboticArm.
        pose (list of float): End position [x, y, z, rx, ry, rz].
        v (float, optional): Speed of the motion. Defaults to 20.
        connect (int, optional): Trajectory connection flag. Defaults to 0.
        block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
        r (float, optional): Blending radius. Defaults to 0.

    Returns:
        None
    """
    movel_result = robot.rm_movel(pose, v, r, connect, block)
    if movel_result == 0:
        print("\nmovel motion succeeded\n")
    else:
        print("\nmovel motion failed, Error code: ", movel_result, "\n")


def demo_movec(robot, pose_via, pose_to, v=20, r=0, loop=0, connect=0, block=1):
    """
    Perform movec motion.

    Args:
        robot (RoboticArm): Instance of the RoboticArm.
        pose_via (list of float): Via position [x, y, z, rx, ry, rz].
        pose_to (list of float): End position for the circular path [x, y, z, rx, ry, rz].
        v (float, optional): Speed of the motion. Defaults to 20.
        loop (int, optional): Number of loops. Defaults to 0.
        connect (int, optional): Trajectory connection flag. Defaults to 0.
        block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
        r (float, optional): Blending radius. Defaults to 0.

    Returns:
        None
    """
    movec_result = robot.rm_movec(pose_via, pose_to, v, r, loop, connect, block)
    if movec_result == 0:
        print("\nmovec motion succeeded\n")
    else:
        print("\nmovec motion failed, Error code: ", movec_result, "\n")


def demo_movej_p(robot, pose, v=20, r=0, connect=0, block=1):
    """
    Perform movej_p motion.

    Args:
        robot (RoboticArm): Instance of the RoboticArm.
        pose (list of float): Position [x, y, z, rx, ry, rz].
        v (float, optional): Speed of the motion. Defaults to 20.
        connect (int, optional): Trajectory connection flag. Defaults to 0.
        block (int, optional): Whether the function is blocking (1 for blocking, 0 for non-blocking). Defaults to 1.
        r (float, optional): Blending radius. Defaults to 0.

    Returns:
        None
    """
    movej_p_result = robot.rm_movej_p(pose, v, r, connect, block)
    if movej_p_result == 0:
        print("\nmovej_p motion succeeded\n")
    else:
        print("\nmovej_p motion failed, Error code: ", movej_p_result, "\n")


def connect_robot(ip, port, level=3, mode=None):
    """
    Connect to the robot arm.

    Args:
        ip (str): IP address of the robot arm.
        port (int): Port number.
        level (int, optional): Connection level. Defaults to 3.
        mode (int, optional): Thread mode as an integer (0: single, 1: dual, 2: triple). Defaults to None.

    Returns:
        RoboticArm: Instance of the connected RoboticArm.
    """
    if mode is not None:
        thread_mode = rm_thread_mode_e(mode)
        robot = RoboticArm(thread_mode)
    else:
        robot = RoboticArm()

    handle = robot.rm_create_robot_arm(ip, port, level)

    if handle.id == -1:
        print("\nFailed to connect to the robot arm\n")
        exit(1)
    else:
        print(f"\nSuccessfully connected to the robot arm: {handle.id}\n")

    return robot


def disconnect_robot(robot):
    """
    Disconnect from the robot arm.

    Args:
        robot (RoboticArm): Instance of the RoboticArm.

    Returns:
        None
    """
    handle = robot.rm_delete_robot_arm()
    if handle == 0:
        print("\nSuccessfully disconnected from the robot arm\n")
    else:
        print("\nFailed to disconnect from the robot arm\n")


def robot_motion_1():
    """
    Perform a sequence of motions with robot 1.

    Returns:
        None
    """
    # Connect to robot 1
    robot1 = connect_robot("192.168.1.18", 8080, 3, 2)

    # Perform movej motion with default parameters
    demo_movej(robot1)

    # Perform movej motion with specified joint positions
    demo_movej(robot1, [0, 20, 70, 0, 90, 0])

    # Perform movej_p motion
    demo_movej_p(robot1, [0.3, 0, 0.3, 3.141, 0, 0])

    # Perform movel motion
    demo_movel(robot1, [0.2, 0, 0.3, 3.141, 0, 0])

    # Perform movec motion
    demo_movec(robot1, [0.25, 0.05, 0.3, 3.141, 0, 0], [0.25, -0.05, 0.3, 3.141, 0, 0], loop=2)

    # Disconnect from robot 1
    disconnect_robot(robot1)


def robot_motion_2():
    """
    Perform a sequence of motions with robot 2.

    Returns:
        None
    """
    # Connect to robot 2
    robot2 = connect_robot("192.168.1.19", 8080, 3)

    # Perform movej motion with default parameters
    demo_movej(robot2)

    # Perform movej motion with specified joint positions
    demo_movej(robot2, [0, 20, 70, 0, 90, 0])

    # Perform movej_p motion
    demo_movej_p(robot2, [0.3, 0, 0.3, 3.141, 0, 0])

    # Perform movel motion
    demo_movel(robot2, [0.2, 0, 0.3, 3.141, 0, 0])

    # Perform movec motion
    demo_movec(robot2, [0.25, 0.05, 0.3, 3.141, 0, 0], [0.25, -0.05, 0.3, 3.141, 0, 0], loop=2)

    # Disconnect from robot 2
    disconnect_robot(robot2)


def main():
    # Create and start threads for robot motions
    thread1 = threading.Thread(target=robot_motion_1)
    thread2 = threading.Thread(target=robot_motion_2)

    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print("Both robot motions completed")


if __name__ == "__main__":
    main()
