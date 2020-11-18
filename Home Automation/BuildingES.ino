//BuildingES.ino
int ledPin = 13; // LED connected to digital pin 13

char incomingBit;	// for incoming serial data

void setup() {
  pinMode(ledPin, OUTPUT);      // sets the digital pin as output
  Serial.begin(9600);	// opens serial port, sets data rate to 9600 bps
}
void loop() {
  if (Serial.available() > 0) {
		// read the incoming byte:
		incomingBit = Serial.read();
		// say what you got:
		//Serial.print(“I received:  “);
		Serial.println(incomingBit);
                if(incomingBit == ‘Y’) 
{
                    digitalWrite(ledPin, HIGH);    // sets the LED ON
                    delay(1000);
                }
                else {
                  digitalWrite(ledPin, LOW);   // sets the LED OFF
					  delay(1000);
                }
	}
}
