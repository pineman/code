/*
 * Code that exposes undefined behaviour concerning shifts in C
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <limits.h>

typedef uint8_t Byte;
typedef uint16_t Byte2;
typedef uint32_t Byte4;
typedef uint64_t Byte8;

int main()
{
	unsigned int i;

	Byte *byte = (Byte *) malloc(sizeof(Byte));
	// memset takes 2nd arg int -> INT_MAX is all 1s!
	byte = (Byte *) memset(byte, INT_MAX, sizeof(Byte));
	// shift uint8_t 8 times, all good.
	for (i = 1; i <= sizeof(Byte)*8; i++)
		printf("%" PRIX8 "\n", *byte >> i);

	Byte2 *byte2 = (Byte2 *) malloc(sizeof(Byte2));
	byte2 = (Byte2 *) memset(byte2, INT_MAX, sizeof(Byte2));
	// shift uint16_t 16 times, still all good.
	for (i = 1; i <= sizeof(Byte2)*8; i++)
		printf("%" PRIX16 "\n", *byte2 >> i);

	Byte4 *byte4 = (Byte4 *) malloc(sizeof(Byte4));
	byte4 = (Byte4 *) memset(byte4, INT_MAX, sizeof(Byte4));
	// shift uint32_t 32 times: UNDEFINED BEHAVIOR.
	// substitute <= for < in the "for" condition
	for (i = 1; i <= sizeof(Byte4)*8; i++)
		printf("%" PRIX32 "\n", *byte4 >> i);

	Byte8 *byte8 = (Byte8 *) malloc(sizeof(Byte8));
	byte8 = (Byte8 *) memset(byte8, INT_MAX, sizeof(Byte8));
	// the same for shifting uint64_t 64 times
	for (i = 1; i <= sizeof(Byte8)*8; i++)
		printf("%" PRIX64 "\n", *byte8 >> i);

	return EXIT_SUCCESS;
}
