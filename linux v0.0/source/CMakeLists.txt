include_directories(../include)

add_library(cpu SHARED CPU.cpp)

add_executable(${TARGET} main.cpp)
target_link_libraries(${TARGET} cpu)