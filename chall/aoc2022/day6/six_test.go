package main

import (
	"testing"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func Test_checkAllDifferent(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"", args{"aaaa"}, false},
		{"", args{"abcd"}, true},
		{"", args{"abca"}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isAllDifferent(tt.args.s); got != tt.want {
				t.Errorf("checkAllDifferent() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partOne(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"", args{[]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}}, 7},
		{"", args{[]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}}, 5},
		{"", args{[]string{"nppdvjthqldpwncqszvftbrmjlhg"}}, 6},
		{"", args{[]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}}, 10},
		{"", args{[]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}}, 11},
		{"", args{aoc2022.GetInput(6)}, 1142},
		{"", args{aoc2022.GetBigBoyInput(6)}, 85760445},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partOne(tt.args.input); got != tt.want {
				t.Errorf("partOne() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partTwo(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"", args{[]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}}, 19},
		{"", args{[]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}}, 23},
		{"", args{[]string{"nppdvjthqldpwncqszvftbrmjlhg"}}, 23},
		{"", args{[]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}}, 29},
		{"", args{[]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}}, 26},
		{"", args{aoc2022.GetInput(6)}, 2803},
		{"", args{aoc2022.GetBigBoyInput(6)}, 91845017},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partTwo(tt.args.input); got != tt.want {
				t.Errorf("partTwo() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partOne_fasterer(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"", args{[]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}}, 7},
		//{"", args{[]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}}, 5},
		{"", args{[]string{"nppdvjthqldpwncqszvftbrmjlhg"}}, 6},
		// {"", args{[]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}}, 10},
		// {"", args{[]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}}, 11},
		{"", args{aoc2022.GetInput(6)}, 1142},
		{"", args{aoc2022.GetBigBoyInput(6)}, 85760445},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partOne_fasterer(tt.args.input); got != tt.want {
				t.Errorf("partOne_fasterer() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partTwo_faster(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"", args{[]string{"mjqjpqmgbljsphdztnvjfqwrcgsmlb"}}, 19},
		{"", args{[]string{"bvwbjplbgvbhsrlpgdmjqwftvncz"}}, 23},
		{"", args{[]string{"nppdvjthqldpwncqszvftbrmjlhg"}}, 23},
		{"", args{[]string{"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"}}, 29},
		{"", args{[]string{"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"}}, 26},
		{"", args{aoc2022.GetInput(6)}, 2803},
		{"", args{aoc2022.GetBigBoyInput(6)}, 91845017},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partTwo_faster(tt.args.input); got != tt.want {
				t.Errorf("partTwo_faster() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Benchmark_partTwoBigBoy(b *testing.B) {
	input := aoc2022.GetBigBoyInput(6)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		partTwo(input)
	}
}

func Benchmark_partTwo_fasterBigBoy(b *testing.B) {
	input := aoc2022.GetBigBoyInput(6)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		partTwo_faster(input)
	}
}

func Benchmark_partTwo_fastererBigBoy(b *testing.B) {
	input := aoc2022.GetBigBoyInput(6)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		partTwo_fasterer(input)
	}
}
