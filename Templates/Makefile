#CC=gcc -fstack-clash-protection
CC=clang
#CXX=
CFLAGS+= -std=c11 -fno-plt -pipe -fdiagnostics-color=always -march=native -pthread
CFLAGS+= -Wall -Wextra -Wpedantic -Wunused-result -Wunreachable-code -Werror=implicit-fallthrough=5
#CFLAGS+= -Weverything
#CFLAGS+= -O3 -flto
CFLAGS+= -g3 -Og
#CFLAGS+= -pg
#CFLAGS+= -D
CFLAGS+= -fsanitize=undefined
#CFLAGS+= -fsanitize=address -fsanitize=leak -fcheck-pointer-bounds
CFLAGS+= -fsanitize=thread
# Security flags
CFLAGS+= -D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fstack-protector-strong -fPIE
CFLAGS+= -I cb_common -I library -D_POSIX_C_SOURCE="200809L"
#CXXFLAGS=$(CFLAGS)
#LDFLAGS+= -fuse-ld=gold
LDFLAGS+= -z noexecstack -z relro -z now -pie
LDLIBS+=

SRCDIR=.
SRC=$(shell find $(SRCDIR) -type f -name "*.c" | cut -d"/" -f2-)

# Define executables and their link dependencies here
EXECS = exec1 exec2
exec1_DEPS = file1.c
exec1_LIBS = m
exec2_DEPS =
exec1_LIBS =

###############################################################################
# No more user editing is needed below
###############################################################################
OBJDIR=.obj

define EXEC_templ =
$(1): $$(addprefix $$(OBJDIR)/,$$($(1)_DEPS:%.c=%.o))
	$(CC) -o $$@ $$(LDFLAGS) $$(LDLIBS) $$($(1)_LIBS:%=-l%) $$^
endef

$(foreach exec,$(EXECS),$(eval $(call EXEC_templ,$(exec))))

-include $(addprefix $(OBJDIR)/, $(SRC:.c=.d))
$(OBJDIR)/%.d: %.c
	@mkdir -p `dirname $@`
	$(CC) $(CPPFLAGS) -MM -MF $@ $^

$(OBJDIR)/%.o: %.c
	$(CC) -c -o $@ $(CPPFLAGS) $(CFLAGS) $<

.PHONY=all clean remake
.DEFAULT_GOAL=all
all: $(EXECS)

clean:
	@rm -rf $(OBJDIR) $(EXECS)

remake:
	$(MAKE) clean
	$(MAKE)

# This rebuilds everything if the Makefile was modified
# http://stackoverflow.com/questions/3871444/making-all-rules-depend-on-the-makefile-itself/3892826#3892826
-include .dummy
.dummy: Makefile
	@touch $@
	@$(MAKE) -s clean
