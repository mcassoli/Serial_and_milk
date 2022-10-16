//Description of setup

int LED_PIN = 13;
int incomingByte = 0; // for incoming serial data

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_PIN, HIGH);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // prints the received data
    Serial.print("Leonardo Received: ");
    Serial.println((int)incomingByte);

    if ((int)incomingByte > 100){
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else{
      analogWrite(LED_PIN, LOW);
      digitalWrite(LED_BUILTIN, LOW);

    }
  }
}
