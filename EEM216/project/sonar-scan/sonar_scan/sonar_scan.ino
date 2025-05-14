#include <Servo.h>

Servo servo;
const int trigPin = 9;
const int echoPin = 10;
const int servoPin = 11;
const int buzzerPin = 12;  // Buzzer dijital pin
const int servoSpeed = 30;

long duration;
int distance;

void setup() {
  servo.attach(servoPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);  // Buzzer pin çıkış olarak ayarlandı
  Serial.begin(9600);
}

void loop() {
  for (int angle = 0; angle <= 180; angle++) {
    scan(angle);
  }

  for (int angle = 180; angle >= 0; angle--) {
    scan(angle);
  }
}

void scan(int angle) {
  servo.write(angle);
  delay(servoSpeed);  // Daha hızlı taramak için bu değeri düşürebilirsin

  // Mesafe ölçümü
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  // Buzzer kontrolü
  if (distance > 0 && distance < 5) {
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(buzzerPin, LOW);
  }

  // Python için seri çıkış (açı,mesafe)
  Serial.print(angle);
  Serial.print(",");
  Serial.println(distance);
}