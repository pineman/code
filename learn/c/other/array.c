#include <stdio.h>
#include <string.h>

/* this confirms that
 * char string[x] = {0}
 * initializes string to nullbytes corectly.
 */

int main(void)
{
	char string[11] = {0};
	int i = 0;
	for (i = 0; i < 11 - 4; i++)
		string[i] = 'a';

	printf("%s\n", string);
	printf("%d\n", strlen(string));

	return 0;
}
