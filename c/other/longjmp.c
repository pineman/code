#include <stdio.h>
#include <setjmp.h>

jmp_buf buffer;

void function() {
    printf("Entering function\n");
    setjmp(buffer);
    printf("Exiting function\n");
}

int main() {
    function(); // First, enter and exit the function normally.
    printf("Back in main\n");
    longjmp(buffer, 1); // Then, jump back into the function, which is undefined behavior.
    return 0;
}
