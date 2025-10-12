#include <Wire.h>
#include <MPU6050_light.h>
#include <LiquidCrystal.h>

// LCD başlatma: (RS, EN, D4, D5, D6, D7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

MPU6050 mpu(Wire);

const int ledPin = 8;
const int buzzerPin = 9;
const float threshold = 0.1; // ayarlanabilir eşik

void setup() 
{
  Serial.begin(9600);
  Wire.begin();
  lcd.begin(16, 2); // 16 sütunlu, 2 satırlı LCD
  lcd.clear();
  lcd.print("Starting...");

  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while (status != 0) {
    lcd.setCursor(0, 1);
    lcd.print("Sensor error!");
    delay(500);
  }

  mpu.calcOffsets();// kalibrasyon
  lcd.clear();
  lcd.print("Ready to detect");
}

void loop() 
{
  mpu.update();

  float ax = mpu.getAccX();
  float ay = mpu.getAccY();
  float az = mpu.getAccZ();

  float magnitude = sqrt(ax * ax + ay * ay + az * az);

  Serial.println(magnitude);

  if (abs(magnitude - 1.0) > threshold) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(buzzerPin, HIGH);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("IN EARTHQUAKE");
    lcd.setCursor(0, 1);
    lcd.print("APPROACHING!!!");
  } else {
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Calm");
    lcd.setCursor(0, 1);
    lcd.print("No shaking");
  }

  delay(2000);
}


