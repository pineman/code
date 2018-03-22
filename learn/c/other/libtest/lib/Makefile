CC=gcc
CFLAGS=-c -g -Wall -Wextra -pedantic -I../include
LDFLAGS=-shared

all:
	make libhello

libhello: hello.c Makefile
	gcc $(CFLAGS) hello.c -o hello.o
	gcc $(LDFLAGS) -Wl,-soname,libhello.so hello.o -o libhello.so

clean:
	rm -f hello.o
	rm -f libhello.so
