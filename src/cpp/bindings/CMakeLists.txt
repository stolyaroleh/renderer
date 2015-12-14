cmake_minimum_required(VERSION 3.0)

IF(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11)")
ENDIF()

find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})

add_library(bindings SHARED api.cpp ParamSetProxy.h ParamSetProxy.cpp)
target_link_libraries(bindings ${PYTHON_LIBRARIES} ${pbrt} ${OPENEXR_LIBS})

add_custom_target(install_bindings
        COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/bindings.dll ${CMAKE_CURRENT_SOURCE_DIR}/../../python/pbrt.pyd
)

add_custom_target(install_exr_converter
        COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_PREFIX}/bin/hdrtoldr.exe ${CMAKE_CURRENT_SOURCE_DIR}/../../python/hdrtoldr.exe
)