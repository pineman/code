#CC=clang
#CXX=
CFLAGS=-Wall -Wextra -pedantic -Wunused-result -Wunreachable-code
#CFLAGS+=-O0
CFLAGS+=-g -Og
#CFLAGS+=-pg
CFLAGS+=-fdiagnostics-color=always
#CXXFLAGS=$(CFLAGS)
CPPFLAGS=
LDFLAGS=
LDLIBS=
SRCDIR=.
SRC=$(shell find $(SRCDIR) -type f -name "*.c")

all: $(SRC:%.c=%)

.PHONY: clean remake
clean:
	rm -f $(SRC:%.c=%)

remake:
	$(MAKE) clean
	$(MAKE)
