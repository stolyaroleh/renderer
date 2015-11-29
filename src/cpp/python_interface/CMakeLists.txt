cmake_minimum_required(VERSION 3.0)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

set(PYBIND_INCLUDE_DIR "${LIBS}/pybind11/include")
message(STATUS "PYTHON_INCLUDE_DIRS: ${PYTHON_INCLUDE_DIRS}")
message(STATUS "CMAKE_BUILD_DIRECTORY: ${CMAKE_BUILD_DIRECTORY}")
message(STATUS "PYBIND_INCLUDE_DIR: ${PYBIND_INCLUDE_DIR}")

include_directories(${PYBIND_INCLUDE_DIR})
include_directories(${PYTHON_INCLUDE_DIRS})

add_library(example SHARED test.cpp)
target_link_libraries(example ${PYTHON_LIBRARIES})
