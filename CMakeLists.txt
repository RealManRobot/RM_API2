cmake_minimum_required(VERSION 3.22)
cmake_policy(SET CMP0048 NEW)

execute_process(
    COMMAND uname -m
    OUTPUT_VARIABLE ARCH
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
message(STATUS "Detected architecture using uname: ${ARCH}")

set(C_DIR "${CMAKE_CURRENT_SOURCE_DIR}/C")
set(CPP_DIR "${CMAKE_CURRENT_SOURCE_DIR}/C++")

# 获取当前系统的处理器架构，根据不同的架构设置不同的头文件目录
if(ARCH MATCHES "^(x86_64|amd64)$")
    set(LIB_C_DIR_HEAD "linux_x86_c_v")
    set(LIB_CPP_DIR_HEAD "linux_x86_c++_v")
    set(LIB_C_DEBUG_DIR_HEAD "linux_x86_c_debug_v")
    set(LIB_CPP_DEBUG_DIR_HEAD "linux_x86_c++_debug_v")
elseif(ARCH MATCHES  "^(arm)$")
    set(LIB_C_DIR_HEAD "linux_arm64_c_v")
    set(LIB_CPP_DIR_HEAD "linux_arm64_c++_v")
    set(LIB_C_DEBUG_DIR_HEAD "linux_x86_c_debug_v")
    set(LIB_CPP_DEBUG_DIR_HEAD "linux_x86_c++_debug_v")
else()
    message(FATAL_ERROR "Unsupported architecture: ${ARCH}")
endif()

# 设置库的名称和版本号
# 读取版本头文件内容
file(READ "${CPP_DIR}/include/rm_version.h" VERSION_HEADER_CONTENTS)
# 使用正则表达式提取 SDK_VERSION
string(REGEX MATCH "#define SDK_VERSION \\(\"([^\"]+)\"\\)" VERSION_MATCH ${VERSION_HEADER_CONTENTS})

if(VERSION_MATCH)
    # 提取版本号（括号内的值）
    string(REGEX REPLACE "#define SDK_VERSION \\(\"([^\"]+)\"\\)" "\\1" SDK_VERSION ${VERSION_MATCH})
    message(STATUS "Extracted SDK_VERSION: ${SDK_VERSION}")
    set(LIB_C_DIR "${C_DIR}/linux/${LIB_C_DIR_HEAD}${SDK_VERSION}")
    set(LIB_CPP_DIR "${CPP_DIR}/linux/${LIB_CPP_DIR_HEAD}${SDK_VERSION}")
    set(LIB_C_DEBUG_DIR "${C_DIR}/linux/${LIB_C_DEBUG_DIR_HEAD}${SDK_VERSION}")
    set(LIB_CPP_DEBUG_DIR "${CPP_DIR}/linux/${LIB_CPP_DEBUG_DIR_HEAD}${SDK_VERSION}")
else()
    message(FATAL_ERROR "SDK_VERSION not found in rm_version.h")
endif()

# 检查并去除版本号中的 't' 及其后续部分
string(FIND ${SDK_VERSION} "t" T_INDEX) # 查找 't' 的位置
if(T_INDEX GREATER_EQUAL 0)
    # 如果找到 't'，截断版本号
    string(SUBSTRING ${SDK_VERSION} 0 ${T_INDEX} CLEANED_VERSION)
    message(STATUS "Cleaned SDK_VERSION: ${CLEANED_VERSION}")
else()
    # 如果没有 't'，直接使用提取到的版本号
    set(CLEANED_VERSION ${SDK_VERSION})
    message(STATUS "No cleaning needed, using SDK_VERSION: ${CLEANED_VERSION}")
endif()

# 校验最终版本号是否符合 CMake 要求
string(REGEX MATCH "^[0-9]+\\.[0-9]+\\.[0-9]+" VALID_VERSION ${CLEANED_VERSION})

if(VALID_VERSION)
    message(STATUS "Using valid version: ${VALID_VERSION}")
    # 设置项目版本号
    project(rm_api2 VERSION ${VALID_VERSION})
else()
    message(FATAL_ERROR "Invalid SDK_VERSION format: ${CLEANED_VERSION}")
endif()

# 安装头文件到 include 目录
file(GLOB HEADER_FILES "${CPP_DIR}/include/*.h")
install(
  FILES ${HEADER_FILES}
  DESTINATION include
)

# 安装库文件到 lib 目录
install(FILES 
  "${LIB_C_DIR}/libapi_c.so"
  "${LIB_CPP_DIR}/libapi_cpp.so"
  "${LIB_C_DEBUG_DIR}/libapi_c_debug.so"
  "${LIB_CPP_DEBUG_DIR}/libapi_cpp_debug.so"
  DESTINATION lib
)

# 安装配置文件
set(ConfigFileInstallDir lib/cmake/rm_api2)
set(ConfigFileName rm_api2Config.cmake)
set(ConfigFileVersionName rm_api2ConfigVersion.cmake)
set(ConfigFileModelName rm_api2Config.cmake.in)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  ${CMAKE_BINARY_DIR}/${ConfigFileName}  # 将文件写到 build 目录
  VERSION ${RMAPI2_VERSION_MAJOR}.${RMAPI2_VERSION_MAJOR}
  COMPATIBILITY AnyNewerVersion
)

# 设置 rm_api2-Config.cmake.in 模板参数
configure_file(
  "${CMAKE_CURRENT_LIST_DIR}/${ConfigFileModelName}"
  "${CMAKE_BINARY_DIR}/${ConfigFileName}"
  @ONLY
)

# 生成 rm_api2-ConfigVersion.cmake 文件，用于版本验证
write_basic_package_version_file(
  "${CMAKE_BINARY_DIR}/${ConfigFileVersionName}"
  VERSION "${PROJECT_VERSION}"
  COMPATIBILITY AnyNewerVersion
)

install(
  FILES
    "${CMAKE_BINARY_DIR}/${ConfigFileName}"
    "${CMAKE_BINARY_DIR}/${ConfigFileVersionName}"
  DESTINATION ${ConfigFileInstallDir}
)