/*
 * Implement ROTx cipher for ASCII.
 */

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <stdbool.h>


void usage(const char *program)
{
	printf("Usage: %s [FILE]\n", program);
	printf("Print FILE ROTx'd to stdout.\n");
}

int main(const int argc, const char **argv)
{
	FILE *fp = NULL;
	char *S = NULL;
	errno = 0;

	if (argc != 2) {
		usage(argv[0]);
		goto error;
	}

	fp = fopen(argv[1], "r");
	if (errno) goto error;

	(void) fseek(fp, 0L, SEEK_END);
	if (errno) goto error;

	long fsz = ftell(fp);
	if (errno) goto error;

	rewind(fp);

	S = (char *) calloc((size_t) fsz + 2, sizeof(char));
	if (errno) goto error;

	(void) fread((void *) S, sizeof(char), (size_t) fsz, fp);
	if (errno) goto error;

	int s = 0, r = 0;
	bool upper = false;
	for (int j = 0; j < 26; j++) {
		printf("\nrot%d:------------------------------------------------\n", j);

		for (int i = 0; i < fsz; i++) {
			if (S[i] >= 'A' && S[i] <= 'Z') {
				upper = true;
			}
			else if (S[i] >= 'a' && S[i] <= 'z') {
				upper = false;
			}
			else {
				printf("%c", S[i]);
				continue;
			}

			if (upper) r = 'A';
			else r = 'a';

			s = ((int) S[i]) - r;
			s = (s + j) % 26 + r;

			printf("%c", (char) s);
		}
	}

	free(S);
	fclose(fp);
	return 0;

error:
	if (S) free(S);
	if (fp) fclose(fp);

	if (errno) {
		perror(argv[0]);
		return errno;
	}

	return 1;
}
