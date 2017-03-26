#include <stdio.h>

int main()
{
	int n1, n2;
	char c1;
	scanf("%d%c%d", &n1, &c1, &n2);
	printf("input: %d%c%d\n", n1, c1, n2);

	char a, b;
	sscanf("test", "%c%c", &a, &b);
	printf("%c%c\n", a, b);
}
