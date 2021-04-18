	.text
	.intel_syntax noprefix
	.file	"sharing_cache_align.c"
	.globl	thread_a                # -- Begin function thread_a
	.p2align	4, 0x90
	.type	thread_a,@function
thread_a:                               # @thread_a
	.cfi_startproc
# %bb.0:
	.p2align	4, 0x90
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	add	qword ptr [rip + share], 1
	jmp	.LBB0_1
.Lfunc_end0:
	.size	thread_a, .Lfunc_end0-thread_a
	.cfi_endproc
                                        # -- End function
	.globl	thread_b                # -- Begin function thread_b
	.p2align	4, 0x90
	.type	thread_b,@function
thread_b:                               # @thread_b
	.cfi_startproc
# %bb.0:
	.p2align	4, 0x90
.LBB1_1:                                # =>This Inner Loop Header: Depth=1
	add	qword ptr [rip + share+64], 1
	jmp	.LBB1_1
.Lfunc_end1:
	.size	thread_b, .Lfunc_end1-thread_b
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	sub	rsp, 24
	.cfi_def_cfa_offset 32
	mov	rax, qword ptr fs:[40]
	mov	qword ptr [rsp + 16], rax
	lea	rdx, [rip + thread_a]
	lea	rdi, [rsp + 8]
	xor	esi, esi
	xor	ecx, ecx
	call	pthread_create@PLT
	lea	rdx, [rip + thread_b]
	mov	rdi, rsp
	xor	esi, esi
	xor	ecx, ecx
	call	pthread_create@PLT
	mov	edi, 1
	call	sleep@PLT
	mov	rsi, qword ptr [rip + share]
	mov	rdx, qword ptr [rip + share+64]
	mov	rcx, qword ptr [rip + share]
	add	rcx, qword ptr [rip + share+64]
	lea	rdi, [rip + .L.str]
	xor	eax, eax
	call	printf@PLT
	mov	rax, qword ptr fs:[40]
	cmp	rax, qword ptr [rsp + 16]
	jne	.LBB2_2
# %bb.1:
	xor	eax, eax
	add	rsp, 24
	.cfi_def_cfa_offset 8
	ret
.LBB2_2:
	.cfi_def_cfa_offset 32
	call	__stack_chk_fail@PLT
.Lfunc_end2:
	.size	main, .Lfunc_end2-main
	.cfi_endproc
                                        # -- End function
	.type	share,@object           # @share
	.comm	share,128,64
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"a = %lu, b = %lu, total = %lu\n"
	.size	.L.str, 31


	.ident	"clang version 9.0.1 "
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym thread_a
	.addrsig_sym thread_b
	.addrsig_sym __stack_chk_fail
	.addrsig_sym share
