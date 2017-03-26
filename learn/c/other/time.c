#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <locale.h>

int main(void)
{
	setlocale(LC_ALL, ""); // Set locale to env.

	time_t epoch = 0;
	struct tm *tm = 0;
	char buffer[100];

	time(&epoch);
	tm = localtime(&epoch);

	strftime(buffer, 100, "Today: %Ec %z", tm);
	if (tm->tm_isdst)
		strcat(buffer, " (DST).");

	puts(buffer);

	return EXIT_SUCCESS;
}
