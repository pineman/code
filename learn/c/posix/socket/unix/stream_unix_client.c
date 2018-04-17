#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stddef.h>

#define mperror() { fprintf(stderr, "%s:%d errno = %d: %s\n", __FILE__, __LINE__-1, errno, strerror(errno)); exit(errno); }

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/un.h>

// TODO: handle SIGINT by closing and unlinking the socket

int main(void)
{
	int r;
	int s;

	s = socket(AF_UNIX, SOCK_STREAM, 0);
	if (s == -1) mperror();

	//struct sockaddr_un addr;
	//addr.sun_family = AF_UNIX;
	//strcpy(addr.sun_path, "client");
	//socklen_t addrlen = offsetof(struct sockaddr_un, sun_path) + strlen(addr.sun_path) + 1;
	//r = unlink(addr.sun_path);
	//if (r == -1 && errno != ENOENT) mperror();
	//r = bind(s, (struct sockaddr *) &addr, addrlen);
	//if (r == -1) mperror();

	struct sockaddr_un dest_addr;
	dest_addr.sun_family = AF_UNIX;
	strcpy(dest_addr.sun_path, "server");
	socklen_t dest_addrlen = offsetof(struct sockaddr_un, sun_path) + strlen(dest_addr.sun_path) + 1;
	r = connect(s, (struct sockaddr *) &dest_addr, dest_addrlen);
	if (r == -1) mperror();

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
		if (send_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: write() returned %zd\n", (int) t.tv_sec, t.tv_nsec, send_r);

		recv_r = recv(s, (void *) buf_OK, 50, MSG_WAITALL);
		if (recv_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: recv() %s returned %zd\n", (int) t.tv_sec, t.tv_nsec, buf_OK, recv_r);
	}

	r = close(s);
	if (r == -1) mperror();
	r = unlink(addr.sun_path);
	if (r == -1) mperror();

	return EXIT_SUCCESS;
}
