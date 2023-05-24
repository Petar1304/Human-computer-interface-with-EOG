


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  String data = "";
  // read the input on analog pin 0:
  int ch1 = analogRead(A0);
  // int ch2 = analogRead(A1);

  data.concat(String(ch1));
  // data.concat(',');
  // data.concat(String(ch2));

  // print out the value you read:
  Serial.println(data);
  delay(1);        // delay in between reads for stability
}
