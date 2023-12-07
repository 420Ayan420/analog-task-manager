from ctypes import *
import ctypes
import time

libcpu = cdll.LoadLibrary('build/src/libcpu.so')
multicore = True

class LinuxCPU():
    def __init__(self):
        libcpu.create_CPU.restype = ctypes.c_void_p

        self.obj = libcpu.create_CPU()

    def __del__(self):
        libcpu.delete_CPU(self.obj)

    # prints cpu usage to stdout
    def printCPU(self):
        libcpu.print_CPU()

    # prints per cpu usage to stdout
    def printPerCPU(self):
        libcpu.print_Per_CPU()

    def getNumCPU(self):
        return libcpu.get_Num_CPU()
    
    # return c double/python float
    def getCPU(self):
        tmp = libcpu.get_CPU
        tmp.restype = ctypes.c_double
        return libcpu.get_CPU()
    
    # return list of CPU usage
    def getPerCPU(self):
        tmp = libcpu.get_Per_CPU
        tmp.argtypes = ()
        tmp.restype = ctypes.POINTER(ctypes.c_double)

        # convert c style array into python list
        d_array = tmp(self.getNumCPU())
        d_list = (d_array[i] for i in range(self.getNumCPU()))

        # delete double pointer otherwise memory leak
        self.deletePerCPU(d_array)

        return d_list
    
    def deletePerCPU(self, obj):
        libcpu.delete_Per_CPU(obj)

if __name__ == "__main__":
    # initialize cpu object
    cpu = LinuxCPU()

    while True:
        if multicore:
            data = cpu.getPerCPU()
            for i in data:
                print(i)
            time.sleep(.2)

        else:
            data = float(cpu.getCPU())
            print(data)
            time.sleep(.2)
