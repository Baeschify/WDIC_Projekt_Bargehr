/*
 * usart.c
 * 
 * Created: 11.11.2019 19:21:52
 * 
 * Author: lau
 */ 


#include "usart.h"

//=========================================
//USART Initialisierung (Datenformat: 8N1)
//=========================================
void usart_init() 
{
	// Baudrate einstellen
	int baudrate = (unsigned long) (12000000/9600)/16-1;	//baudrate hier ist 9600
	UBRRH = (baudrate>>8);						//URSEL=0					
	UBRRL = baudrate;
	
	//UART-RAhmen konfigurieren
	//UCSRA=(1<<RXC) | (1<<TXC);	
	UCSRB= (1<<TXEN) | (1<<TXCIE) | (1<<RXCIE) | (1<<RXEN);						//enable Receiver/Transmitter, RX Complete Interrupt Enable, 
	//UCSRC= 						//asynchroner Mode, Datenformat 8N1, URSEL=1
	
}

//=========================================
//USART Senderoutine
//=========================================
void usart_putchar(unsigned char data)	
{
	while (!( UCSRA & (1<<UDRE)) );	// warten bis Sendepuffer leer ist ("polling")
	UDR = data;						// neue Daten senden
}

void usart_sendstring(char *s)
{
	int i = 0;
	while(s[i]!=0)			//wenn array fertig ist, dann wert ist Null
	{
		usart_putchar(s[i]);
		usart_putchar('\r');

		i++;
	}
}


//=========================================
//USART Empfangs-ISR
//=========================================
ISR(USART_RXC_vect)
{
	PORTC=UDR;
}

