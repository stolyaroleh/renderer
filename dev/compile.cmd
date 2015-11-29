@echo off
call vcvarsall amd64
cd ../
mkdir build
cd build
cmake -G"NMake Makefiles" ../
nmake
cd ../dev