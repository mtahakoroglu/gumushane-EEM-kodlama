#include <Servo.h>
Servo motor;
int analogPin = A2;

void setup() {
  motor.attach(9);
  Serial.begin(9600);
}

void loop() {
   int x = analogRead(analogPin);
   int y = map(x, 0, 1023, 0, 180);
   //int z = map(x, 0, 1023, 900, 2100);
   motor.write(y);
   //motor.writeMicroseconds(z);
   Serial.print("PWM signal (us): ");
   Serial.println(y);
}