#include <SoftwareSerial.h>
SoftwareSerial XBee(2, 3); // RX = 2, TX = 3

void setup() {
    XBee.begin(9600);
    Serial.begin(9600);
}

void loop() {
    int potDegeri = analogRead(A0);
    uint16_t kanalSinyali = map(potDegeri, 0, 1023, 900, 2100);
    Serial.println(kanalSinyali);
    //XBee.write(kanalSinyali);
    //XBee.write('h'); // Başlangıç karakteri
    XBee.write((byte*)(&kanalSinyali), sizeof(kanalSinyali));
    delay(50);
}
