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

int main(int argc, char *argv[])
{
	int r;
	struct sockaddr_in parent_addr;
	socklen_t parent_addrlen = sizeof(struct sockaddr_in);
	parent_addr.sin_family = AF_INET;

	r = inet_pton(AF_INET, "178.62.77.101", (void *) &parent_addr.sin_addr);
	char *check = NULL;
	unsigned long test = 0;
	errno = 0;
	test = strtoul(argv[1], &check, 10);
	parent_addr.sin_port = htons((uint16_t) test);

	int p = socket(AF_INET, SOCK_STREAM, 0);
	if (p == -1) emperror(errno);
	r = connect(p, (struct sockaddr *) &parent_addr, parent_addrlen);
	if (r == -1) emperror(errno);

	int s = 10;
	char *buf = malloc(s);
	uint32_t j = 0;
	while (1) {
		memcpy(buf, &j, 4);
		r = send(p, buf, 4, MSG_NOSIGNAL);
		printf("send returned %d %d\n", r, j++);
		if (r == -1) { emperror(errno); break; }
	}
	r = close(p);
	if (r == -1) emperror(errno);

	return EXIT_SUCCESS;
}
