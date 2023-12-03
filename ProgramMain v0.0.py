import clr #IMPORTANT! pip install pythonnet, NOT pip install clr
import serial
import time

clr.AddReference('OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer, SensorType

ser = serial.Serial('COM4', 9600, timeout=1)

c = Computer()
c.CPUEnabled = True
c.GPUEnabled = True
c.Open()

while True:
    c.Hardware[1].Update()  # Update the hardware info
    for sensor in c.Hardware[1].Sensors:
        if sensor.SensorType == SensorType.Temperature and sensor.Value is not None:
            temperature = sensor.Value
            print("GPU Temp is:", temperature).
            ser.write(f"{temperature}\n".encode())