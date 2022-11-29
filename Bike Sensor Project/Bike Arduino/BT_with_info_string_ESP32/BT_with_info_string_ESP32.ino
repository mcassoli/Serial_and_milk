#define echoPin 32
#define trigPin 33
#define LEDPin 25

#include "BluetoothSerial.h"

long duration;
int distance;
int DIST_THRESH = 15;

BluetoothSerial SerialBT;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(LEDPin, OUTPUT);

  Serial.begin(9600);
  Serial.println('ESP32s testing!');
  SerialBT.begin("ESPTest");
  Serial.println("BT began!");


}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  String dstring = String(distance);

  String bike_status = "AVAILABLE\n";

  if(distance < DIST_THRESH){
    digitalWrite(LEDPin, HIGH);
    bike_status = "NOT AVAILABLE\n";
  }else{
    digitalWrite(LEDPin, LOW);
  }

  Serial.print(dstring);
  Serial.println();
  bike_status += distance;
  SerialBT.print(bike_status);

  delay(20);
}