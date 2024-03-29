#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>
#include <assert.h>
#include <errno.h>
#include <locale.h>
#include <time.h>

#define emperror(err) do { \
	char __buf__[1024]; \
	strerror_r(err, __buf__, sizeof(__buf__)); \
	fprintf(stderr, "\x1B[31m%s:%d %s(), errno = %d %s\n\x1B[0m", __FILE__, __LINE__-1, __func__, err, __buf__); \
	exit(err); \
} while(0);

#include <pthread.h>

int a = 0;

void *inc(void *arg)
{
	for (int i = 0; i < 100; i++) {
		a++;
	}
}

int main(int argc, char *argv[])
{
	int r;

	pthread_t t1, t2;

	pthread_create(&t1, NULL, inc, NULL);
	pthread_create(&t2, NULL, inc, NULL);

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);

	printf("a = %d\n", a);

	return EXIT_SUCCESS;
}
