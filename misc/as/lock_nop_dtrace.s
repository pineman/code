# dtrace's sdt provider makes the DTRACE_PROBE macro include an undefined
# extern function at the probe site. the kernel runtime linker then catches
# that undefined symbol and places 5 NOPs at its location. when an sdt probe
# is enabled, the first (or some other?) NOP is replaced by an 0xf0, which is
# the LOCK prefix instruction - creating effectively a LOCK NOP.
# it's an illegal instruction so it causes an #UD fault, as this file tests.
# the fault  is then handled by passing execution to dtrace itself (dtrace_invop).
# See
# https://web.archive.org/web/20161108030709/http://www.solarisinternals.com/wiki/index.php/DTrace_Topics_Overhead,
# https://www.cs.dartmouth.edu/~sergey/cs108/2009/dtrace-internals-x86.pdf
    .text
    .globl _start

_start:
    lock
    nop
    movq $60, %rax
    xor %rdi, %rdi
    syscall
