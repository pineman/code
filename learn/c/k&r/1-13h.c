#include <stdio.h>
#define MAXLENGTH 40

int main()
{
	int c = 0;
	int n = 0;
	int lengths[MAXLENGTH];

	for (int i = 0; i < MAXLENGTH; ++i)
		lengths[i] = 0;

	while ((c = getchar()) != EOF) {
		if ( !(c == '\n' || c == ' ' || c == '\t') )
			++n;
		else {
			if (n != 0) {
				int i = lengths[n];
				lengths[n] = ++i;
				//++lengths[n]; //this makes the last element -1 for some reason
			}
			n = 0;
		}
	}

	puts("\nHistogram of word lengths:");
	for (int i = 0; i < MAXLENGTH; i++) {
		if (lengths[i] != 0) {
			printf("%d: ", i);
			for (int j = 1; j <= lengths[i]; ++j)
				printf("|");
			printf("\n");
		}
	}
}
