#include <stdio.h>
#include <stdlib.h>

#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>

#include "common.h"

int
main(int argc, char **argv)
{
	errno = 0;
	int c;
	char buffer[4096];
	char hello[] = "Hello!\n";

	struct addrinfo hints = {0}, *server;
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	c = getaddrinfo(HOST, PORT, &hints, &server);
	if (c != 0) return EXIT_FAILURE;

	int sock = socket(server->ai_family, server->ai_socktype, server->ai_protocol);
	if (errno) { perror(argv[0]); exit(errno); }

	bind(sock, server->ai_addr, server->ai_addrlen);
	if (errno) { perror(argv[0]); exit(errno); }

	listen(sock, 0);
	if (errno) { perror(argv[0]); exit(errno); }

	int client = accept(sock, server->ai_addr, &(server->ai_addrlen));
	if (errno) { perror(argv[0]); exit(errno); }

	// https://blog.netherlabs.nl/articles/2009/01/18/the-ultimate-so_linger-page-or-why-is-my-tcp-not-reliable
	ssize_t wc = write(client, hello, sizeof(hello));
	if (errno) { perror(argv[0]); exit(errno); }
	printf("%zd bytes written\n", wc);

	ssize_t rc_total = 0, rc;
	for (;;) {
		rc = read(client, buffer, 4096);
		if (errno) { perror(argv[0]); exit(errno); }

		if (rc == 0) {
			// EOF
			break;
		}

		rc_total += rc;
	}
	printf("%zd bytes received\n", rc_total);

	freeaddrinfo(server);
	close(sock);
	if (errno) { perror(argv[0]); exit(errno); }

	return EXIT_SUCCESS;
}
