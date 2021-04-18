	.file	"sharing_cache_align.c"
	.intel_syntax noprefix
# GNU C17 (Arch Linux 9.3.0-1) version 9.3.0 (x86_64-pc-linux-gnu)
#	compiled by GNU C version 9.3.0, GMP version 6.2.0, MPFR version 4.0.2, MPC version 1.1.0, isl version isl-0.21-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -fdiagnostics-color=always -D_REENTRANT
# sharing_cache_align.c -masm=intel -mtune=generic -march=x86-64
# -auxbase-strip sharing_cache_align.s -O0 -fverbose-asm
# options enabled:  -fPIC -fPIE -faggressive-loop-optimizations
# -fassume-phsa -fasynchronous-unwind-tables -fauto-inc-dec -fcommon
# -fdelete-null-pointer-checks -fdwarf2-cfi-asm -fearly-inlining
# -feliminate-unused-debug-types -ffp-int-builtin-inexact -ffunction-cse
# -fgcse-lm -fgnu-runtime -fgnu-unique -fident -finline-atomics
# -fipa-stack-alignment -fira-hoist-pressure -fira-share-save-slots
# -fira-share-spill-slots -fivopts -fkeep-static-consts
# -fleading-underscore -flifetime-dse -flto-odr-type-merging -fmath-errno
# -fmerge-debug-strings -fpeephole -fplt -fprefetch-loop-arrays
# -freg-struct-return -fsched-critical-path-heuristic
# -fsched-dep-count-heuristic -fsched-group-heuristic -fsched-interblock
# -fsched-last-insn-heuristic -fsched-rank-heuristic -fsched-spec
# -fsched-spec-insn-heuristic -fsched-stalled-insns-dep -fschedule-fusion
# -fsemantic-interposition -fshow-column -fshrink-wrap-separate
# -fsigned-zeros -fsplit-ivs-in-unroller -fssa-backprop
# -fstack-protector-strong -fstdarg-opt -fstrict-volatile-bitfields
# -fsync-libcalls -ftrapping-math -ftree-cselim -ftree-forwprop
# -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
# -ftree-loop-optimize -ftree-parallelize-loops= -ftree-phiprop
# -ftree-reassoc -ftree-scev-cprop -funit-at-a-time -funwind-tables
# -fverbose-asm -fzero-initialized-in-bss -m128bit-long-double -m64 -m80387
# -malign-stringops -mavx256-split-unaligned-load
# -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387 -mfxsr
# -mglibc -mieee-fp -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone
# -msse -msse2 -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.comm	share,128,64
	.globl	thread_a
	.type	thread_a, @function
thread_a:
.LFB0:
	.cfi_startproc
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	mov	QWORD PTR -8[rbp], rdi	# arg, arg
.L2:
# sharing_cache_align.c:24: 		share.a++;
	mov	rax, QWORD PTR share[rip]	# _1, share.a
# sharing_cache_align.c:24: 		share.a++;
	add	rax, 1	# _2,
	mov	QWORD PTR share[rip], rax	# share.a, _2
	jmp	.L2	#
	.cfi_endproc
.LFE0:
	.size	thread_a, .-thread_a
	.globl	thread_b
	.type	thread_b, @function
thread_b:
.LFB1:
	.cfi_startproc
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	mov	QWORD PTR -8[rbp], rdi	# arg, arg
.L4:
# sharing_cache_align.c:31: 		share.b++;
	mov	rax, QWORD PTR share[rip+64]	# _1, share.b
# sharing_cache_align.c:31: 		share.b++;
	add	rax, 1	# _2,
	mov	QWORD PTR share[rip+64], rax	# share.b, _2
	jmp	.L4	#
	.cfi_endproc
.LFE1:
	.size	thread_b, .-thread_b
	.section	.rodata
	.align 8
.LC0:
	.string	"a = %lu, b = %lu, total = %lu\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	sub	rsp, 48	#,
	mov	DWORD PTR -36[rbp], edi	# argc, argc
	mov	QWORD PTR -48[rbp], rsi	# argv, argv
# sharing_cache_align.c:36: {
	mov	rax, QWORD PTR fs:40	# tmp92, MEM[(<address-space-1> long unsigned int *)40B]
	mov	QWORD PTR -8[rbp], rax	# D.3935, tmp92
	xor	eax, eax	# tmp92
# sharing_cache_align.c:38: 	pthread_create(&a, NULL, thread_a, NULL);
	lea	rax, -24[rbp]	# tmp89,
	mov	ecx, 0	#,
	lea	rdx, thread_a[rip]	#,
	mov	esi, 0	#,
	mov	rdi, rax	#, tmp89
	call	pthread_create@PLT	#
# sharing_cache_align.c:39: 	pthread_create(&b, NULL, thread_b, NULL);
	lea	rax, -16[rbp]	# tmp90,
	mov	ecx, 0	#,
	lea	rdx, thread_b[rip]	#,
	mov	esi, 0	#,
	mov	rdi, rax	#, tmp90
	call	pthread_create@PLT	#
# sharing_cache_align.c:40: 	sleep(1);
	mov	edi, 1	#,
	call	sleep@PLT	#
# sharing_cache_align.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	mov	rdx, QWORD PTR share[rip]	# _1, share.a
# sharing_cache_align.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	mov	rax, QWORD PTR share[rip+64]	# _2, share.b
# sharing_cache_align.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	lea	rcx, [rdx+rax]	# _3,
	mov	rdx, QWORD PTR share[rip+64]	# _4, share.b
	mov	rax, QWORD PTR share[rip]	# _5, share.a
	mov	rsi, rax	#, _5
	lea	rdi, .LC0[rip]	#,
	mov	eax, 0	#,
	call	printf@PLT	#
	mov	eax, 0	# _13,
# sharing_cache_align.c:42: }
	mov	rsi, QWORD PTR -8[rbp]	# tmp93, D.3935
	xor	rsi, QWORD PTR fs:40	# tmp93, MEM[(<address-space-1> long unsigned int *)40B]
	je	.L7	#,
	call	__stack_chk_fail@PLT	#
.L7:
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Arch Linux 9.3.0-1) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
