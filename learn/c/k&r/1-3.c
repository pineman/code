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

	fahr = lower;

	puts("| ºF|    ºC|");
	puts("|―――|――――――|");
	while (fahr <= upper) {
		celsius = 5 * (fahr-32) / 9;
		printf("|%3.0f|%6.1f|\n", fahr, celsius);
		fahr += step;
	}
}
