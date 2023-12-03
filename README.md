# analog-task-manager
Let's make a Analog task manager inspired that allows us to display the CPU core loads, CPU core temperatures, CPU power consumption, GPU load, GPU temperature, GPU power consumption, and memory usage.

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
1. Feasiblity analysis as proof of concept of pipeline.

# build instructions
## version v0.0
1.  Use visual studio code for python script and Ardiuno IDE for Ardiuno code.
2.  Install libraries using:
    1.  pip install pythonnet
    2.  pip install pyserial
3.  Run python script as administrator through terminal to ensure that CPU readings are read properly. (not required for anything other than CPU temperatures)
