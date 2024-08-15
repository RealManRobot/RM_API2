cmake_minimum_required(VERSION 3.10)  # 更新 CMake 最低版本以支持 CMAKE_C_STANDARD
project(RMDemo_IOControl)

# 设置 C 标准
set(CMAKE_CXX_STANDARD 11)  # 设置 C 标准为 C11

# 设置源文件
set(SOURCES
        src/main.cpp
)

# 添加可执行文件
add_executable(RMDemo_IOControl ${SOURCES})

# 查找库
find_library(RMAN_API_LIB NAMES api_cpp PATHS "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm/lib")

if(NOT RMAN_API_LIB)
    message(FATAL_ERROR "api_cpp library not found")
else()
    message(STATUS "RMAN_API_LIB: ${RMAN_API_LIB}")
    # 链接库
    target_link_libraries(RMDemo_IOControl ${RMAN_API_LIB})
    # 包含目录
    target_include_directories(RMDemo_IOControl PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm/include")

    # 如果是 Windows 平台，拷贝 DLL 文件到可执行文件的目录
    if(WIN32)
        add_custom_command(TARGET RMDemo_IOControl POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm/lib/api_cpp.dll"
                $<TARGET_FILE_DIR:RMDemo_IOControl>)
    endif()

    # 如果是 UNIX 平台
    if(UNIX)
        add_custom_command(TARGET RMDemo_IOControl POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm/lib/libapi_cpp.so"
                $<TARGET_FILE_DIR:RMDemo_IOControl>)
    endif()

endif()

# 定义拖动示教文件保存路径为预处理器宏
set(TRAJECTORY_FILE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/data/trajectory.txt")
add_definitions(-DTRAJECTORY_FILE_PATH="${TRAJECTORY_FILE_PATH}")
# 定义在线编程文件路径为预处理器宏
set(PROJECT_FILE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/data/project.txt")
add_definitions(-DPROJECT_FILE_PATH="${PROJECT_FILE_PATH}")
