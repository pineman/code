AS=as
#ASFLAGS=--gstabs
ASFLAGS=
LD=ld

all:
	$(MAKE) sys_write

clean:
	rm -f *.o
	rm -f sys_write

sys_write: sys_write.s sys_exit.s Makefile
	$(AS) $(ASFLAGS) -o sys_exit.o sys_exit.s
	$(AS) $(ASFLAGS) -o $@.o $@.s
	$(LD) -o $@ $@.o sys_exit.o
