#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdint.h>

#define emperror(err) do { \
	char __buf__[1024]; \
	strerror_r(err, __buf__, sizeof(__buf__)); \
	fprintf(stderr, "\x1B[31m%s:%d %s(), errno = %d %s\n\x1B[0m", __FILE__, __LINE__-1, __func__, err, __buf__); \
	exit(err); \
} while(0);

#define MAX 1000

typedef struct aluno
{
	char *nome;
	int numero;
	int nota;
} aluno;

int main() {
	char buffer[MAX];
	unsigned long nr_alunos = 0;
	aluno *alunos = NULL;

	printf("Quantos alunos pretende introduzir?\n");
	do {
		printf(" > ");
		errno = 0;
		char *chk = fgets(buffer, MAX, stdin);
		if (!chk) goto error;
		nr_alunos = strtoul(buffer, &chk, 10);
		// 0 is invalid. To accept 0, must do nr_alunos == chk.
	} while (!nr_alunos || nr_alunos > SIZE_MAX);
	if (errno) goto error;

	errno = 0;
	alunos = (aluno *) calloc(nr_alunos, sizeof(aluno));
	if (errno) goto error;

	for (unsigned int i = 0; i < nr_alunos; i++)
		free((alunos+i) -> nome);
	free(alunos);

	return EXIT_SUCCESS;

	/* GOTO FTW
	 * AINT NOTHING WRONG WITH GOTO
	 * HATERS GON H8 M8 */
error:
	emperror(errno);
}
