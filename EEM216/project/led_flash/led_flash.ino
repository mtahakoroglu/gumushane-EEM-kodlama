#define LED_PIN 8

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // LED'i yak
  delay(100);
  digitalWrite(LED_PIN, LOW); // LED'i yak
  delay(1900);
}