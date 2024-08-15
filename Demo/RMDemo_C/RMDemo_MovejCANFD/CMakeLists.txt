cmake_minimum_required(VERSION 3.5)
project(RMDemo_MovejCANFD)

# 设置 C 标准
set(CMAKE_C_STANDARD 11)

# 添加忽略定义重定义警告的选项
if(CMAKE_C_COMPILER_ID STREQUAL "GNU" OR CMAKE_C_COMPILER_ID STREQUAL "Clang")
    add_compile_options(-Wno-define-redefinition)
endif()

# 设置源文件
set(SOURCES
        src/main.c
)

# 添加可执行文件
add_executable(RMDemo_MovejCANFD ${SOURCES})

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
    target_link_libraries(RMDemo_MovejCANFD ${RMAN_API_LIB})

    # 包含目录
    target_include_directories(RMDemo_MovejCANFD PUBLIC "${ROBOTIC_ARM_INCLUDE_DIR}")

    # 如果是 Windows 平台，拷贝 DLL 文件到可执行文件的目录
    if(WIN32)
        add_custom_command(TARGET RMDemo_MovejCANFD POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/api_c.dll"
                $<TARGET_FILE_DIR:RMDemo_MovejCANFD>)
    endif()

    # 如果是 UNIX 平台，确保动态库文件可以在运行时被找到
    if(UNIX)
        add_custom_command(TARGET RMDemo_MovejCANFD POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy_if_different
                "${ROBOTIC_ARM_LIB_DIR}/libapi_c.so"
                $<TARGET_FILE_DIR:RMDemo_MovejCANFD>)
    endif()

endif()

# 将数据文件路径定义为预处理器宏
add_definitions(-DDATA_FILE_PATH="${CMAKE_CURRENT_SOURCE_DIR}/data/RM65&RM63_canfd_data.txt")
