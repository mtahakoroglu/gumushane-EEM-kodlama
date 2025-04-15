#define trigPin 9
#define echoPin 10
#define redLedPin 6
#define greenLedPin 7
#define buzzerPin 8

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  long duration;
  int distance;
  // Trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Read echo and calculate distance in cm
  duration = pulseIn(echoPin, HIGH);// returns time in microseconds
  //  The speed of sound in air is indeed ~340 m/s (34,000 cm/s)
  //  The time it takes for the sound to travel to the object and back is divided by 2
  //  to get the one-way distance.
  //  The distance is then calculated as distance = (duration / 2) * speed of sound
  //  or simplified to distance = duration / 58 (since speed of sound is ~340 m/s)
  distance = duration / 58;
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  // Control LEDs and Buzzer
  if (distance > 5) {
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(redLedPin, LOW);
    digitalWrite(buzzerPin, LOW);
  }
  else {
    digitalWrite(greenLedPin, LOW);
    digitalWrite(redLedPin, HIGH);
    digitalWrite(buzzerPin, HIGH); // Turn on buzzer
  }
  delay(50); // small delay
}