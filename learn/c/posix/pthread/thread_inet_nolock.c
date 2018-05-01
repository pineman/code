#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stddef.h>

#define eperror(r) { fprintf(stderr, "%s:%d errno = %d: %s\n", __FILE__, __LINE__-1, r, strerror(r)); exit(r); }

#include <sys/types.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <pthread.h>

#define NUM_THREADS 2

struct thread_arg {
	pthread_t thread_id;
	int thread_no;
};

int s;

// test integer and floating point code

// TODO: Everyone increment the same number
void *thread_function(void *arg)
{
	struct thread_arg *targ = (struct thread_arg *) arg;

	pthread_t t = pthread_self();
	bool must_be_true = pthread_equal(t, targ->thread_id);

	pid_t p = getpid();

	printf("hello from thread %d, pid %d, non-portable thread_id %#x, %d\n",
		targ->thread_no, p, (int) targ->thread_id, must_be_true);

	char *ret = malloc(1);
	srand(t);
	*ret = (char) (rand() % ('z' - 'A') + 'A'); // TODO: rand not thread safe

	int r;
	ssize_t size = 100000;
	char *buf = malloc(size);
	for (int i = 0; i < size; i++) {
		buf[i] = *ret;
	}
	//sleep(targ->thread_no);
	for (;;) {

		r = write(s, (void *) buf, size);
		if (r == -1) eperror(errno);
		printf("thread %d wrote %d * %c\n", targ->thread_no, r, *ret);
	}

	return (void *) ret;
}

int main(int argc, char *argv[])
{
	int r;
	struct thread_arg *targs = malloc(sizeof(struct thread_arg) * NUM_THREADS);

	//srand(time(NULL));

	s = socket(AF_INET, SOCK_STREAM, 0);
	if (s == -1) eperror(errno);

	struct sockaddr_in dest_addr;
	socklen_t dest_addrlen = sizeof(struct sockaddr_in);
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(1337);
	r = inet_aton("178.62.77.101", &dest_addr.sin_addr);
	if (r == -1) eperror(errno);
	r = connect(s, (struct sockaddr *) &dest_addr, dest_addrlen);
	if (r == -1) eperror(errno);

	for (int t = 0; t < NUM_THREADS; t++) {
		targs[t].thread_no = t;
		/* The pthread_create() call stores the thread ID into corresponding
		 * element of targs[] */
		r = pthread_create(&targs[t].thread_id, NULL, thread_function, (void *) &targs[t]);
		if (r != 0) eperror(r);
	}

	printf("hello from main thread, pid %d, non-portable thread_id %#x\n",
		getpid(), (int) pthread_self());

	void *ret;
	for (int t = 0; t < NUM_THREADS; t++) {
		r = pthread_join(targs[t].thread_id, &ret);
		printf("thread %d returned %c\n", t, *((char *) ret));
		free(ret);
		if (r != 0) eperror(r);
	}

	close(s);
	free(targs);

	return EXIT_SUCCESS;
}
