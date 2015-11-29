@echo off

SET pyuic="C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat"

pushd %~dp0
cd ..

SET root_dir=%cd%
SET output_location=%root_dir%\src\python\ui_generated

rd /s /q %output_location%
mkdir %output_location%
cd %output_location%

type NUL > __init__.py

for /f %%f in ('dir /b %root_dir%\qt') do call %pyuic% %root_dir%\qt\%%f -x -o %%~nf_ui.py

popd