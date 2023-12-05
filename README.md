# version v0.1 to be released soon™, preview below
https://github.com/420Ayan420/analog-task-manager/assets/88883638/63c6c09d-1d9d-4b19-8ece-d5b362b19ff9

# analog-task-manager
Let's make a Analog task manager that allows us to display the CPU core loads, CPU core temperatures, CPU power consumption, GPU load, GPU temperature, GPU power consumption, and memory usage.

We need you! Whilst I have the necessary skills to complete this project, I do not have the time so I am looking for contributors so that this project can really reach a good level of completeness and so that we may all enjoy it.

# overall scope and timeline of project
1.  Software
    1.  Create a script to read all relevant readings from from WMI (windows management instrumentation)
    2.  Parse and process this data into a useful voltage value
    3.  Send this processed data to an Arduino so that it can be used to control analog gauges. Also add basic code to add color changing lights.
2.  Hardware
    1. Take this data and send it properly to the relevant gauge using the digital PWM pins on the Arduino Mega2560.
    2. Use digital I/O pins to control the RGB lights for each gauge so that it can be red/yellow/green for the status of the gauge.
    3. Add in 2 toggle switches for ON/OFF for the reading on the gauge and the backlight on the gauge.
    4. Add a variable resistor dimmer switch for each gauge backlight.
3.  Nice-to-haves
    1. Nice casing that is curved and matches the curve of your eyes just like a curved monitor does.
    2. Make it sit low so it does not cover a large portion of desk space.
    3. Make it modular so additional gauge clusters can be added without having to change the frame. Use magnets and contact connectors such as 4-pin headphone jacks to connect for power and data.
    4. Perhaps make a program/software that can easily adapt to each system and allow the user to program what each gauge does.
    5. Add a small LCD on the gauge to allow user to change the name of the purpose of each gauge easily and without fuss.

# what's been done so far
## version v0.0
1. Feasibility analysis as proof of concept of pipeline. [see here for more information](https://ayanali.net/projects/2023-12-3-analog-task-manager/)
```
analog task manager
├── OpenHardwareMonitorLib.dll      # available through their source code.
├── OpenHardwareMonitorLib.sys      # auto-produced
├── sketch v0.0.ino                 # arduino sketch 
└── ProgramMain v0.0.py             # feasibility analysis
```
See the following video for a demonstration of this code, the top LED lights up when the temperature exceed 51°C.

https://github.com/420Ayan420/analog-task-manager/assets/88883638/63c14dab-c670-4c56-806e-0af1d9d13348

# build instructions
## version v0.0
1.  Use visual studio code for python script and Ardiuno IDE for Ardiuno code.
2.  Install libraries using:
    1.  pip install pythonnet
    2.  pip install pyserial
4.  Upload `sketch v0.0.ino` to your arduino using Arduino IDE
5.  Run python script as administrator through terminal to ensure that CPU readings are read properly. (not required for anything other than CPU temperatures) by using `python 'ProgramMain v0.0.py'`. Ensure that the COM port in the script matches the COM port in the Arduino IDE.
