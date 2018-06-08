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

#define emperror(err) do { char __buf__[1024]; sprintf(__buf__, "%s:%d %s(), errno = %d", __FILE__, __LINE__-1, __func__, err); perror(__buf__); } while(0);

#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>

static int c;

void *recv_t(void *arg)
{
	(void) arg;
	ssize_t r;
	size_t s = 10;
	char *buf = malloc(s);
	while (1) {
		r = recv(c, buf, s, MSG_WAITALL);
		printf("recv: recv() returned %zd %s\b \b %lu\n", r, buf, pthread_self());
		if (r == -1) emperror(errno);
	}
}

int main(int argc, char *argv[])
{
	int r;

	int s = socket(AF_INET, SOCK_STREAM, 0);
	if (s == -1) emperror(errno);

	struct sockaddr_in local_addr;
	socklen_t local_addrlen = sizeof(struct sockaddr_in);

	r = listen(s, SOMAXCONN);
	if (r == -1) emperror(errno);

	r = getsockname(s, (struct sockaddr *) &local_addr, &local_addrlen);
	if (r == -1) emperror(errno);
	printf("%d\n", ntohs(local_addr.sin_port));

	c = accept(s, NULL, 0);

	pthread_t t1, t2;
	pthread_create(&t1, NULL, recv_t, NULL);
	pthread_create(&t2, NULL, recv_t, NULL);
	pthread_join(t1, NULL);
	pthread_join(t2, NULL);


	return EXIT_SUCCESS;
}
