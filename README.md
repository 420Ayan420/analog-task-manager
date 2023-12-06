# version v0.1 Released! Check below and (Releases)[https://github.com/420Ayan420/analog-task-manager/releases].

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
├── OpenHardwareMonitorLib.dll      # available through their source code
├── OpenHardwareMonitorLib.sys      # auto-produced
├── sketch v0.0.ino                 # arduino sketch 
└── ProgramMain v0.0.py             # feasibility analysis
```
See the following video for a demonstration of this code, the top LED lights up when the temperature exceed 51°C.

https://github.com/420Ayan420/analog-task-manager/assets/88883638/63c14dab-c670-4c56-806e-0af1d9d13348

## version v0.1
This release contains basic functionality where:
1. Takes CPU load and temperature values for AMD and Intel CPUs
2. Takes GPU load and temperature values for AMD and Nvidia GPUs
3. Displays these readings as text
4. Sends them to Arduino for sending to electronics
5. Has a GUI so that it easy to change COM, baudrate, and readrate

```
analog task manager
├── v0.0                            # version v0.0
|   ├── OpenHardwareMonitorLib.dll      # available through their source code
|   ├── OpenHardwareMonitorLib.sys      # auto-produced
|   ├── sketch v0.0.ino                 # arduino sketch 
|   └── ProgramMain v0.0.py             # feasibility analysis
├── v0.1                            # version v0.1
|   ├── OpenHardwareMonitorLib.dll      # available through their source code
|   ├── OpenHardwareMonitorLib.sys      # auto-produced
|   ├── Wiring Diagram v0.1.png         # diagram for electronic circuit
|   ├── sketch v0.1.ino                 # arduino sketch 
|   └── ProgramMain v0.1.py             # feasibility analysis
├── LICENSE.md
└── README.md
```

This is a generalized solution and should work on any Windows computer, the python script (or in this case the .exe) sends data as a single line string which can then be decoded on the Arduino side. **CPU temperature values are only accessible if the program is run as administrator on windows, this is due to to how windows handles this temperature reading.**

https://github.com/420Ayan420/analog-task-manager/assets/88883638/2d228a02-a99e-4825-95ec-60477e4ea5f8

Setup instructions as follows below.

## setup instructions
## version v0.0
This build has no executable program.

## version v0.1
1.  Prepare electronic circuit as shown in the `Wiring Diagram v0.1.png`
2.  Download and install [Arduino IDE](https://www.arduino.cc/en/software)
3.  Place `sketch v0.1.ino` into the Arduino IDE
4.  Connect to your Arduino (doesn't have to be Mega2560) and note the communication port as COMn and baudrate as x, where x and n are a positive integer values.
5.  Upload the sketch
6.  Open `ProgramMain v0.1.exe` and input the same baudrate and COM port as noted from the Arduino IDE
7.  Press read, the RX LED on your Arduino should start flashing and a voltage will be applied on PWM Digital Pin 12 (or the one that you decided on in the code)

# build instructions
## version v0.0
1.  Use visual studio code for python script and Arduino IDE for Arduino code.
2.  Install libraries using:
    1.  pip install pythonnet
    2.  pip install pyserial
4.  Upload `sketch v0.0.ino` to your arduino using Arduino IDE
5.  Run python script as administrator through terminal to ensure that CPU readings are read properly. (not required for anything other than CPU temperatures) by using `python 'ProgramMain v0.0.py'`. Ensure that the COM port in the script matches the COM port in the Arduino IDE.

## version v0.1
## version v0.0
1.  Use visual studio code for python script and Arduino IDE for Arduino code.
2.  Install libraries using:
    1.  pip install pythonnet
    2.  pip install pyserial
4.  Upload `sketch v0.1.ino` to your arduino using Arduino IDE
5.  Following `Wiring Diagram v0.1.png` to connect up Arduino
6.  Run python script as administrator through terminal to ensure that CPU readings are read properly. (not required for anything other than CPU temperatures) by using `python 'ProgramMain v0.1.py'`. Ensure that the COM port in the script matches the COM port in the Arduino IDE.