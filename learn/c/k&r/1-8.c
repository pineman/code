#include <stdio.h>

int main()
{
	int c, nl, nt, nb;

	nl = nt = nb = 0;

	while ((c = getchar()) != EOF) {
		if (c == '\n')
			++nl;
		if (c == '\t')
			++nt;
		if (c == ' ')
			++nb;
	}

	printf("newlines = %d\n", nl);
	printf("tabs = %d\n", nt);
	printf("blanks = %d\n", nb);
}
