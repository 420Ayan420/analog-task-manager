cmake_minimum_required(VERSION 3.6)

# The project name
project(led_mon)
set(TARGET "led_mon")

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_COMPILER /usr/bin/gcc CACHE PATH "")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -g" CACHE STRING "compile flags" FORCE)

## add directories
add_subdirectory(source)