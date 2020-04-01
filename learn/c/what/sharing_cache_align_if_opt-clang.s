	.text
	.intel_syntax noprefix
	.file	"sharing_cache_align_if.c"
	.globl	thread                  # -- Begin function thread
	.p2align	4, 0x90
	.type	thread,@function
thread:                                 # @thread
	.cfi_startproc
# %bb.0:
	cmp	dword ptr [rdi], 1
	jne	.LBB0_2
	.p2align	4, 0x90
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	add	qword ptr [rip + share], 1
	jmp	.LBB0_1
	.p2align	4, 0x90
.LBB0_2:                                # =>This Inner Loop Header: Depth=1
	add	qword ptr [rip + share+64], 1
	jmp	.LBB0_2
.Lfunc_end0:
	.size	thread, .Lfunc_end0-thread
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	push	rbx
	.cfi_def_cfa_offset 16
	sub	rsp, 32
	.cfi_def_cfa_offset 48
	.cfi_offset rbx, -16
	mov	rax, qword ptr fs:[40]
	mov	qword ptr [rsp + 24], rax
	mov	dword ptr [rsp + 20], 1
	mov	dword ptr [rsp + 16], 2
	lea	rbx, [rip + thread]
	lea	rdi, [rsp + 8]
	lea	rcx, [rsp + 20]
	xor	esi, esi
	mov	rdx, rbx
	call	pthread_create@PLT
	mov	rdi, rsp
	lea	rcx, [rsp + 16]
	xor	esi, esi
	mov	rdx, rbx
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
	cmp	rax, qword ptr [rsp + 24]
	jne	.LBB1_2
# %bb.1:
	xor	eax, eax
	add	rsp, 32
	.cfi_def_cfa_offset 16
	pop	rbx
	.cfi_def_cfa_offset 8
	ret
.LBB1_2:
	.cfi_def_cfa_offset 48
	call	__stack_chk_fail@PLT
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
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
	.addrsig_sym thread
	.addrsig_sym __stack_chk_fail
	.addrsig_sym share
