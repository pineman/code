package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

type stack []byte

func (s *stack) Push(v byte) {
	*s = append(*s, v)
}

func (s *stack) Pop() byte {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}

// The puzzle inputs are so well-crafted that it diminishes the fun - each row
// has trailing spaces up to the 36th column (=4 spaces each * 9 columns - 1)
func parseCrates(input []string) [9]stack {
	var crateColumns [9]stack
	for col := 0; col < 9; col++ {
		for row := 7; row >= 0; row-- {
			crate := input[row][col*4+1]
			if string(crate) != " " {
				crateColumns[col].Push(crate)
			}
		}
	}
	return crateColumns
}

func moveCrates(input []string, crates *[9]stack) {
	for _, v := range input {
		num, src, dst := 0, 0, 0
		fmt.Sscanf(v, "move %d from %d to %d", &num, &src, &dst)
		for j := 0; j < num; j++ {
			crates[dst-1].Push(crates[src-1].Pop())
		}
	}
}

func moveCrates9001(input []string, crates *[9]stack) {
	for _, v := range input {
		num, src, dst := 0, 0, 0
		fmt.Sscanf(v, "move %d from %d to %d", &num, &src, &dst)
		// Still cleaner than using slice and index arithmetic directly?
		var tmp []byte
		for i := 0; i < num; i++ {
			tmp = append(tmp, crates[src-1].Pop())
		}
		for i := num - 1; i >= 0; i-- {
			crates[dst-1].Push(tmp[i])
		}
	}
}

func partOne(input []string) string {
	crates := parseCrates(input[:8])
	moveCrates(input[10:], &crates)
	result := ""
	for i := range crates {
		result += string(crates[i][len(crates[i])-1])
	}
	return result
}

func partTwo(input []string) string {
	crates := parseCrates(input[:8])
	moveCrates9001(input[10:], &crates)
	result := ""
	for i := range crates {
		result += string(crates[i][len(crates[i])-1])
	}
	return result
}

func main() {
	input := aoc2022.GetInput(5)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
