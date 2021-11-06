#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int tmp = A0;
int Phores = A1;
int ValPhores;

void setup() {
  lcd.begin(16, 2);
  pinMode(Phores, INPUT);
  pinMode(tmp, INPUT);
}

void loop() {
  lcd.clear();
  
  ValPhores=analogRead(Phores);
  
  //Hitung suhu ke Celcius
  float celsius = (float(analogRead(tmp)) * 5 * 100 / 1024);
  
  //Tampilkan suhu pada Baris pertama LCD
  lcd.setCursor(0, 0); 
  lcd.print("Suhu: ");
  lcd.print(celsius);
  lcd.print(" C ");
  
  //Tampilkan kecerahan pada baris kedua LCD
  lcd.setCursor(0, 1);
  lcd.print("Kecerahan: ");
  lcd.print(ValPhores);
  
  delay(1024);
}
 