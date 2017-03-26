CC=gcc
CFLAGS=-Wall -Wextra -pedantic -g -I../include
LDFLAGS=-L../lib -lhello

all:
	make hello_test

hello_test: hello_test.c Makefile
	gcc $(CFLAGS) $(LDFLAGS) hello_test.c -o hello_test

clean:
	rm -f hello_test
