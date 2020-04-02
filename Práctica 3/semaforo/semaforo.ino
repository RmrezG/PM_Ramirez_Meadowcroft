void setup()
{
DDRB = DDRB | B11111111; // Data Direction Register B: Inputs 0-6, Output 7
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
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"OUT PORTB, R17 \n\t"
"call tiempo \n\t"
"OUT PORTB, R18 \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"call tiempo \n\t"
"OUT PORTB, R19 \n\t"
"call tiempo \n\t"
"jmp main \n\t"


"tiempo: \n\t"
"LDI r22, 80 \n\t"
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
);
}
