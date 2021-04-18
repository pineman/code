#include <stdio.h>

/* This program illustrates how the division of
 * two vars type int is truncated to 0.
 * To avoid that, make p and q type float */
int main(int argc, char *argv[])
{
	//int p = 10000;
	int p = 5;
	int q = 9;
	float result;

	result = p / q;
	//printf("%05.1f\n", result);
	printf("%f\n", result);
	return 0;
}
