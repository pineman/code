#include <stdio.h>
#include <stdlib.h>

int main()
{
	int size = 0;
	int check = 0;
	int c = 0;

	do {
		check = scanf("%d", &size);
		while ((c = getchar()) != '\n' && c != EOF);
	} while (!check && size > 0);

	int *array = (int *) calloc((size_t) size, sizeof(int));

	for (int i = 0; i < size; i++) {
		array[i] = 10;
		printf("%d\n", array[i]);
	}

	free(array);

	return EXIT_SUCCESS;
}
