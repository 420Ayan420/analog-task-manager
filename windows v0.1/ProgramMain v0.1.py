import clr      # IMPORTANT! pip install pythonnet, NOT pip install clr
import serial   # IMPORTANT! pip install pyserial
import time     
import psutil   # IMPORTANT! pip install psutil

import tkinter as tk
import webbrowser
from threading import Thread

clr.AddReference('OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer, HardwareType, SensorType

def open_link(url):
    webbrowser.open_new(url)

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Analog Task Manager v0.1")
        master.geometry("325x450")

        # COM port entry
        self.label_com = tk.Label(master, text="COM Port (e.g. COM4):")
        self.label_com.pack()
        self.entry_com = tk.Entry(master)
        self.entry_com.pack()

        # Baud rate entry
        self.label_baud = tk.Label(master, text="Baud Rate (e.g. 9600):")
        self.label_baud.pack()
        self.entry_baud = tk.Entry(master)
        self.entry_baud.pack()

        # Update interval entry
        self.label_interval = tk.Label(master, text="Update Interval (seconds):")
        self.label_interval.pack()
        self.entry_interval = tk.Entry(master)
        self.entry_interval.pack()

        # Button Frame
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(fill=tk.X, expand=True)

        # Read button
        self.read_button = tk.Button(self.button_frame, text="Read", command=self.start_reading)
        self.read_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Stop button
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_reading)
        self.stop_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Text widget for displaying readings
        self.readings_display = tk.Text(master, height=9, width=50)  # Increased height
        self.readings_display.pack()
        
        # Help link
        self.help_text = tk.Text(master, height=3, width=50, bg=master.cget("bg"), relief=tk.FLAT, cursor="arrow")
        self.help_text.insert(tk.END, "Need Help? Want to check out the code? All available ")
        self.help_text.insert(tk.END, "here", "link")
        self.help_text.insert(tk.END, ".")
        self.help_text.tag_config("link", foreground="blue", underline=1)
        self.help_text.tag_bind("link", "<Button-1>", lambda e: open_link("https://github.com/420Ayan420/analog-task-manager"))
        self.help_text.config(state=tk.DISABLED)
        self.help_text.pack()

        # Credits link
        self.credits_text = tk.Text(master, height=4, width=50, bg=master.cget("bg"), relief=tk.FLAT, cursor="arrow")
        self.credits_text.insert(tk.END, "Produced by Ayan @ ")
        self.credits_text.insert(tk.END, "ayanali.net", "link")
        self.credits_text.insert(tk.END, ", contributing to the open-source code and getting the word out helps Ayan work on projects like these for longer.")
        self.credits_text.tag_config("link", foreground="blue", underline=1)
        self.credits_text.tag_bind("link", "<Button-1>", lambda e: open_link("http://ayanali.net"))
        self.credits_text.config(state=tk.DISABLED)
        self.credits_text.pack()

        self.reading = False

    def start_reading(self):
        if not self.reading:
            self.reading = True
            com_port = self.entry_com.get()
            baud_rate = int(self.entry_baud.get())
            interval = float(self.entry_interval.get())
            self.thread = Thread(target=self.read_data, args=(com_port, baud_rate, interval))
            self.thread.start()

    def stop_reading(self):
        self.reading = False
        self.thread.join()

    def read_data(self, com_port, baud_rate, interval):
        ser = serial.Serial(com_port, baud_rate, timeout=1)
        c = Computer()
        c.CPUEnabled = True
        c.GPUEnabled = True
        c.Open()
        num_cores = psutil.cpu_count(logical=False)

        while self.reading:
            for hardware_item in c.Hardware:
                if hardware_item.HardwareType == HardwareType.CPU:
                    hardware_item.Update()
                    temperatures = []
                    loads = []

                    for sensor in hardware_item.Sensors:
                        if sensor.SensorType == SensorType.Temperature:
                            temperatures.append(sensor.Value)
                        elif sensor.SensorType == SensorType.Load:
                            loads.append(sensor.Value)

                    for i in range(num_cores):
                        temp_str = f"{temperatures[i]:.1f}°C" if temperatures[i] is not None else "N/A"
                        load_str = f"{loads[i+1]:.1f}%" if loads[i+1] is not None else "N/A"
                        self.update_display(f"Core {i+1}: Temp = {temp_str}, Load = {load_str}")

                    cpu_total_load = f"{loads[0]:.1f}%" if loads[0] is not None else "N/A"
                    cpu_package_temp = f"{temperatures[-1]:.1f}°C" if temperatures[-1] is not None else "N/A"
                    self.update_display(f"CPU Total Load: {cpu_total_load}")
                    self.update_display(f"CPU Package Temp: {cpu_package_temp}")

                    load_readings = ','.join(f"{l:.1f}" for l in loads if l is not None)
                    ser.write((load_readings + "\n").encode())

                    self.update_display("-" * 40)

                    break

            time.sleep(interval)

    def update_display(self, message):
        self.readings_display.insert(tk.END, message + "\n")
        self.readings_display.see(tk.END)

# Create the main window
root = tk.Tk()
app = MainGUI(root)
root.mainloop()
