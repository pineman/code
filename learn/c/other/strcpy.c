#include <stdio.h>
#include <string.h>

int main()
{
	char str1[] = "freitas  é estúpido";
	char str2[] = "freitas";

	int len = sizeof(str1);
	strcpy(str1, str2);

	for (int i = 0; i < len; i++)
		printf("%c", str1[i]);
}
