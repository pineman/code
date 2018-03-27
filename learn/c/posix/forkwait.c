#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <limits.h>

int main(int argc, char *argv[])
{
	printf("before fork: pid is %d\n", getpid());
	pid_t pid;
	pid = fork();
	if (pid == 0) {
		printf("child: pid is %d\n", getpid());
		printf("child: parent's pid is %d\n", getppid());
		sleep(UINT_MAX);
	}
	else {
		printf("parent: child's pid is %d\n", pid);
		printf("parent: pid is %d\n", getpid());
		printf("parent: parent's pid is %d\n", getppid());

		int cstatus;
		pid_t cpid;
		cpid = wait(&cstatus);
		if (WIFEXITED(cstatus)) {
			printf("parent: child %d exited normally\n", cpid);
		}
		else {
			printf("parent: child %d exited abnormally, with %d\n", cpid, WEXITSTATUS(cstatus));
		}
	}

	return EXIT_SUCCESS;
}
