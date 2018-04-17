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
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void)
{
	int r;
	int s;

	s = socket(AF_INET, SOCK_STREAM, 0);
	if (s == -1) mperror();

	struct sockaddr_in local_addr;
	//local_addr.sin_family = AF_INET;
	//local_addr.sin_port = 0;
	//local_addr.sin_addr.s_addr = INADDR_ANY;
	socklen_t local_addrlen = sizeof(struct sockaddr_in);

	//r = bind(s, (struct sockaddr *) &local_addr, local_addrlen);
	//if (r == -1) mperror();

	r = listen(s, SOMAXCONN);
	if (r == -1) mperror();

	r = getsockname(s, (struct sockaddr *) &local_addr, &local_addrlen);
	if (r == -1) mperror();
	printf("unbound listening socket - address: %s port: %d\n", inet_ntoa(local_addr.sin_addr), ntohs(local_addr.sin_port));

	int c = s.accept();
	if (c == -1) mperror();

	r = close(s);
	if (r == -1) mperror();

	return EXIT_SUCCESS;
}
