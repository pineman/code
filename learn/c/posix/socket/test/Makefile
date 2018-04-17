#CC=
#CCX=
CFLAGS=-Wall -Wextra -pedantic
CFLAGS+=-O0
#CFLAGS+=-g -Og
#CFLAGS+=-pg
#CXXFLAGS=$(CFLAGS)
CPPFLAGS=
LDFLAGS=
LDLIBS=
SRCDIR=.
SRC!=find $(SRCDIR) -type f -name "*.c"

all: $(SRC:%.c=%)

.PHONY: clean
clean:
	rm -f $(SRC:%.c=%)
