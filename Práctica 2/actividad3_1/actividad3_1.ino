void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  //Detener todas las interrupciones
  noInterrupts();
  //Registro de control A en 0
  TCCR1A=0;
  //Activar el modo CTC en Timer1
  TCCR1B=0;
  TCCR1B |=(1<<WGM12);
  //Pre-escalador en 1024
  TCCR1B |=(1<<CS12) | (1<<CS10);
  //Inicializar el contador en 0
  TCNT1=0;
  //Valor del registro comparador según la formula
  OCR1A=7812;
  //Inicializar el comparador para el registro A
  TIMSK1 |=(1<<OCIE1A);
  //Activar interrupciones nuevamente
  interrupts();
}

boolean led=false;
ISR(TIMER1_COMPA_vect){
  if(led){
    digitalWrite(LED_BUILTIN,LOW);    
    led=false;
  }
  else{
    digitalWrite(LED_BUILTIN,HIGH);
    led=true;
  }
}

void loop() {
  
}
