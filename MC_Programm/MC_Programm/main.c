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
    DDRD = 0b00000010;
	DDRA = 0xF0;
	PORTD = 0x0F;
	
    while (1) 
    {
		if((PINA & 0x01)==0x01) //S0 gedrückt
		{
			_delay_ms(500);		//Tastenentprellung 0.5s
			char s[] = "fwd";
			usart_sendstring(s);	
		}
		else if((PINA & 0x02)==0x02) //S1 gedrückt
		{
			_delay_ms(500);		//Tastenentprellung 0.5s
			char s[] = "bkw";
			usart_sendstring(s);
		}
    }
}

