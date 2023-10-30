#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
const int iPin = 8;

Servo servo;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  servo.attach(9);
  pinMode(iPin,INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'O') {
      // Open the door (adjust servo position)
      servo.write(90); // You may need to adjust this angle
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Access Granted");
      delay(3000);
      int ir_out;
  ir_out=digitalRead(iPin);
      if (ir_out==HIGH)
  {
    lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Door closing");
          lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Thanks");
  }
  delay(5000);
      
      
    } else if (command == 'C') {
      // Close the door (reset servo position)
      servo.write(0);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Access Denied");
      delay(5000);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Thanks");
    }
  }
  
 
}