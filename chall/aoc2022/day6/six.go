package main

import (
	"fmt"
	"math/bits"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

// func isAllDifferent_terrible(s string) bool {
// 	r := map[rune]int{}
// 	for _, v := range s {
// 		r[v] += 1
// 	}
// 	for _, v := range r {
// 		if v != 1 {
// 			return false
// 		}
// 	}
// 	return true
// }

func isAllDifferent(s string) bool {
	var b uint32
	for _, v := range s {
		b += 1 << (v & 0b00011111)
		//b += 1 << (v - 'a')
	}
	return bits.OnesCount32(b) == len(s)
}

func partOne(input []string) int {
	in := input[0]
	i := 0
	for ; i < len(in); i++ {
		if isAllDifferent(in[i : i+4]) {
			break
		}
	}
	return i + 4
}

func partTwo(input []string) int {
	in := input[0]
	i := 0
	for ; i < len(in); i++ {
		if isAllDifferent(in[i : i+14]) {
			break
		}
	}
	return i + 14
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// func window(input []string, marker_size int) int {
// 	in := input[0]
// 	m := map[byte]int{}
// 	start, end := 0, 0
// 	for end-start < marker_size {
// 		c := in[end]
// 		if v, ok := m[c]; ok {
// 			start = max(start, v+1)
// 		}
// 		m[c] = end
// 		end++
// 	}
// 	return end
// }

// TODO: seems to fail on example input for part one
func window_array(input string, marker_size int) int {
	m := [26]int{0}
	start, end := 0, 0
	for end-start < marker_size {
		index := input[end] - 'a'
		if v := m[index]; v != 0 {
			start = max(start, v+1)
		}
		m[index] = end
		end++
	}
	return end
}

// TODO: seems to fail on example input for part one
func window_array_bits(input string, marker_size int) int {
	m := [32]int{0}
	start, end := 0, 0
	for end-start < marker_size {
		index := input[end] & 0b00011111
		if v := m[index]; v != 0 {
			start = max(start, v+1)
		}
		m[index] = end
		end++
	}
	return end
}

func partTwo_faster(input []string) int {
	return window_array(input[0], 14)
}

func partOne_fasterer(input []string) int {
	return window_array_bits(input[0], 4)
}

func partTwo_fasterer(input []string) int {
	return window_array_bits(input[0], 14)
}

func main() {
	input := aoc2022.GetInput(6)
	fmt.Println(partOne(input))
	fmt.Println(partOne_fasterer(input))
	fmt.Println(partTwo(input))
	fmt.Println(partTwo_fasterer(input))
	input = aoc2022.GetBigBoyInput(6)
	fmt.Println(partOne(input))
	fmt.Println(partOne_fasterer(input))
	fmt.Println(partTwo(input))
	fmt.Println(partTwo_fasterer(input))
}
