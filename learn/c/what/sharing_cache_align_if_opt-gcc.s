	.file	"sharing_cache_align_if.c"
	.intel_syntax noprefix
# GNU C17 (Arch Linux 9.3.0-1) version 9.3.0 (x86_64-pc-linux-gnu)
#	compiled by GNU C version 9.3.0, GMP version 6.2.0, MPFR version 4.0.2, MPC version 1.1.0, isl version isl-0.21-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -fdiagnostics-color=always -D_REENTRANT
# sharing_cache_align_if.c -masm=intel -mtune=generic -march=x86-64
# -auxbase-strip sharing_cache_align_if_opt.s -O3 -fverbose-asm
# options enabled:  -fPIC -fPIE -faggressive-loop-optimizations
# -falign-functions -falign-jumps -falign-labels -falign-loops
# -fassume-phsa -fasynchronous-unwind-tables -fauto-inc-dec
# -fbranch-count-reg -fcaller-saves -fcode-hoisting
# -fcombine-stack-adjustments -fcommon -fcompare-elim -fcprop-registers
# -fcrossjumping -fcse-follow-jumps -fdefer-pop
# -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively
# -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
# -fexpensive-optimizations -fforward-propagate -ffp-int-builtin-inexact
# -ffunction-cse -fgcse -fgcse-after-reload -fgcse-lm -fgnu-runtime
# -fgnu-unique -fguess-branch-probability -fhoist-adjacent-loads -fident
# -fif-conversion -fif-conversion2 -findirect-inlining -finline
# -finline-atomics -finline-functions -finline-functions-called-once
# -finline-small-functions -fipa-bit-cp -fipa-cp -fipa-cp-clone -fipa-icf
# -fipa-icf-functions -fipa-icf-variables -fipa-profile -fipa-pure-const
# -fipa-ra -fipa-reference -fipa-reference-addressable -fipa-sra
# -fipa-stack-alignment -fipa-vrp -fira-hoist-pressure
# -fira-share-save-slots -fira-share-spill-slots
# -fisolate-erroneous-paths-dereference -fivopts -fkeep-static-consts
# -fleading-underscore -flifetime-dse -floop-interchange
# -floop-unroll-and-jam -flra-remat -flto-odr-type-merging -fmath-errno
# -fmerge-constants -fmerge-debug-strings -fmove-loop-invariants
# -fomit-frame-pointer -foptimize-sibling-calls -foptimize-strlen
# -fpartial-inlining -fpeel-loops -fpeephole -fpeephole2 -fplt
# -fpredictive-commoning -fprefetch-loop-arrays -free -freg-struct-return
# -freorder-blocks -freorder-blocks-and-partition -freorder-functions
# -frerun-cse-after-loop -fsched-critical-path-heuristic
# -fsched-dep-count-heuristic -fsched-group-heuristic -fsched-interblock
# -fsched-last-insn-heuristic -fsched-rank-heuristic -fsched-spec
# -fsched-spec-insn-heuristic -fsched-stalled-insns-dep -fschedule-fusion
# -fschedule-insns2 -fsemantic-interposition -fshow-column -fshrink-wrap
# -fshrink-wrap-separate -fsigned-zeros -fsplit-ivs-in-unroller
# -fsplit-loops -fsplit-paths -fsplit-wide-types -fssa-backprop
# -fssa-phiopt -fstack-protector-strong -fstdarg-opt -fstore-merging
# -fstrict-aliasing -fstrict-volatile-bitfields -fsync-libcalls
# -fthread-jumps -ftoplevel-reorder -ftrapping-math -ftree-bit-ccp
# -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars
# -ftree-copy-prop -ftree-cselim -ftree-dce -ftree-dominator-opts
# -ftree-dse -ftree-forwprop -ftree-fre -ftree-loop-distribute-patterns
# -ftree-loop-distribution -ftree-loop-if-convert -ftree-loop-im
# -ftree-loop-ivcanon -ftree-loop-optimize -ftree-loop-vectorize
# -ftree-parallelize-loops= -ftree-partial-pre -ftree-phiprop -ftree-pre
# -ftree-pta -ftree-reassoc -ftree-scev-cprop -ftree-sink
# -ftree-slp-vectorize -ftree-slsr -ftree-sra -ftree-switch-conversion
# -ftree-tail-merge -ftree-ter -ftree-vrp -funit-at-a-time -funswitch-loops
# -funwind-tables -fverbose-asm -fversion-loops-for-strides
# -fzero-initialized-in-bss -m128bit-long-double -m64 -m80387
# -malign-stringops -mavx256-split-unaligned-load
# -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387 -mfxsr
# -mglibc -mieee-fp -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone
# -msse -msse2 -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.p2align 4
	.globl	thread
	.type	thread, @function
thread:
.LFB12:
	.cfi_startproc
	cmp	DWORD PTR [rdi], 1	# MEM[(int *)arg_7(D)],
	lea	rdx, share[rip]	# tmp93,
	je	.L2	#,
	.p2align 4,,10
	.p2align 3
.L3:
# sharing_cache_align_if.c:29: 			share.b++;
	mov	rax, QWORD PTR share[rip+64]	# _13, share.b
# sharing_cache_align_if.c:29: 			share.b++;
	add	rax, 1	# _14,
	mov	QWORD PTR share[rip+64], rax	# share.b, _14
	jmp	.L3	#
.L2:
# sharing_cache_align_if.c:26: 			share.a++;
	mov	rax, QWORD PTR [rdx]	# _1, share.a
# sharing_cache_align_if.c:26: 			share.a++;
	add	rax, 1	# _2,
	mov	QWORD PTR [rdx], rax	# share.a, _2
# sharing_cache_align_if.c:26: 			share.a++;
	mov	rax, QWORD PTR [rdx]	# _1, share.a
# sharing_cache_align_if.c:26: 			share.a++;
	add	rax, 1	# _2,
	mov	QWORD PTR [rdx], rax	# share.a, _2
	jmp	.L2	#
	.cfi_endproc
.LFE12:
	.size	thread, .-thread
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC0:
	.string	"a = %lu, b = %lu, total = %lu\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB13:
	.cfi_startproc
	sub	rsp, 40	#,
	.cfi_def_cfa_offset 48
# sharing_cache_align_if.c:38: 	pthread_create(&a, NULL, thread, (void *) &a_arg);
	xor	esi, esi	#
	lea	rdx, thread[rip]	#,
# sharing_cache_align_if.c:35: {
	mov	rax, QWORD PTR fs:40	# tmp102, MEM[(<address-space-1> long unsigned int *)40B]
	mov	QWORD PTR 24[rsp], rax	# D.3982, tmp102
	xor	eax, eax	# tmp102
# sharing_cache_align_if.c:38: 	pthread_create(&a, NULL, thread, (void *) &a_arg);
	mov	rcx, rsp	# tmp91,
	lea	rdi, 8[rsp]	# tmp92,
# sharing_cache_align_if.c:36: 	int a_arg = 1, b_arg = 2;
	mov	DWORD PTR [rsp], 1	# a_arg,
# sharing_cache_align_if.c:36: 	int a_arg = 1, b_arg = 2;
	mov	DWORD PTR 4[rsp], 2	# b_arg,
# sharing_cache_align_if.c:38: 	pthread_create(&a, NULL, thread, (void *) &a_arg);
	call	pthread_create@PLT	#
# sharing_cache_align_if.c:39: 	pthread_create(&b, NULL, thread, (void *) &b_arg);
	xor	esi, esi	#
	lea	rcx, 4[rsp]	# tmp93,
	lea	rdx, thread[rip]	#,
	lea	rdi, 16[rsp]	# tmp94,
	call	pthread_create@PLT	#
# sharing_cache_align_if.c:40: 	sleep(1);
	mov	edi, 1	#,
	call	sleep@PLT	#
# sharing_cache_align_if.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	mov	rcx, QWORD PTR share[rip]	# _1, share.a
# sharing_cache_align_if.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	mov	rax, QWORD PTR share[rip+64]	# _2, share.b
# sharing_cache_align_if.c:41: 	printf("a = %lu, b = %lu, total = %lu\n", share.a, share.b, share.a + share.b);
	lea	rdi, .LC0[rip]	#,
	mov	rdx, QWORD PTR share[rip+64]	# _4, share.b
	mov	rsi, QWORD PTR share[rip]	# _5, share.a
	add	rcx, rax	# tmp99, _2
	xor	eax, eax	#
	call	printf@PLT	#
# sharing_cache_align_if.c:42: }
	mov	rax, QWORD PTR 24[rsp]	# tmp103, D.3982
	xor	rax, QWORD PTR fs:40	# tmp103, MEM[(<address-space-1> long unsigned int *)40B]
	jne	.L9	#,
	xor	eax, eax	#
	add	rsp, 40	#,
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret	
.L9:
	.cfi_restore_state
	call	__stack_chk_fail@PLT	#
	.cfi_endproc
.LFE13:
	.size	main, .-main
	.comm	share,128,64
	.ident	"GCC: (Arch Linux 9.3.0-1) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
