/*

count_serial

A simple 1Hz serial count 0-9.
*/

int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  delay(1000);
  Serial.write(i);
  i++;
  if (i>9) {
    i = 0;
  } 
  
}
