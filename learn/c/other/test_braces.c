#include <stdio.h>

int main()
{
	int x, y;
	x = 0;
	y = 3;

	for (x = 0; x <= 10; x++) {
		if (x < 2) {
			if (y > 2)
				puts("ye");
		}
		else if (x == 7)
			puts("ne");
	}
}
