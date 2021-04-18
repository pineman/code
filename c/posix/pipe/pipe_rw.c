#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define chk_perror() { if (errno) { fprintf(stderr, "%s:%d errno = %d: %s\n", __FILE__, __LINE__-1, errno, strerror(errno)); exit(errno); } }

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void child_process(int pipefd[2])
{
	int a = 2;
	srand(getpid());
	if (rand() % 2 == 1) write(pipefd[1], &a, sizeof(int));
	sleep(1);
	int b;
	read(pipefd[0], &b, sizeof(int));
	if (b == 3) printf("child %d: b = %d\n", getpid(), b);
}

void parent_process(int pipefd[2])
{
	int a;
	read(pipefd[0], &a, sizeof(int));
	printf("parent: a = %d\n", a);
	sleep(1);
	int b = 3;
	write(pipefd[1], &b, sizeof(int));
	write(pipefd[1], &b, sizeof(int));
	write(pipefd[1], &b, sizeof(int));
	write(pipefd[1], &b, sizeof(int));
}

int main(int argc, char *argv[])
{
	pid_t pid;
	int i;
	int pipefd[2];
	pipe(pipefd);
	for (i = 0; i < 10; i++) {
		errno = 0;
		pid = fork();
		if (pid == -1) chk_perror();
		if (pid == 0) {
			break; // don't continue fork()ing if we're a child
		}
	}

	if (pid == 0) {
		child_process(pipefd);
	}
	else {
		parent_process(pipefd);
	}

	return EXIT_SUCCESS;
}
