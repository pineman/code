#include <stdio.h>

void firstp(int *array)
{
	printf("%p\n", array);
	array[0] = 100;
}

int main(void)
{
	int array[] = {1, 2, 3};
	firstp(array);
	printf("%d %d %d\n", array[0], array[1], array[2]);
}
