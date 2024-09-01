api_version=1.0.2

if [ ! -d lib/ ]; then  
    mkdir -p lib/  
fi  
cp C/linux/linux_x86_c_v$api_version/* lib/
cp C/windows/win_x64_c_v$api_version/* lib/

# 源目录  
c_src_dir="C/include"  

# *****************************替换C demo库****************************
# 目标目录的基路径  
base_dst_dir="Demo/RMDemo_C"  

# 遍历所有名为 RMDemo_* 的目录  
for dir in "$base_dst_dir"/RMDemo_*; do  
    # 检查该目录是否存在  
    if [ -d "$dir" ]; then  
        # 构建目标目录路径  
        dst_dir="$dir/Robotic_Arm"  
          
        # 如果目标目录不存在，则创建它  
        if [ ! -d "$dst_dir" ]; then  
            mkdir -p "$dst_dir"  
        fi  
          
        # 复制文件  
        cp -r "$c_src_dir"/* "$dst_dir"/include  
        cp -r lib/ "$dst_dir"
    fi  
done


# *****************************替换Qt&&VisualStudio&&C# demo库****************************
cp lib/* Demo/RMDemo_QtExample_C/lib/
cp C/include/* Demo/RMDemo_QtExample_C/include/
cp lib/* Demo/RMDemo_VisualStudio_Project/lib/
cp C/include/* Demo/RMDemo_VisualStudio_Project/include
cp C/windows/win_x64_c_v$api_version/api_c.dll Demo/RMDemo_CSHARP_Project/lib
rm -rf Demo/RMDemo_VisualStudio_Project/lib/libapi_c.so
# *****************************替换c++demo库****************************
rm -rf lib/*
cp C++/linux/linux_x86_c++_v$api_version/* lib/
cp C++/windows/win_x64_c++_v$api_version/* lib/

# 头文件源目录  
cpp_src_dir="C++/include"  
  
# 目标目录的基路径  
base_dst_dir="Demo/RMDemo_Cpp"  

  
# 遍历所有名为 RMDemo_* 的目录  
for dir in "$base_dst_dir"/RMDemo_*; do  
    # 检查该目录是否存在  
    if [ -d "$dir" ]; then  
        # 构建目标目录路径  
        dst_dir="$dir/Robotic_Arm"  
          
        # 如果目标目录不存在，则创建它  
        if [ ! -d "$dst_dir" ]; then  
            mkdir -p "$dst_dir"  
        fi  
          
        # 复制文件  
        cp -r "$cpp_src_dir"/* "$dst_dir"/include  
        cp -r lib/ "$dst_dir"
    fi  
done

# *****************************替换python demo****************************
rm -rf lib

# 源目录  
python_src_dir="Python/Robotic_Arm"  
  
# 目标目录的基路径  
base_dst_dir="Demo/RMDemo_Python"  

  
# 遍历所有名为 RMDemo_* 的目录  
for dir in "$base_dst_dir"/RMDemo_*; do  
    # 检查该目录是否存在  
    if [ -d "$dir" ]; then  
        # 构建目标目录路径  
        dst_dir="$dir/src/Robotic_Arm"  
          
        # 如果目标目录不存在，则创建它  
        if [ ! -d "$dst_dir" ]; then  
            mkdir -p "$dst_dir"  
        fi  
          
        # 复制文件  
        cp -r "$python_src_dir"/* "$dst_dir"  
    fi  
done
