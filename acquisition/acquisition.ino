
String data;
int brojac = 0;
int sumValue = 0;
float value = 0;
int n = 10;

void setup() {
  Serial.begin(9600);
}

void loop() {
  data = "";
  int ch1 = analogRead(A0);
  int ch2 = analogRead(A1);

  /*
  sumValue += ch1;
  brojac++;
  if (brojac == n) {
    data = "";
    brojac = 0;
    value = sumValue / n;
    data.concat(String(value));
    Serial.println(data);
  }
  */

  // output data
  data.concat(String(ch1));
  data.concat(',');
  data.concat(String(ch2));

  Serial.println(data);
  delay(10);
}
