	.text
	.intel_syntax noprefix
	.file	"sharing_cache_align_if.c"
	.globl	thread                  # -- Begin function thread
	.p2align	4, 0x90
	.type	thread,@function
thread:                                 # @thread
	.cfi_startproc
# %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
	mov	rax, qword ptr [rbp - 8]
	mov	ecx, dword ptr [rax]
	mov	dword ptr [rbp - 12], ecx
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	cmp	dword ptr [rbp - 12], 1
	jne	.LBB0_3
# %bb.2:                                #   in Loop: Header=BB0_1 Depth=1
	mov	rax, qword ptr [rip + share]
	add	rax, 1
	mov	qword ptr [rip + share], rax
	jmp	.LBB0_4
.LBB0_3:                                #   in Loop: Header=BB0_1 Depth=1
	mov	rax, qword ptr [rip + share+64]
	add	rax, 1
	mov	qword ptr [rip + share+64], rax
.LBB0_4:                                #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_1
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
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 96
	mov	rax, qword ptr fs:[40]
	mov	qword ptr [rbp - 8], rax
	mov	dword ptr [rbp - 36], edi
	mov	qword ptr [rbp - 48], rsi
	mov	dword ptr [rbp - 12], 1
	mov	dword ptr [rbp - 16], 2
	lea	rax, [rip + thread]
	xor	ecx, ecx
	mov	edx, ecx
	lea	rdi, [rbp - 24]
	lea	rsi, [rbp - 12]
	mov	qword ptr [rbp - 56], rsi # 8-byte Spill
	mov	rsi, rdx
	mov	qword ptr [rbp - 64], rdx # 8-byte Spill
	mov	rdx, rax
	mov	r8, qword ptr [rbp - 56] # 8-byte Reload
	mov	dword ptr [rbp - 68], ecx # 4-byte Spill
	mov	rcx, r8
	mov	qword ptr [rbp - 80], rax # 8-byte Spill
	call	pthread_create@PLT
	lea	rdi, [rbp - 32]
	lea	rcx, [rbp - 16]
	mov	rsi, qword ptr [rbp - 64] # 8-byte Reload
	mov	rdx, qword ptr [rbp - 80] # 8-byte Reload
	mov	dword ptr [rbp - 84], eax # 4-byte Spill
	call	pthread_create@PLT
	mov	edi, 1
	mov	dword ptr [rbp - 88], eax # 4-byte Spill
	call	sleep@PLT
	mov	rsi, qword ptr [rip + share]
	mov	rdx, qword ptr [rip + share+64]
	mov	rcx, qword ptr [rip + share]
	mov	r8, qword ptr [rip + share+64]
	add	rcx, r8
	lea	rdi, [rip + .L.str]
	mov	r9d, dword ptr [rbp - 68] # 4-byte Reload
	mov	dword ptr [rbp - 92], eax # 4-byte Spill
	mov	al, r9b
	call	printf@PLT
	mov	rcx, qword ptr fs:[40]
	mov	rdx, qword ptr [rbp - 8]
	cmp	rcx, rdx
	jne	.LBB1_2
# %bb.1:
	xor	eax, eax
	add	rsp, 96
	pop	rbp
	.cfi_def_cfa rsp, 8
	ret
.LBB1_2:
	.cfi_def_cfa rbp, 16
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
	.addrsig_sym pthread_create
	.addrsig_sym sleep
	.addrsig_sym printf
	.addrsig_sym __stack_chk_fail
	.addrsig_sym share
