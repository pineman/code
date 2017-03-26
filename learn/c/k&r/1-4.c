#include <stdio.h>

/*
** print Fahrenheit-Celsius table
** floating-point version
*/

int main()
{
	float fahr, celsius;
	int lower, upper, step;

	lower = 0;		/* lower limit of temperature table */
	upper = 300;	/* upper limit */
	step = 20;		/* step size */

	celsius = lower;

	puts("| ºC|    ºF|");
	puts("|―――|――――――|");
	while (celsius <= upper) {
		fahr = 9/5 * (celsius + 32);
		printf("|%3.0f|%6.1f|\n", celsius, fahr);
		celsius += step;
	}
}
