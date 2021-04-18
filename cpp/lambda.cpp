#include <iostream>

int main(void)
{
	char buf[100] = {0};

	buf[0] = 'z';

	[&] () { buf[0] = 'a'; buf[1] = 'b'; buf[2] = 'c'; puts(buf); }();

	puts(buf);
}
