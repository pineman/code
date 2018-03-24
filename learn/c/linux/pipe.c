#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <time.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define NUM_CHILDREN_MAX 8UL
#define CHILD_BUFSIZ 10

void child_process(int pipefd[2])
{
	//close(pipefd[0]); // Causes SIGPIPE in the parent
	pid_t pid = getpid();

	close(pipefd[1]);
	printf("child %d: closed write pipe\n", pid);

	char *buf = malloc(1024); // should be big enough
	char *tmp_buf = malloc(50);
	int int_buf;
	srand(pid);

	ssize_t read_ret;
	sprintf(buf, "child %d:", pid);
	while (1) {
		errno = 0;
		read_ret = read(pipefd[0], &int_buf, sizeof(int));
		printf("child %d: read returned %zd\n", pid, read_ret);
		if (read_ret == 0) { break; }
		if (errno) { perror("child"); exit(errno); };
		sprintf(tmp_buf, " %d", int_buf);
		strcat(buf, tmp_buf);
		usleep(random() % 500000);
	}
	close(pipefd[0]);
	printf("child %d: closed read pipe\n", pid);
	puts(buf);
	free(buf);
	free(tmp_buf);
}

void parent_process(int num_children, int pipefd[2])
{
	close(pipefd[0]);
	puts("parent: closed read pipe");

	ssize_t write_ret;
	for (int i = 0; i < num_children * CHILD_BUFSIZ; i++) {
		errno = 0;
		write_ret = write(pipefd[1], &i, sizeof(int));
		printf("parent: write returned %zd\n", write_ret);
		if (errno) { perror(""); exit(errno); };
	}
	close(pipefd[1]);
	puts("parent: closed write pipe");

	int s;
	pid_t t;
	for (int i = 0; i < num_children; i++) {
		t = wait(&s);
		printf("parent: got child %d\n", t);
	}
}

unsigned long str_to_ulong(const char *str, const unsigned long max)
{
	char *check = NULL;
	unsigned long res = strtoul(str, &check, 10);
	if (check == str || res > max) {
		puts("Invalid str_to_ulong");
		exit(1);
	}
	return res;
}

int main(int argc, char *argv[])
{
	if (argc <= 1) {
		puts("No argument");
		exit(1);
	}

	unsigned long num_children = str_to_ulong(argv[1], NUM_CHILDREN_MAX);

	// TODO: open pipe
	int pipefd[2];
	errno = 0;
	pipe(pipefd);
	if (errno) { perror(""); exit(errno); };

	pid_t pid;
	unsigned int i; // Save i to pass to child_process later as it is the child's unique "number"
	for (i = 0; i < num_children; i++) {
		errno = 0;
		pid = fork();
		if (errno) { perror(""); exit(errno); }
		if (pid == 0) {
			break; // don't continue fork()ing if we're a child
		}
	}

	if (pid == 0) {
		child_process(pipefd);
	}
	else {
		parent_process(num_children, pipefd);
	}

	return EXIT_SUCCESS;
}
