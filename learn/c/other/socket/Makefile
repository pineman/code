# http://beej.us/guide/bgnet/output/html/singlepage/bgnet.html#syscalls

# Careful for -std=c99, POSIX functions are not defined
# http://stackoverflow.com/questions/12024703/why-cant-getaddrinfo-be-found-when-compiling-with-gcc-and-std-c99
CFLAGS=-g -Wall -Wextra -pedantic
CPPFLAGS=
LDFLAGS=
CC=gcc
SRC=
EXEC=

all:
	make client server

client: client.o
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)

server: server.o
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)

clean:
	rm -rf *.o client server

# This rebuilds everything if the Makefile was modified
# http://stackoverflow.com/questions/3871444/making-all-rules-depend-on-the-makefile-itself/3892826#3892826
-include .dummy
.dummy: Makefile
	touch $@
	$(MAKE) -s clean
