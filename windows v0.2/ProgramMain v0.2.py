import clr      # IMPORTANT! pip install pythonnet, NOT pip install clr
import serial   # IMPORTANT! pip install pyserial
import time     
import psutil   # IMPORTANT! pip install psutil

import tkinter as tk
import webbrowser
from threading import Thread

import pystray  # IMPORTANT! pip install pystray
from PIL import Image, ImageDraw
from pystray import MenuItem as item
import os
import sys

clr.AddReference('OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer, HardwareType, SensorType

def open_link(url):
    webbrowser.open_new(url)

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle([width // 2, 0, width, height // 2], fill=color2)
    dc.rectangle([0, height // 2, width // 2, height], fill=color2)
    return image

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Analog Task Manager v0.1")
        master.geometry("325x450")

        self.label_com = tk.Label(master, text="COM Port (e.g. COM4):")
        self.label_com.pack()
        self.entry_com = tk.Entry(master)
        self.entry_com.pack()

        self.label_baud = tk.Label(master, text="Baud Rate (e.g. 9600):")
        self.label_baud.pack()
        self.entry_baud = tk.Entry(master)
        self.entry_baud.pack()

        self.label_interval = tk.Label(master, text="Update Interval (seconds):")
        self.label_interval.pack()
        self.entry_interval = tk.Entry(master)
        self.entry_interval.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(fill=tk.X, expand=True)

        self.read_button = tk.Button(self.button_frame, text="Read", command=self.start_reading)
        self.read_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_reading)
        self.stop_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.readings_display = tk.Text(master, height=9, width=50)
        self.readings_display.pack()
        
        self.help_text = tk.Text(master, height=3, width=50, bg=master.cget("bg"), relief=tk.FLAT, cursor="arrow")
        self.help_text.insert(tk.END, "Need Help? Want to check out the code? All available ")
        self.help_text.insert(tk.END, "here", "link")
        self.help_text.insert(tk.END, ".")
        self.help_text.tag_config("link", foreground="blue", underline=1)
        self.help_text.tag_bind("link", "<Button-1>", lambda e: open_link("https://github.com/420Ayan420/analog-task-manager"))
        self.help_text.config(state=tk.DISABLED)
        self.help_text.pack()

        self.credits_text = tk.Text(master, height=4, width=50, bg=master.cget("bg"), relief=tk.FLAT, cursor="arrow")
        self.credits_text.insert(tk.END, "Produced by Ayan @ ")
        self.credits_text.insert(tk.END, "ayanali.net", "link")
        self.credits_text.insert(tk.END, ", contributing to the open-source code and getting the word out helps Ayan work on projects like these for longer.")
        self.credits_text.tag_config("link", foreground="blue", underline=1)
        self.credits_text.tag_bind("link", "<Button-1>", lambda e: open_link("http://ayanali.net"))
        self.credits_text.config(state=tk.DISABLED)
        self.credits_text.pack()

        self.reading = False

        self.master.protocol("WM_DELETE_WINDOW", self.hide_window)

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
                hardware_item.Update()
                for sensor in hardware_item.Sensors:
                    self.update_display(f"{hardware_item.Name} {sensor.Name}: {sensor.Value} {sensor.SensorType}")
            time.sleep(interval)

    def update_display(self, message):
        self.readings_display.insert(tk.END, message + "\n")
        self.readings_display.see(tk.END)

    def hide_window(self):
        self.master.withdraw()
        icon.run()

    def show_window(self, icon, item):
        icon.stop()
        self.master.after(0, self.master.deiconify)

    def exit_program(self, icon, item):
        icon.stop()
        self.master.destroy()

# Create system tray icon
icon = pystray.Icon("ATM", create_image(64, 64, 'black', 'blue'), "Analog Task Manager")
icon.menu = pystray.Menu(
    item('Show ATM', lambda icon, item: app.show_window(icon, item)),
    item('Close ATM', lambda icon, item: app.exit_program(icon, item))
)

# Create the main window
root = tk.Tk()
app = MainGUI(root)
root.mainloop()
