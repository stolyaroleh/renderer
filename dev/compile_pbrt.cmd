@echo off
call vcvarsall amd64
cd ..
mkdir build
cd build
cmake -G"NMake Makefiles" ../src/cpp/pbrt-v3/
nmake
cd ../dev