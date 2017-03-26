	.text
	.globl exit

exit:
	movl	$1, %eax
	movl	$0, %ebx
	int		$0x80
	ret
