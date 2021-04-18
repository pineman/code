#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <errno.h>
#include <string.h>

int main(void) {
	char buffer[100];
	char *end;
	int si;

	fgets(buffer, sizeof(buffer), stdin);

	errno = 0;

	const unsigned long sl = strtoul(buffer, &end, 10);
	printf("errno: %d\n", errno);
	buffer[strcspn(buffer, "\n")] = 0; // replace trailing \n with \0

	if (end == buffer) {
		fprintf(stderr, "%s: not a (decimal) number\n", buffer);
	}
	else if (*end != '\0') {
		fprintf(stderr, "%s: extra characters at end of input: %s\n", buffer, end);
	}
	else if (sl == ULONG_MAX && errno == ERANGE) {
		fprintf(stderr, "%s out of range of type unsigned long\n", buffer);
	}
	else if (sl > UINT_MAX) {
		fprintf(stderr, "%lu out of range of type unsigned int\n", sl);
	}
	else {
		si = (unsigned int) sl;
		fprintf(stdout, "%d\n", si);
		return EXIT_SUCCESS;
	}

	return EXIT_FAILURE;
}
