#include <stdio.h>

int main()
{
	int c = 0;
	int last = 0;

	while ((c = getchar()) != EOF) {
		if ( !(last == ' ' && c == ' ') )
			putchar(c);
		last = c;
	}
}
