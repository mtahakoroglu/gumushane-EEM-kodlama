const int ledPins[] = {3, 4, 5, 6, 7, 8, 9, 10};
const int numLeds = 8;
const int buttonPin = 2;

int currentLed = 0; // Su anki LED konumu
int direction = 1; // 1: ileri, -1: geri
bool flashing = true; // LED yanip sonme durumu
int buttonState; // Mevcut buton durumu
int lastButtonState = HIGH; 
unsigned long lastDebounceTime = 0;  
const unsigned long debounceDelay = 50;  
int f = 4; 
unsigned long delayTime = (1000 / f) / (2 * numLeds - 2); 
unsigned long previousMillis = 0;  

void setup() {
  for (int i = 0; i < numLeds; i++) pinMode(ledPins[i], OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  buttonState = digitalRead(buttonPin);
}

void loop() {
  int reading = digitalRead(buttonPin);

  // Debounce kontrolu
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == LOW) {
        flashing = !flashing;  // Butona basildiginda durdur/baslat
      }
    }
  }

  lastButtonState = reading;

  // Eger flashing aktifse ve zaman dolduysa LED guncelle
  if (flashing && (millis() - previousMillis >= delayTime)) {
    previousMillis = millis();

    // Onceki LED'i sondur
    for (int i = 0; i < numLeds; i++) digitalWrite(ledPins[i], LOW);

    // Su anki LED'i yak
    digitalWrite(ledPins[currentLed], HIGH);

    // Sonraki LED'i belirle
    currentLed += direction;

    // Uclara ulastiginda yon degistir
    if (currentLed >= numLeds) {
      currentLed = numLeds - 2;
      direction = -1;
    } else if (currentLed < 0) {
      currentLed = 1;
      direction = 1;
    }
  }
}
