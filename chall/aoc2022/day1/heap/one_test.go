package main

import "testing"

func Benchmark_heap(b *testing.B) {
	for i := 0; i < b.N; i++ {
		heap_main()
	}
}

func Benchmark_heap_fix(b *testing.B) {
	for i := 0; i < b.N; i++ {
		heap_fix_main()
	}
}
