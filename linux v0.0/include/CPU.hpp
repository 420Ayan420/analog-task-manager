#include <string.h>
#include <iostream>
#include <cstdio>
#include <sys/times.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>

#include <FixedDeque.hpp> // wrapper deque class to calculate rolling average

class CPU{
    private:
        struct last_values{
            unsigned long long lastTotalUser;
            unsigned long long lastTotalUserLow;
            unsigned long long lastTotalSys;
            unsigned long long lastTotalIdle;
            FixedDeque<double,5> fd;
        };

        std::vector<last_values> vec_lv;

    public:
        CPU();
        void print_per_cpu();   // prints per core cpu usage
        void print_cpu();       // prints overall cpu usage

        std::vector<double> get_per_cpu();
        double get_cpu();

        int numProcessors;
};

