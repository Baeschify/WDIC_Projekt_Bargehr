/*
 * usart.h
 *
 * Created: 11.11.2019 19:38:19
 *  Author: lau
 */ 

#define F_CPU 12000000
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#include <string.h>
#include <stdlib.h>	//aufgabe 5

#ifndef USART_H_
#define USART_H_

extern void usart_init();
extern void usart_putchar(unsigned char data);
extern void usart_sendstring();

#endif /* USART_H_ */