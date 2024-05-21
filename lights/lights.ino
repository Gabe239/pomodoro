const int ledPin_1 = 10;  
const int ledPin_2 = 12;

void setup() {
    pinMode(ledPin_1, OUTPUT);
    digitalWrite(ledPin_2, LOW);
    digitalWrite(ledPin_1, LOW); 
    Serial.begin(9600);     
}

void loop() {
    if (Serial.available() > 0) {
        char receivedChar = Serial.read();
        if (receivedChar == 'S') {
            digitalWrite(ledPin_2, HIGH);  
            digitalWrite(ledPin_1, LOW);  
        } else if (receivedChar == 'E') {
            digitalWrite(ledPin_2, LOW); 
            digitalWrite(ledPin_1, HIGH);   
        }
    }
}
