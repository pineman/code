#!/bin/sh

uname -a 
for CC in clang gcc; do
	echo ===== $($CC --version | head -n1) =====
	$CC -O0 -pthread sharing_cache_align.c -S -fverbose-asm -masm=intel -o sharing_cache_align-$CC.s 
	$CC -O3 -pthread sharing_cache_align.c -S -fverbose-asm -masm=intel -o sharing_cache_align_opt-$CC.s
	$CC -O0 -pthread sharing_cache_align_if.c -S -fverbose-asm -masm=intel -o sharing_cache_align_if-$CC.s
	$CC -O3 -pthread sharing_cache_align_if.c -S -fverbose-asm -masm=intel -o sharing_cache_align_if_opt-$CC.s

	$CC -O0 -pthread sharing_cache_align.c && echo "no if, no opts" && ./a.out
	$CC -O3 -pthread sharing_cache_align.c && echo "no if, yes opts" && ./a.out
	$CC -O0 -pthread sharing_cache_align_if.c && echo "yes if, no opts" && ./a.out 
	$CC -O3 -pthread sharing_cache_align_if.c && echo "yes if, yes opts" && ./a.out
done
