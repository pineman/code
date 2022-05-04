BITS 32
EXTERN _exit
GLOBAL _start
SECTION .text
_start:
	mov		al, 0x22
	syscall
	mov		al, 0x3c
	cltd
	syscall
