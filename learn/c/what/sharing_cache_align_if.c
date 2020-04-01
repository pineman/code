#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <signal.h>

struct Share {
	volatile uint64_t a;
	volatile uint64_t b;
};

typedef uint64_t __attribute__((aligned(64))) Auint64_t;
struct SharePad {
	volatile Auint64_t a;
	volatile Auint64_t b;
};

struct SharePad share;
//struct Share share;

void *thread(void *arg)
{
	int my_arg = *((int *) arg);
	while (1) {
		if (my_arg == 1) {
			share.a++;
		}
		else {
			share.b++;
		}
	}
}

int main(int argc, char *argv[])
{
	int a_arg = 1, b_arg = 2;
	pthread_t a, b;
	pthread_create(&a, NULL, thread, (void *) &a_arg);
	pthread_create(&b, NULL, thread, (void *) &b_arg);
	sleep(1);
	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
}
