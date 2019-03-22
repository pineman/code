void setup(){
  Serial.begin(1000000);
}

void loop(){
  Serial.println("a");
  Serial.flush();
}
