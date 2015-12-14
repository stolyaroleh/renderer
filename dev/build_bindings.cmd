@echo off
setlocal
call vcvarsall x86
cd ..\
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_PBRT=OFF -G"NMake Makefiles" ..\
nmake bindings
nmake install_bindings
nmake install_exr_converter
cd ..\dev