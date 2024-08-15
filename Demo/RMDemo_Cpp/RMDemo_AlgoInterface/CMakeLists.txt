cmake_minimum_required(VERSION 3.1)  # 更新 CMake 最低版本以支持 CMAKE_C_STANDARD
project(RMDemo_AlgoInterface)

# 设置 C 标准
set(CMAKE_C_STANDARD 11)  # 设置 C 标准为 C11

# 设置源文件
set(SOURCES
        src/main.cpp
)

# 添加可执行文件
add_executable(RMDemo_AlgoInterface ${SOURCES})

# 定义库和头文件的路径
set(ROBOTIC_ARM_DIR "${CMAKE_CURRENT_SOURCE_DIR}/Robotic_Arm")
set(ROBOTIC_ARM_LIB_DIR "${ROBOTIC_ARM_DIR}/lib")
set(ROBOTIC_ARM_INCLUDE_DIR "${ROBOTIC_ARM_DIR}/include")

# 查找库
find_library(RMAN_API_LIB NAMES api_cpp PATHS "${ROBOTIC_ARM_LIB_DIR}")

if(NOT RMAN_API_LIB)
    message(FATAL_ERROR "api_cpp library not found")
else()
    message(STATUS "RMAN_API_LIB: ${RMAN_API_LIB}")

    # 链接库
    target_link_libraries(RMDemo_AlgoInterface ${RMAN_API_LIB})

    # 包含目录
    target_include_directories(RMDemo_AlgoInterface PUBLIC "${ROBOTIC_ARM_INCLUDE_DIR}")

    # 如果是 Windows 平台，拷贝 DLL 文件到可执行文件的目录
    if(WIN32)
        add_custom_command(TARGET RMDemo_AlgoInterface POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/api_cpp.dll"
                $<TARGET_FILE_DIR:RMDemo_AlgoInterface>)
    endif()

    # 如果是 UNIX 平台，确保动态库文件可以在运行时被找到
    if(UNIX)
        add_custom_command(TARGET RMDemo_AlgoInterface POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/libapi_cpp.so"
                $<TARGET_FILE_DIR:RMDemo_AlgoInterface>)
    endif()

endif()