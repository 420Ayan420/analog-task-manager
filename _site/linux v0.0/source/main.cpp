#include <iostream>
#include <ostream>
#include <unistd.h>  

#include <CPU.hpp>

int main()
{
    CPU cpu;
    while(true){
        cpu.print_per_cpu();
        usleep(200000);
    }
} 