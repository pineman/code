#include <stdio.h>
#include <stdlib.h>
#include <pty.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <signal.h>

#define BLOCK_SIZE 1024
char buf[BLOCK_SIZE + 1];

const char PROMPT_READY[] = "__import__('sys').ps1 += '\\x03';"
							 "__import__('sys').ps2 += '\\x03'\n";

char *const execv_args[] = {"/usr/bin/python", NULL};

void disable_terminal_echo(int fd)
{
	struct termios *termios_p;

	termios_p = calloc(1, sizeof(struct termios));
	termios_p->c_lflag &= ECHO;
	tcsetattr(fd, TCSANOW, termios_p);
}

void read_until_prompt(int python)
{
	ssize_t s;

	while (1) {
		s = read(python, buf, BLOCK_SIZE);
		buf[s] = '\0';
		printf("%s", buf);
		if (buf[s - 1] == '\x03') break;
	}
}

int main(int argc, char *argv[])
{
	pid_t pid;
	int python;

	pid = forkpty(&python, NULL, NULL, NULL);

	if (pid != 0) {
		int python_script = open(argv[1], O_RDONLY);

		disable_terminal_echo(python);

		for (int i = 0; i < 3; i++) {
			// TODO: make generic readline, that python_script can also use
			while (1) {
				read(python, buf, 1);
				putchar(buf[0]);
				if (buf[0] == '\n') break;
			}
		}

		read(python, buf, 1024);
		write(python, PROMPT_READY, sizeof(PROMPT_READY));
		read_until_prompt(python);

		while (1) {
			// TODO: read line from python_script and feed into python/stdout

			read_until_prompt(python);
		}

		close(python_script);
		puts("");
		kill(python, SIGTERM);
	}
	else {
		execv(execv_args[0], execv_args);
	}

	return EXIT_SUCCESS;
}
