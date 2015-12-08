@echo off
call vcvarsall amd64
cd ..\
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -G"NMake Makefiles" ..\
REM nmake zlibstatic
REM nmake
nmake bindings
nmake install_bindings
cd ..\dev