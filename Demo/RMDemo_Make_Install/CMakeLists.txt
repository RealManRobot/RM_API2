cmake_minimum_required(VERSION 3.22)
project(MyApp)

# 设置 C 标准
set(CMAKE_C_STANDARD 11)  # 设置 C 标准为 C11
set(CMAKE_CXX_STANDARD 17)  # 设置 C++ 标准为 C++17

set(CMAKE_BUILD_TYPE Release)

# 查找 rm_api2
find_package(rm_api2 1.0 REQUIRED)

# 添加可执行目标
# add_executable(MyApp main.cpp)
add_executable(MyApp main.c)

# 链接 rm_api2 库
target_link_libraries(MyApp PRIVATE rm_api2)
