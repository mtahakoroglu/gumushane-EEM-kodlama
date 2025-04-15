void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop() {
  int delayTime = analogRead(A0);
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW);
  delay(delayTime);
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  delay(delayTime);
}
