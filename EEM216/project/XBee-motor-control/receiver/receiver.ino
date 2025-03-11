#include <Servo.h>

#include <SoftwareSerial.h>

//For Atmega328P's
// XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
// XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
SoftwareSerial XBee(2, 3); // RX, TX

Servo motor;
const int motorPin = 9;
uint16_t kanalSinyali;


void setup() {
    XBee.begin(9600);
    Serial.begin(9600);
    motor.attach(motorPin);
    motor.writeMicroseconds(900); // Eğer bir sinyal yoksa hep 900us olsun
}

void loop() {

//if (XBee.available()) {
  //int value = XBee.read();
  //Serial.println(value);
  //int kanalSinyali = map(value, 0, 255, 900, 2100);
  //motor.writeMicroseconds(kanalSinyali);
//}

  
    if (XBee.available() >= 2) { // En az 3 byte gelmeden devam etme!
      XBee.readBytes((byte*)(&kanalSinyali), sizeof(kanalSinyali));
      Serial.println(kanalSinyali);
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
