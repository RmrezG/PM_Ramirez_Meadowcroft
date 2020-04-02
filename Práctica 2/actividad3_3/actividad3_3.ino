// interrupt pin
int interrupt_pin = 2;

//contador
int counter = 0;

void setup()
{
  DDRB = DDRB | B11111111; // Data Direction Register B: Inputs 0-6, Output 7
  Serial.begin(9600);
  cli();
  TCCR1B = 0; TCCR1A = 0;
  TCCR1B |= (1 << CS12);
  TCNT1 = 3036;
  TIMSK1 |= (1 << TOIE1);
  sei();

}

ISR(TIMER1_OVF_vect)
{
asm(
    "interrupcion: \n\t"
    ".EQU PORTB, 0x05 \n\t"
    "SBIS PORTB, 6 \n\t"
    "RCALL OPCION_1 \n\t"
    "SBIS PORTB, 2 \n\t"
    "RCALL OPCION_2 \n\t"
    "JMP END \n\t"
    
    "OPCION_1:"
    "CBI PORTB,6 \n\t"
    "SBI PORTB,5 \n\t"
    "RCALL WAIT \n\t"
    "CBI PORTB,5 \n\t"
    "CBI PORTB,1 \n\t"
    "SBI PORTB,4 \n\t"
    "SBI PORTB,2 \n\t"
    "RET \n\t"
    
    "OPCION_2:"
    "CBI PORTB,2 \n\t"
    "SBI PORTB,3 \n\t"
    "RCALL WAIT \n\t"
    "CBI PORTB,3 \n\t"
    "CBI PORTB,4 \n\t"
    "SBI PORTB,6 \n\t"
    "SBI PORTB,1 \n\t"
    "RET \n\t"
    
    "WAIT: \n\t"
    "LDI r22, 40 \n\t"
    "LOOP_3: \n\t"
    "LDI r21, 255 \n\t"
    "LOOP_2: \n\t"
    "LDI r20, 255 \n\t"
    "LOOP_1: \n\t"
    "DEC r20 \n\t"
    "BRNE LOOP_1 \n\t"
    "DEC r21 \n\t"
    "BRNE LOOP_2 \n\t"
    "DEC r22 \n\t"
    "BRNE LOOP_3 \n\t"
    "ret \n\t"
    "END: \n\t"
    );
}
void loop()
{

asm (
  "inicio: \n\t"
  ".EQU PORTB, 0x05 \n\t"
  "LDI R16, 0B01000010 \n\t"
  "LDI R17, 0B00100010 \n\t"
  "LDI R18, 0B00010100 \n\t"
  "LDI R19, 0B00011000 \n\t"
  "OUT PORTB, R16 \n\t"
  "LOOP:"
  "JMP LOOP \n\t"
);
}
