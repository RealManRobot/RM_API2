@echo off

rem 设置构建目录的路径
set BUILD_DIR=build

rem 如果构建目录存在，则删除它
if exist "%BUILD_DIR%" (
    echo Deleting existing build directory...
    rmdir /s /q "%BUILD_DIR%"
)

rem 创建新的构建目录
echo Creating new build directory...
mkdir "%BUILD_DIR%"

rem 进入构建目录
cd "%BUILD_DIR%"

rem 运行 CMake 配置
cmake -S .. -B .

rem 使用 CMake 编译项目
cmake --build .

rem 检查编译是否成功
if exist "Debug\RMDemo_ModbusRTU.exe" (
    rem 运行生成的可执行文件
    echo Run...
    Debug\RMDemo_ModbusRTU.exe
) else (
    echo Failed.
)

rem 返回到批处理文件所在目录
cd ..

pause
