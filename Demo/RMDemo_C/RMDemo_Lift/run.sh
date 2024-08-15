#!/bin/bash

# 设置构建目录
BUILD_DIR=build

# 如果构建目录存在，则删除
if [ -d "$BUILD_DIR" ]; then
  rm -rf $BUILD_DIR
fi

# 创建构建目录
mkdir $BUILD_DIR

# 进入构建目录
cd $BUILD_DIR

# 运行CMake配置
cmake ..

# 运行make进行编译
make

# 返回根目录
cd ..

# 运行编译后的可执行文件
./build/RMDemo_Lift