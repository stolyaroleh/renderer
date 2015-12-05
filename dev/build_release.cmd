@echo off
call vcvarsall amd64
cd ..\
mkdir build\release
cd build\release
cmake -DCMAKE_BUILD_TYPE=Release -G"NMake Makefiles" ..\..\
nmake
cd ..\..\dev