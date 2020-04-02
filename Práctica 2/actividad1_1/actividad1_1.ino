void setup() {
  //configuracion del Timer1 interrupt para suceder cada 0.25seg 
  cli();  //se apagan las interrupciones globales (default)
  TCCR1B=0 ; //estado default del registro de control del timer 
  TCCR1A=0 ;
  TCCR1B|=(1<<CS11)|(1<<CS10);  //configurar el preescalador a 64
  TCNT1=49911;  //punto de inicio del contador
  TIMSK1|=(1<<TOIE1);
  sei();

  asm(
    "LDI r19, 0x00 \n\t"
    "LDI r20, 0xF0 \n\t"
    "LDI r21, 0x80 \n\t"
    "OUT 0x04, r20 \n\t"
    "OUT 0x05, r21 \n\t"
    );
}

void loop() {
  
  asm(
    "MAIN: \n\t"

    "MOV r21,r19 \n\t"
    "SWAP r21 \n\t"
    "OUT 0x05,r21 \n\t"

    "JMP MAIN \n\t"
    );
}

ISR(TIMER1_OVF_vect)
{   

  asm(
    "CPI r19,0x0F \n\t"
    "BRNE NOIGU \n\t"
    "LDI r19,0x00 \n\t"
    "JMP END \n\t"
    "NOIGU: \n\t"
    "INC r19 \n\t"
    "END: \n\t"
  );  
}
