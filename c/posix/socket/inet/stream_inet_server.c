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

	struct sockaddr_in local_addr;
	local_addr.sin_family = AF_INET;
	local_addr.sin_port = htons(1337);
	local_addr.sin_addr.s_addr = INADDR_ANY;
	socklen_t local_addrlen = sizeof(struct sockaddr_in);

	r = bind(s, (struct sockaddr *) &local_addr, local_addrlen);
	if (r == -1) eperror(errno);

	r = listen(s, SOMAXCONN);
	if (r == -1) eperror(errno);

	while (1) {
		struct sockaddr_in c_addr;
		socklen_t c_addrlen = sizeof(c_addr);
		int c = accept(s, (struct sockaddr *) &c_addr, &c_addrlen);
		if (r == -1) eperror(errno);

		ssize_t bufsize = 1000;
		char buf[bufsize];
		ssize_t recv_r;
		bool garble = false;
		while (1) {
			recv_r = recv(c, (void *) buf, bufsize, MSG_WAITALL);
			if (recv_r == -1) eperror(errno);
			if (recv_r == 0) break;
			printf("got %zd bytes\n",  recv_r);
			//puts(buf);
			for (int i = 0; i < bufsize; i++) {
				if (buf[i] != buf[0]) {
					printf("buf[i] = %c buf[0] = %c\n", buf[i], buf[0]);
					garble = true;
					break;
				}
			}
			if (garble) {
				puts("---- Garbled!!");
				garble = false;
			}
		}
		r = close(c);
		if (r == -1) eperror(errno);
	}

	r = close(s);
	if (r == -1) eperror(errno);

	return EXIT_SUCCESS;
}
