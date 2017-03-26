#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char *test = NULL;
	test = (char *) calloc(20, 1);
	strcpy(test, "we-love-ist");
	const char *test1 = "-";

	printf("%s\n", strsep(&test, test1));
	printf("%s\n", strsep(&test, test1));
	printf("%s\n", strsep(&test, test1));

	free(test);
}
