cmake_minimum_required(VERSION 3.0)

project(Renderer)

set(CMAKE_BUILD_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/build)

add_subdirectory(src/cpp/pbrt-v3)

#set(LIBS "${CMAKE_CURRENT_SOURCE_DIR}/libs")

#set(BISON_EXECUTABLE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/win_flex_bison/win_bison.exe)
#set(FLEX_EXECUTABLE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/win_flex_bison/win_flex.exe)

#add_subdirectory(src/cpp/python_interface)
