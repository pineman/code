#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


int main(int argc, char *argv[])
{
	asm("jmp *%0"
		:
		:"r"(&main)
		:
		);
}
