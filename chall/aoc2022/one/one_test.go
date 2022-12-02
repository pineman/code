package main

import (
	"fmt"
	"testing"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func Test_partOne(t *testing.T) {
	got := partOne(aoc2022.GetInput(1))
	want := 66306
	if got != want {
		t.Errorf("got = %d; want %d", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	got := partTwo(aoc2022.GetInput(1))
	want := 195292
	if got != want {
		t.Errorf("got = %d; want %d", got, want)
	}
}

func Benchmark_partTwo(b *testing.B) {
	for i := 0; i < b.N; i++ {
		input := aoc2022.GetInput(1)
		fmt.Println(partTwo(input))
	}
}
