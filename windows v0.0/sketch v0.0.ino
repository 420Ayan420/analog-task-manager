void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);  // Start the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    float gpuTemperature = Serial.parseFloat();
    if (gpuTemperature > 51.0) {
      digitalWrite(LED_BUILTIN, HIGH);
    } else {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
