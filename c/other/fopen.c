#include <stdio.h>

int main(void)
{
	FILE *test;

	test = fopen("freitas.txt", "w");

	const char *freitas = "O Freitas é gay.\n";
	fputs(freitas, test);
	fclose(test);
}
