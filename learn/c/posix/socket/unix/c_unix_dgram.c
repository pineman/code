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

int main(int argc, char *argv[])
{
	int r;
	int s;
	s = socket(AF_UNIX, SOCK_DGRAM, 0);
	if (s == -1) mperror();

	struct sockaddr_un addr;
	memset(&addr, 0, sizeof(addr));
	addr.sun_family = AF_UNIX;
	socklen_t addr_size = offsetof(struct sockaddr_un, sun_path) + strlen(addr.sun_path) + 1;
	r = bind(s, (struct sockaddr *) &addr, addr_size);
	if (r == -1) mperror();

	struct sockaddr_un dest_addr;
	dest_addr.sun_family = AF_UNIX;
	char path[] = "test";
	strcpy(dest_addr.sun_path, path);
	socklen_t dest_addr_size = offsetof(struct sockaddr_un, sun_path) + strlen(dest_addr.sun_path) + 1;


	size_t bufsize = 212960;
	char buf[bufsize];
	for (unsigned int i = 0; i < bufsize; i++) {
		buf[i] = 'a';
	}
	ssize_t send_r, recv_r;
	struct timespec t;
	while (1) {
		send_r = sendto(s, (void *) buf, bufsize, 0, (struct sockaddr *) &dest_addr, dest_addr_size);
		if (send_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: sendto() returned %zd\n", (int) t.tv_sec, t.tv_nsec, send_r);

		recv_r = recv(s, (void *) buf, bufsize, 0);
		if (recv_r == -1) mperror();
		clock_gettime((clockid_t) CLOCK_REALTIME, &t);
		printf("%d.%ld: recv OK returned %zd\n", (int) t.tv_sec, t.tv_nsec, recv_r);
	}

	r = close(s);
	if (r == -1) mperror();

	return EXIT_SUCCESS;
}
