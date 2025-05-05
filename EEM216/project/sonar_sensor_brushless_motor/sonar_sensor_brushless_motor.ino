#include <Servo.h>

#define TRIG_PIN 9
#define ECHO_PIN 10

Servo motor;

void setup() {
  Serial.begin(9600); // Start serial communication for debugging
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  motor.attach(3);
}

void loop() {
  // Measure the distance using the ultrasonic sensor
  long duration, distance;
  // Trigger the sensor
  digitalWrite(TRIG_PIN, LOW);  
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  // Read the echo pin
  duration = pulseIn(ECHO_PIN, HIGH);
  // Calculate the distance in cm (speed of sound is ~ 343 m/s)
  distance = duration * 0.034 / 2;
  // Map the distance to motor speed
  uint16_t motorSpeed = map(distance, 10, 500, 900, 2100);
  motor.writeMicroseconds(motorSpeed);
  // Print distance for debugging
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm, Motor Speed: ");
  Serial.println(motorSpeed);
  delay(20);
}