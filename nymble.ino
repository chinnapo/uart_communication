#include <EEPROM.h>

#define BAUD_RATE 2400

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {
  char receivedData;
  unsigned long startTime, endTime;
  while (Serial.available() > 0) {
    startTime = micros(); 

    receivedData = Serial.read();
    EEPROM.write(0, receivedData);
    

    endTime = micros(); 
    printTransmissionSpeed(endTime - startTime);
  }
  
  for (int i = 0; i < EEPROM.length(); i++) {
    startTime = micros(); 
    char data = EEPROM.read(i);
    Serial.write(data);

    endTime = micros(); 
    printTransmissionSpeed(endTime - startTime);
  }
}

void printTransmissionSpeed(unsigned long duration) {
 
  float speed = 8.0 / ((float)duration / 1000000.0);
  Serial.print("Speed: ");
  Serial.print(speed, 2);
  Serial.println(" bits/second");
}
