// D2'den D9'a kadar olan pinler, seçelim
int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9}; // 8 LED için pinler
int numLeds = 8; // LED sayısı
int f = 2; // frekans | saniyede kaç kere tur atsın
int delayTime = (1000/f)/(2*numLeds-2); // ms

void setup() {
  // LED pinlerini çıkış olarak ayarlıyoruz
  for (int i=0; i<numLeds; i++)
    pinMode(ledPins[i], OUTPUT);
}

void loop() {
  // LED'leri D2'den D9'a doğru yak
  for (int i=0; i<numLeds; i++) {
    digitalWrite(ledPins[i], HIGH); // LED'i yak
    delay(delayTime);
    digitalWrite(ledPins[i], LOW); // öbür LED'e geçmeden LED'i söndür
  }
  // LED'leri D9'dan D2'ye doğru geri yak (D9 ve D2 dâhil değil)
  for (int i=numLeds-2; i>0; i--) { // numLeds-2 çünkü D9 tekrar yanmamalı
    digitalWrite(ledPins[i], HIGH); // LED'i yak
    delay(delayTime);
    digitalWrite(ledPins[i], LOW); // öbür LED'e geçmeden LED'i söndür
  }
}