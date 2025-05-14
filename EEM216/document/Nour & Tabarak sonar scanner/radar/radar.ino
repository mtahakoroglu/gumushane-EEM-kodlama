#include <Servo.h>
// Ultrasonic Sensor Pins
const int trigPin = 10;
const int echoPin = 11;
// Servo Configuration
Servo myServo;
int angle = 15;
// Measurement Variables
long duration;
int distance;
void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600); // Fixed baud rate
myServo.attach(9);
}
void loop() {
// Sweep from 15° to 165°
for(angle = 15; angle <= 165; angle++) {
myServo.write(angle);
delay(30);
distance = calculateDistance();
sendData(angle, distance);
}
// Sweep back from 165° to 15°
for(angle = 165; angle >= 15; angle--) { // Fixed loop syntax
myServo.write(angle);
delay(30);
distance = calculateDistance();
sendData(angle, distance);
}
}
int calculateDistance() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH); // Fixed function name
distance = duration * 0.034 / 2;
return distance;
}
void sendData(int angle, int distance) {
Serial.print(angle);
Serial.print("."); // Data separator
Serial.println(distance); // Line ending
}