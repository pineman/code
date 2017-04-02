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
	ssize_t wc;
	char buffer[1000000] = {0};

	struct addrinfo hints = {0}, *server;
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	c = getaddrinfo(HOST, PORT, &hints, &server);
	if (c != 0) return EXIT_FAILURE;

	int sock = socket(server->ai_family, server->ai_socktype, server->ai_protocol);
	if (errno) { perror(argv[0]); exit(errno); }

	connect(sock, server->ai_addr, server->ai_addrlen);
	if (errno) { perror(argv[0]); exit(errno); }

	wc = write(sock, buffer, 1000000);
	if (errno) { perror(argv[0]); exit(errno); }
	printf("%zd bytes written\n", wc);

	// https://blog.netherlabs.nl/articles/2009/01/18/the-ultimate-so_linger-page-or-why-is-my-tcp-not-reliable
	// https://news.ycombinator.com/item?id=14014136
	close(sock);
	freeaddrinfo(server);
	if (errno) { perror(argv[0]); exit(errno); }

	return EXIT_SUCCESS;
}
