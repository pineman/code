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

int main(void)
{
	int r;
	int s;

	s = socket(AF_UNIX, SOCK_DGRAM, 0);
	if (s == -1) mperror();

	struct sockaddr_un addr;
	addr.sun_family = AF_UNIX;
	strcpy(addr.sun_path, "server");
	socklen_t addrlen = offsetof(struct sockaddr_un, sun_path) + strlen(addr.sun_path) + 1;
	r = unlink(addr.sun_path);
	if (r == -1 && errno != ENOENT) mperror();
	r = bind(s, (struct sockaddr *) &addr, addrlen);
	if (r == -1) mperror();

	struct sockaddr_un c_addr;
	socklen_t c_addrlen = sizeof(c_addr);

	size_t bufsize = 1000000;
	char buf[bufsize];
	char buf_OK[50] = "OK";
	ssize_t recv_r, send_r;
	struct timespec t;
	while (1) {
		recv_r = recvfrom(s, (void *) buf, bufsize, 0, (struct sockaddr *) &c_addr, &c_addrlen);
		if (recv_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: recv() returned %zd\n", (int) t.tv_sec, t.tv_nsec, recv_r);

		send_r = sendto(s, (void *) buf_OK, 50, 0, (struct sockaddr *) &c_addr, c_addrlen);
		if (send_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: sent OK returned %zd\n", (int) t.tv_sec, t.tv_nsec, send_r);
	}

	r = close(s);
	if (r == -1) mperror();
	r = unlink(addr.sun_path);
	if (r == -1) mperror();

	return EXIT_SUCCESS;
}
