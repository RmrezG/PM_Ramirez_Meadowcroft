int Rojo1=13;
int Amarillo1=12;
int Verde1=11;
int Rojo2=10;
int Amarillo2=9;
int Verde2=8;

void setup() {
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
  OCR1A=34286;//7812
  //Inicializar el comparador para el registro A
  TIMSK1 |=(1<<OCIE1A);
  //Activar interrupciones nuevamente
  interrupts();

  pinMode(Rojo1,OUTPUT);
  pinMode(Amarillo1,OUTPUT);
  pinMode(Verde1,OUTPUT);
  pinMode(Rojo2,OUTPUT);
  pinMode(Amarillo2,OUTPUT);
  pinMode(Verde2,OUTPUT);
  
}
//boolean flag=true;
int bandera=0;
ISR(TIMER1_COMPA_vect){
  if(bandera==0){
    digitalWrite(Amarillo1,LOW);
    digitalWrite(Rojo1,HIGH);
    digitalWrite(Rojo2,LOW);
    digitalWrite(Verde2,HIGH);
    bandera=1;
  }
  else{
    if(bandera==1){
      digitalWrite(Verde2,LOW);
      digitalWrite(Amarillo2,HIGH);
      bandera=2;
    }
    else{
      if(bandera==2){
        digitalWrite(Amarillo2,LOW);
        digitalWrite(Rojo2,HIGH);
        digitalWrite(Rojo1,LOW);
        digitalWrite(Verde1,HIGH);
        bandera=3;
      }
      else{        
        if(bandera==3){
          digitalWrite(Verde1,LOW);
          digitalWrite(Amarillo1,HIGH);
          bandera=0;
        }
      }
    }
  }

  /*
  if(flag){
    digitalWrite(Rojo2,LOW);
    digitalWrite(Verde1,LOW);
    digitalWrite(Rojo1,HIGH);
    digitalWrite(Verde2,HIGH);
    flag=false;
  }
  else{
    digitalWrite(Rojo1,LOW);
    digitalWrite(Verde2,LOW);
    digitalWrite(Rojo2,HIGH);
    digitalWrite(Verde1,HIGH);
    flag=true;
  }
  */
}

void loop() {
  
}
