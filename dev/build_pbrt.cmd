@echo off
setlocal
call vcvarsall x86
cd ..\
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_PBRT=ON -G"NMake Makefiles" ..\
nmake zlibstatic
nmake install
cd ..\dev