#include <Servo.h>

#include <SoftwareSerial.h>

Servo motor;
const int motorPin = 9;
uint16_t kanalSinyali;


void setup() {
    Serial.begin(9600);
    Serial.begin(9600);
    motor.attach(motorPin);
    motor.writeMicroseconds(900); // Eğer bir sinyal yoksa hep 900us olsun
}

void loop() {
  if (Serial.available() >= 2) { // En az 2 byte gelmeden devam etme!
    Serial.readBytes((byte*)(&kanalSinyali), sizeof(kanalSinyali));
    //Serial.println(kanalSinyali);
    motor.writeMicroseconds(kanalSinyali); // Motor hızını güncelle
        //if (XBee.read() == 'h') { // Başlangıç baytı 'h' olmalı
            //while (XBee.available() < 2); // 2 byte tamamen gelene kadar bekle

            //int highByte = XBee.read(); // İlk byte (yüksek byte)
            //int lowByte = XBee.read();  // İkinci byte (düşük byte)

            /*if (highByte != -1 && lowByte != -1) { // Geçerli veri kontrolü
                uint16_t kanalSinyali = (highByte << 8) | lowByte; // İki byte'ı birleştir
                Serial.println(kanalSinyali);
                motor.writeMicroseconds(kanalSinyali); // Motor hızını güncelle
            }*/
    }
}
