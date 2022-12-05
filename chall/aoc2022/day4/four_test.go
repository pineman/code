package main

import (
	"testing"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func Test_partOne(t *testing.T) {
	type args struct {
		input []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"", args{aoc2022.GetInput(4)}, 487},
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
		{"", args{aoc2022.GetInput(4)}, 849},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partTwo(tt.args.input); got != tt.want {
				t.Errorf("partTwo() = %v, want %v", got, tt.want)
			}
		})
	}
}
