package main

import (
	"fmt"
	"testing"
)

func Test_partOne(t *testing.T) {
	type args struct {
		input  []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"normal", args{getInput(), 2020}, 691771},
		{"bigboy", args{getBigBoy(), 99920044}, 1939883877222459},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partOne(tt.args.input, tt.args.target); got != tt.want {
				t.Errorf("partOne() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partTwo(t *testing.T) {
	type args struct {
		input  []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"normal", args{getInput(), 2020}, 232508760},
		// {"bigboy", args{getBigBoy(), 99920044}, 32625808479480099854130},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := partTwo(tt.args.input, tt.args.target); got != tt.want {
				t.Errorf("partTwo() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Benchmark_partTwo(b *testing.B) {
	for i := 0; i < b.N; i++ {
		partTwo(getInput(), 2020)
	}
}

func Test_twoSum(t *testing.T) {
	type args struct {
		input  []int
		target int
	}
	tests := []struct {
		args    args
		want    int
		want1   int
		wantErr bool
	}{
		{args{[]int{50, 50}, 100}, 50, 50, false},
		{args{[]int{50, 50, 1}, 100}, 50, 50, false},
		{args{[]int{50, 2, 50}, 110}, -1, -1, true},
	}
	for _, tt := range tests {
		name := fmt.Sprintf("input %v, target %v", tt.args.input, tt.args.target)
		t.Run(name, func(t *testing.T) {
			got, got1, err := twoSum(tt.args.input, tt.args.target)
			if (err != nil) != tt.wantErr {
				t.Errorf("twoSum() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("twoSum() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("twoSum() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_threeSum(t *testing.T) {
	type args struct {
		input  []int
		target int
	}
	tests := []struct {
		args    args
		want    int
		want1   int
		want2   int
		wantErr bool
	}{
		{args{[]int{30, 30, 30}, 90}, 30, 30, 30, false},
		{args{[]int{30, 30, 1, 30}, 90}, 30, 30, 30, false},
		{args{[]int{30, 30, 1, 30}, 100}, -1, -1, -1, true},
	}
	for _, tt := range tests {
		name := fmt.Sprintf("input %v, target %v", tt.args.input, tt.args.target)
		t.Run(name, func(t *testing.T) {
			got, got1, got2, err := threeSum(tt.args.input, tt.args.target)
			if (err != nil) != tt.wantErr {
				t.Errorf("threeSum() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("threeSum() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("threeSum() got1 = %v, want %v", got1, tt.want1)
			}
			if got2 != tt.want2 {
				t.Errorf("threeSum() got2 = %v, want %v", got2, tt.want2)
			}
		})
	}
}
