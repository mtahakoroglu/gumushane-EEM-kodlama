const int pwmPin = 2; // PWM sinyali üreteceğimiz bacak
const int potPin = A0; // Potansiyometre girişi
const int f = 1000; // PWM sinyali frekansı (Hz)

void setup() {
  pinMode(pwmPin, OUTPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin); // 0-1023 arası değer
  int dutyCycle = map(potValue, 0, 1023, 0, 255); // PWM için 0-255 arası
  analogWrite(pwmPin, dutyCycle); // PWM sinyali oluştur
  Serial.print("Duty Cycle %");
  Serial.println(map(dutyCycle, 0, 255, 0, 100)); 
  delay(1000/f);
}