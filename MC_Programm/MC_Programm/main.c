/*
 * MC_Programm.c
 *
 * Created: 
 * Author : pbphi
 */ 

#include <avr/io.h>
#include "usart.h"
#include <util/delay.h>
#include <avr/interrupt.h>

int main(void)
{
    DDRD = 0b00000001;
	DDRA = 0xF0;
	PORTA = 0x0F;
	DDRC = 0xFF;
	PORTC = 0xF0;
	
	usart_init();
	
    while (1) 
    {
		if((~PINA & 0x01)==0x01) //S0 gedrückt
		{
			PORTC=0xFF;
			_delay_ms(500);		//Tastenentprellung 0.5s
			char s[] = "fwd";
			usart_sendstring(s);	
		}
		if((~PINA & 0x02)==0x02) //S1 gedrückt
		{
			PORTC=0x00;
			_delay_ms(500);		//Tastenentprellung 0.5s
			char s[] = "bkw";
			usart_sendstring(s);
		}
    }
}

