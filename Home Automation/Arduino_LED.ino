//Arduino_LED.ino
int ledPin = 13;                 // LED connected to digital pin 13

void setup() {
  pinMode(ledPin, OUTPUT);      // sets the digital pin as output
  Serial.begin(9600);	// opens serial port, sets data rate to 9600 bps
}
void loop() {
  digitalWrite(ledPin, LOW);   // sets the LED on
  delay(1000);                  // waits for a second
  digitalWrite(ledPin, LOW);    // sets the LED off
  delay(1000);                  // waits for a second
}
