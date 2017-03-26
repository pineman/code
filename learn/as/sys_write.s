	.data
hello:
	.ascii	"Hello world!\n"
	.set STR_SIZE, . - hello

	.text
	.globl _start
	.globl exit
_start:
	movl	$4, %eax
	movl	$1, %ebx
	movl	$hello, %ecx
	movl	$STR_SIZE, %edx
	int		$0x80
	call	exit
