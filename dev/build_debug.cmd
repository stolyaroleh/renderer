@echo off
call vcvarsall amd64
cd ..\
mkdir build\debug
cd build\debug
cmake -DCMAKE_BUILD_TYPE=Debug -G"NMake Makefiles" ..\..\
nmake
cd ..\..\dev