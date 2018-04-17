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

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void)
{
	struct in_addr addr; // literally just a uint32_t

	int t = inet_aton("178.62.77.101", &addr);
	if (t == 0) {
		fprintf(stderr, "Invalid address\n");
		exit(EXIT_FAILURE);
	}

	printf("inet_aton() = %#x\n", addr.s_addr);

	printf("inet_ntoa() = %s\n", inet_ntoa(addr));

	return EXIT_SUCCESS;
}
