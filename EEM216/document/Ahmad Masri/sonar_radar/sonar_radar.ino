#include <Servo.h> 
const int trigPin = 4;
const int echoPin = 3;
long zaman;
int x; // ölçülen mesafe
Servo servoMotor;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  Serial.begin(57600);
  servoMotor.attach(9);
}

void loop() {
  // 15-165 derece arasını 1 derece hassasiyetle tara
  for(int i=15;i<=165;i++) {  
    servoMotor.write(i);
    delay(30);
    x = mesafeHesap();
    Serial.print(i); 
    Serial.print(","); 
    Serial.print(distance);
    Serial.print(".");
  }
  // 165-15 derece arasını 1 derece hassasiyetle tara
  for(int i=165;i>15;i--) {  
    servoMotor.write(i);
    delay(30);
    x = mesafeHesap();
    Serial.print(i);
    Serial.print(",");
    Serial.print(x);
    Serial.print(".");
  }
}

int mesafehesap() {
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  zaman = pulseIn(echoPin, HIGH); 
  mesafe = zaman*0.034/2;
  return mesafe;
}