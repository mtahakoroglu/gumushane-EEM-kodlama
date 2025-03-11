void setup() {
    Serial.begin(9600);
}

void loop() {
    int potDegeri = analogRead(A0);
    uint16_t kanalSinyali = map(potDegeri, 0, 1023, 900, 2100);
    Serial.write((byte*)(&kanalSinyali), sizeof(kanalSinyali));
    delay(20);
}