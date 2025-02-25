const int pwmPin = 9; // PWM çıkışı
const int potPin = A0; // Potansiyometre girişi
const int f = 1000; // Hz 

void setup() {
  pinMode(pwmPin, OUTPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin); // 0-1023 arası değer
  int dutyCycle = map(potValue, 0, 1023, 0, 255); // PWM için 0-255 arası
  analogWrite(pwmPin, dutyCycle); // Duty cycle ayarla
  Serial.print("Duty Cycle: ");
  Serial.print(map(dutyCycle, 0, 255, 0, 100)); 
  Serial.println("%");
  delay(1000/f); // 1 ms periyot (1 kHz frekans)
}