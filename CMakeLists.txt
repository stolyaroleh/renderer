cmake_minimum_required(VERSION 3.0)

project(Renderer)

set(CMAKE_BUILD_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/build)
set(CMAKE_INSTALL_PREFIX  ${CMAKE_CURRENT_SOURCE_DIR}/install)

if (${BUILD_PBRT})
    add_subdirectory(pbrt-v3)
ELSE(${BUILD_PBRT})
    include_directories(src)
    include_directories(pbrt-v3/src)
    include_directories(libs/pybind11/include)

    find_library(pbrt NAMES libpbrt.lib PATHS install/lib REQUIRED)
    find_library(IlmImf NAMES IlmImf.lib PATHS install/lib REQUIRED)
    find_library(Imath NAMES Imath.lib PATHS install/lib REQUIRED)
    find_library(Iex NAMES Iex.lib PATHS install/lib REQUIRED)
    find_library(IexMath NAMES IexMath.lib PATHS install/lib REQUIRED)
    find_library(IlmThread NAMES IlmThread.lib PATHS install/lib REQUIRED)
    find_library(Half NAMES Half.lib PATHS install/lib REQUIRED)
    find_library(zlibstatic NAMES zlibstatic.lib PATHS install/lib REQUIRED)

    set(OPENEXR_LIBS ${IlmImf} ${Imath} ${Half} ${Iex} ${IexMath} ${IlmThread} ${zlibstatic})

    add_subdirectory(src/cpp/bindings)
ENDIF(${BUILD_PBRT})