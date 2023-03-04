#include <sys/mman.h>
#include <sys/types.h>
#include <stdio.h>

void main() {
	int *addr = mmap(0, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON, -1, 0);
	addr[0] = 123;
	printf("addr is %d\n", addr[0]);
	madvise((caddr_t) addr, 4096, MADV_DONTNEED);
	printf("addr is %d\n", addr[0]);
	// Prints 0 on linux
	// https://www.youtube.com/watch?v=bg6-LVCHmGM&t=3518s
}
