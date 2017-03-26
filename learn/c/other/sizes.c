#include <stdio.h>
#include <stdlib.h>

int main()
{
	int s, i, l, f, d, ll, ld, c;

	s = sizeof(short int);
	i = sizeof(int);
	l = sizeof(long int);
	f = sizeof(float);
	d = sizeof(double);
	ll = sizeof(long long);
	ld = sizeof(long double);
	c = sizeof(char);

	printf("The size of a short int: %d bytes, %d bits\n", s, s * 8);
	printf("The size of an int: %d bytes, %d bits\n", i, i * 8);
 	printf("The size of a long int: %d bytes, %d bits\n", l, l * 8);
	printf("The size of a float: %d bytes, %d bits\n", f, f * 8);
	printf("The size of a double: %d bytes, %d bits\n", d, d * 8);
	printf("The size of a long long int: %d bytes, %d bits\n", ll, ll * 8);
	printf("The size of a long double: %d bytes, %d bits\n", ld, ld * 8);
	printf("The size of a char: %d bytes, %d bits\n", c, c * 8);

	return EXIT_SUCCESS;
}
