	.text
	.intel_syntax noprefix
	.file	"sharing_cache_align.c"
	.globl	thread_a                # -- Begin function thread_a
	.p2align	4, 0x90
	.type	thread_a,@function
thread_a:                               # @thread_a
	.cfi_startproc
# %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	mov	rax, qword ptr [rip + share]
	add	rax, 1
	mov	qword ptr [rip + share], rax
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
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
.LBB1_1:                                # =>This Inner Loop Header: Depth=1
	mov	rax, qword ptr [rip + share+64]
	add	rax, 1
	mov	qword ptr [rip + share+64], rax
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
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 80
	mov	rax, qword ptr fs:[40]
	mov	qword ptr [rbp - 8], rax
	mov	dword ptr [rbp - 28], edi
	mov	qword ptr [rbp - 40], rsi
	lea	rdx, [rip + thread_a]
	xor	ecx, ecx
	mov	eax, ecx
	lea	rdi, [rbp - 16]
	mov	rsi, rax
	mov	dword ptr [rbp - 44], ecx # 4-byte Spill
	mov	rcx, rax
	mov	qword ptr [rbp - 56], rax # 8-byte Spill
	call	pthread_create@PLT
	lea	rdx, [rip + thread_b]
	lea	rdi, [rbp - 24]
	mov	rsi, qword ptr [rbp - 56] # 8-byte Reload
	mov	rcx, qword ptr [rbp - 56] # 8-byte Reload
	mov	dword ptr [rbp - 60], eax # 4-byte Spill
	call	pthread_create@PLT
	mov	edi, 1
	mov	dword ptr [rbp - 64], eax # 4-byte Spill
	call	sleep@PLT
	mov	rsi, qword ptr [rip + share]
	mov	rdx, qword ptr [rip + share+64]
	mov	rcx, qword ptr [rip + share]
	mov	r8, qword ptr [rip + share+64]
	add	rcx, r8
	lea	rdi, [rip + .L.str]
	mov	r9d, dword ptr [rbp - 44] # 4-byte Reload
	mov	dword ptr [rbp - 68], eax # 4-byte Spill
	mov	al, r9b
	call	printf@PLT
	mov	rcx, qword ptr fs:[40]
	mov	rdx, qword ptr [rbp - 8]
	cmp	rcx, rdx
	jne	.LBB2_2
# %bb.1:
	xor	eax, eax
	add	rsp, 80
	pop	rbp
	.cfi_def_cfa rsp, 8
	ret
.LBB2_2:
	.cfi_def_cfa rbp, 16
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
	.addrsig_sym pthread_create
	.addrsig_sym sleep
	.addrsig_sym printf
	.addrsig_sym __stack_chk_fail
	.addrsig_sym share
