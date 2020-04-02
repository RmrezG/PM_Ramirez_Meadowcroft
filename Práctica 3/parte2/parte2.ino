int LED = 50;
int Boton = 30;
int anterior = 0;
int cont = 0;
int counter = 0;

void setup()
{
  Serial.begin(9600); 
  pinMode(LED, OUTPUT);
  pinMode(Boton, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(Boton), interrupcion, FALLING);
}

void loop()
{
  digitalWrite(LED, HIGH);
  delay(500);
  digitalWrite(LED, LOW);
  delay(500);

  if (counter != cont)
   {
      counter = cont;
      
   }
   Serial.println(counter);
   
}

void interrupcion()
{
   cont++;
   Serial.println(cont);
}
