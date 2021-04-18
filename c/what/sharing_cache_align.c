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

void *thread_a(void *arg)
{
	while (1) {
		share.a++;
	}
}

void *thread_b(void *arg)
{
	while (1) {
		share.b++;
	}
}

int main(int argc, char *argv[])
{
	pthread_t a, b;
	pthread_create(&a, NULL, thread_a, NULL);
	pthread_create(&b, NULL, thread_b, NULL);
	sleep(1);
	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
}
