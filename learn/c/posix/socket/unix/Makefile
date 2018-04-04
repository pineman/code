CFLAGS=-Wall -Wextra -pedantic -Wno-unused-parameter -Wno-unused-variable
#CFLAGS+=-O3
CFLAGS+=-g
#CFLAGS+=-g -pg
CPPFLAGS=
LDFLAGS=
CC=gcc
SRC=$(wildcard *.c)

all: $(SRC:%.c=%)

.PHONY: clean
clean:
	rm -f $(SRC:%.c=%)
