#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <wchar.h>

int main(int argc, char *argv[])
{
	setlocale(LC_ALL, "");

	wchar_t test[] = L"\uF933\uF967\uF900\U0001D232";
	wchar_t test2[] = L"盧不豈𝈲";
	printf("%ls, length: %zd\n", test, wcslen(test));
	printf("%ls, length: %zd\n", test2, wcslen(test2));

	return EXIT_SUCCESS;
}
