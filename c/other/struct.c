#include <stdlib.h>
#include <stdio.h>

/*
typedef struct {
	char *str;
} String;*/

struct String {
	char *str;
};
typedef struct String String;

enum numbers {ZERO, ONE, TWO, THREE};
typedef enum numbers numbers;

int main()
{
	String test = {"test"};
	printf("%s\n", test.str);

	numbers one = THREE;
	printf("%d\n", one);

	printf("%zd
}
