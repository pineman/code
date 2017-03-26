#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main()
{
	void *check = NULL;
	while (1) {
		check = malloc(sizeof(int));
		if (!check) {
			perror("Error");
			exit(1);
		}
	}
}
