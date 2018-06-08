#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define eperror(r) { fprintf(stderr, "%s:%d errno = %d: %s\n", __FILE__, __LINE__-1, r, strerror(r)); exit(r); }

#include <unistd.h>
#include <pthread.h>

pthread_mutex_t mutex;
pthread_rwlock_t rwlock;

void *thread_function1(void *arg)
{
	int r;

	puts("1 try lock");
	r = pthread_mutex_lock(&mutex);
	//r = pthread_rwlock_wrlock(&rwlock);
	if (r != 0) eperror(r);
	puts("1 got lock");
	puts("1 dying");
	pthread_exit(NULL);
}

void *thread_function2(void *arg)
{
	int r;

	sleep(5);
	puts("2 try lock");
	r = pthread_mutex_lock(&mutex);
	//r = pthread_rwlock_rdlock(&rwlock);
	if (r != 0) eperror(r);
	puts("2 got lock");
	puts("2 dying");
	pthread_exit(NULL);
}


int main(int argc, char *argv[])
{
	int r;

	pthread_t t1, t2;
	pthread_mutexattr_t mutex_attr;
	r = pthread_mutexattr_init(&mutex_attr);
	if (r != 0) eperror(r);
	r = pthread_mutexattr_settype(&mutex_attr, PTHREAD_MUTEX_ERRORCHECK);
	if (r != 0) eperror(r);
	r = pthread_mutexattr_setrobust(&mutex_attr, PTHREAD_MUTEX_ROBUST);
	if (r != 0) eperror(r);
	r = pthread_mutex_init(&mutex, &mutex_attr);
	if (r != 0) eperror(r);
	r = pthread_mutexattr_destroy(&mutex_attr);
	if (r != 0) eperror(r);

	r = pthread_rwlock_init(&rwlock, NULL);
	if (r != 0) eperror(r);

	/* The pthread_create() call stores the thread ID into corresponding
		* element of targs[] */
	r = pthread_create(&t1, NULL, thread_function1, NULL);
	r = pthread_create(&t2, NULL, thread_function2, NULL);

	sleep(10);

	puts("cancelling 1");
	pthread_cancel(t1);
	puts("joining 1");
	pthread_join(t1, NULL);
	puts("cancelling 2");
	pthread_cancel(t2);
	puts("joining 2");
	pthread_join(t2, NULL);
	puts("everyone is dead");

	r = pthread_mutex_destroy(&mutex);
	if (r != 0) eperror(r);
	r = pthread_rwlock_destroy(&rwlock);
	if (r != 0) eperror(r);

	return EXIT_SUCCESS;
}
