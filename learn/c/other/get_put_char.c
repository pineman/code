#include <stdio.h>

/* So this program is basically an interative ASCII table */

int table(int c)
{
	if (c != 10) /* 'Enter' key converted to int */
		printf("%c\t%d\n", c, c);

	return 0;
}

int main()
{
	puts("Type stuff!");

	int c;

	while ((c = getchar()) != EOF) {
		table(c);
	}

	/* Out of the loop, this 'prints' EOF */
	table(c);

	if (EOF == -1) {
		puts("EOF is indeed -1"); // But that's just a coincidence!
	}

	return 0;
}
