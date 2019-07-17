#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <string.h>

// Need bignums!!
// https://rosettacode.org/wiki/Ackermann_function#C

typedef uint64_t u64;

u64 ack(u64 m, u64 n)
{
	if (m == 0) return n + 1;
	else if (n == 0) return ack(m-1, 1);
	else return ack(m-1, ack(m, n-1));
}

// Optimization for common cases of m
/* https://stackoverflow.com/a/16181288/11452792
typedef unsigned long long N;
N acker (N m, N n)
{
        while (1)
        switch (m)
        {
        case 0: return n+1U;
        case 1: return n+2U;
        case 2: return 2U*(n+1U)+1U;
        case 3: return (1LLU<<(n+3U))-3U;
        default:
                if (n == 0U)
                        n = 1U;
                else
                        n = acker(m, n-1U);
                m--;
                break;
        }
        return n+1U;
}*/

int main(int argc, char *argv[])
{
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			u64 r = ack(i, j);
			time_t unix_time = time(NULL);
			char *time = ctime(&unix_time);
			time[strlen(time)-1] = '\0'; // Overwrite \n
			printf("[%s] ackermann(%d, %d) is %lu\n", time, i, j, r);
		}
	}

	return EXIT_SUCCESS;
}
