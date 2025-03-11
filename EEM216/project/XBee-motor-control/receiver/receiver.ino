#include <Servo.h>

Servo motor;
const int motorPin = 9;
uint16_t kanalSinyali;

void setup() {
  Serial.begin(9600);
  motor.attach(motorPin);
  motor.writeMicroseconds(900); // sinyal yoksa bunu uygula
}

void loop() {
  if (Serial.available()) {
    Serial.readBytes((byte*)(&kanalSinyali), sizeof(kanalSinyali));
    motor.writeMicroseconds(kanalSinyali);
  }
}
