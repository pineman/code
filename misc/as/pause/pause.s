	.text
	.globl _start
_start:
	mov		$0x22,%al
	syscall
	mov		$0x3c,%al
	cltd
	syscall

