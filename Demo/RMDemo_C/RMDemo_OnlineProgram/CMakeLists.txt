cmake_minimum_required(VERSION 3.5)
project(RMDemo_OnlineProgram)

# 设置 C 标准
set(CMAKE_C_STANDARD 11)  # 设置 C 标准为 C11

# 设置源文件
set(SOURCES
        src/main.c
)

# 添加可执行文件
add_executable(RMDemo_OnlineProgram ${SOURCES})

# 定义库和头文件的路径
set(ROBOTIC_ARM_DIR "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm")
set(ROBOTIC_ARM_LIB_DIR "${ROBOTIC_ARM_DIR}/lib")
set(ROBOTIC_ARM_INCLUDE_DIR "${ROBOTIC_ARM_DIR}/include")

# 查找库
find_library(RMAN_API_LIB NAMES api_c PATHS "${ROBOTIC_ARM_LIB_DIR}")

if(NOT RMAN_API_LIB)
    message(FATAL_ERROR "api_c library not found")
else()
    message(STATUS "RMAN_API_LIB: ${RMAN_API_LIB}")

    # 链接库
    target_link_libraries(RMDemo_OnlineProgram ${RMAN_API_LIB})

    # 包含目录
    target_include_directories(RMDemo_OnlineProgram PUBLIC "${ROBOTIC_ARM_INCLUDE_DIR}")

    # 如果是 Windows 平台，拷贝 DLL 文件到可执行文件的目录
    if(WIN32)
        add_custom_command(TARGET RMDemo_OnlineProgram POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/api_c.dll"
                $<TARGET_FILE_DIR:RMDemo_OnlineProgram>)
    endif()

    # 如果是 UNIX 平台，确保动态库文件可以在运行时被找到
    if(UNIX)
        add_custom_command(TARGET RMDemo_OnlineProgram POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/libapi_c.so"
                $<TARGET_FILE_DIR:RMDemo_OnlineProgram>)
    endif()

endif()

# 定义拖动示教文件保存路径为预处理器宏
set(TRAJECTORY_FILE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/data/trajectory.txt")
add_definitions(-DTRAJECTORY_FILE_PATH="${TRAJECTORY_FILE_PATH}")
# 定义在线编程文件路径为预处理器宏
set(PROJECT_FILE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/data/project.txt")
add_definitions(-DPROJECT_FILE_PATH="${PROJECT_FILE_PATH}")
