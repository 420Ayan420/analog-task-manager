//
// IMPORTANT! Before using this, please use a resistor on your choosen analog gauge, high voltages (or currents) can damage them.
//

int cpuLoad;

void setup() {
  Serial.begin(9600);   // IMPORTANT! Change this baudrate to match the baudrate in the python script.
  pinMode(12, OUTPUT);  // IMPORTANT! Set this to what pin you want to use for the PWM signal. See wiring diagram for more details.
}

void loop() {
  if (Serial.available()) {
    String line = Serial.readStringUntil('\n');
    cpuLoad = line.toInt();
    updatePWM(cpuLoad);
  }
}

void updatePWM(int load) {
  int baseline = 30; // Set a baseline PWM value that ensures the gauge moves at low loads
  int maxLoad = 100;
  int pwmValue;

  if (load > 0) {
    pwmValue = map(load, 0, maxLoad, baseline, 255);
  } else {
    pwmValue = baseline; // Apply baseline even when the load is 0%
  }
  
  analogWrite(12, pwmValue);
}