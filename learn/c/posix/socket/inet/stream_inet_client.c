#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stddef.h>

#define eperror(r) { fprintf(stderr, "%s:%d errno = %d: %s\n", __FILE__, __LINE__-1, r, strerror(r)); exit(r); }

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void)
{
	int r;
	int s;

	s = socket(AF_INET, SOCK_STREAM, 0);
	if (s == -1) eperror(errno);

	struct sockaddr_in dest_addr;
	socklen_t dest_addrlen = sizeof(struct sockaddr_in);
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(1337);
	r = inet_aton("127.0.0.1", &dest_addr.sin_addr);
	if (r == -1) eperror(errno);
	r = connect(s, (struct sockaddr *) &dest_addr, dest_addrlen);
	if (r == -1) eperror(errno);

	size_t bufsize = 212960;
	char buf[bufsize];
	for (unsigned int i = 0; i < bufsize; i++) {
		buf[i] = 'a';
	}
	char buf_OK[50];
	ssize_t send_r, recv_r;
	struct timespec t;
	while (1) {
		//send_r = send(s, (void *) buf, bufsize, 0);
		send_r = write(s, (void *) buf, bufsize);
		if (send_r == -1) eperror(errno);
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: write() returned %zd\n", (int) t.tv_sec, t.tv_nsec, send_r);

		recv_r = recv(s, (void *) buf_OK, 50, MSG_WAITALL);
		if (recv_r == -1) eperror(errno);
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: recv() %s returned %zd\n", (int) t.tv_sec, t.tv_nsec, buf_OK, recv_r);
	}

	r = close(s);
	if (r == -1) eperror(errno);

	return EXIT_SUCCESS;
}
