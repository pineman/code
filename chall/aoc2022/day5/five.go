package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

// TODO: try to use a linked list, inserting/removing at the head
type stack []byte

func (s *stack) Push(v byte) {
	*s = append(*s, v)
}

func (s *stack) Pop() byte {
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res
}

func getMatrixDimensions(input []string) (int, int) {
	rows, cols := 0, (len(input[0])+1)/4
	for i, v := range input {
		if v[:2] == " 1" {
			rows = i
			break
		}
	}
	return rows, cols
}

func parseCrates(input []string, rows int, cols int) []stack {
	crates := make([]stack, cols)
	for col := 0; col < cols; col++ {
		for row := rows - 1; row >= 0; row-- {
			crate := input[row][col*4+1]
			if string(crate) != " " {
				crates[col].Push(crate)
			}
		}
	}
	return crates
}

func moveCrates(input []string, crates *[]stack) {
	for _, v := range input {
		num, src, dst := 0, 0, 0
		fmt.Sscanf(v, "move %d from %d to %d", &num, &src, &dst)
		for j := 0; j < num; j++ {
			(*crates)[dst-1].Push((*crates)[src-1].Pop())
		}
	}
}

func moveCrates9001(input []string, crates *[]stack) {
	for _, v := range input {
		num, src, dst := 0, 0, 0
		fmt.Sscanf(v, "move %d from %d to %d", &num, &src, &dst)
		// Still cleaner than using slice and index arithmetic directly?
		var tmp []byte
		for i := 0; i < num; i++ {
			tmp = append(tmp, (*crates)[src-1].Pop())
		}
		for i := num - 1; i >= 0; i-- {
			(*crates)[dst-1].Push(tmp[i])
		}
	}
}

func getTopCrates(crates []stack) string {
	result := ""
	for i := range crates {
		result += string(crates[i].Pop())
	}
	return result
}

func partOne(input []string) string {
	rows, cols := getMatrixDimensions(input)
	crates := parseCrates(input[:rows], rows, cols)
	moveCrates(input[rows+2:], &crates)
	return getTopCrates(crates)
}

func partTwo(input []string) string {
	rows, cols := getMatrixDimensions(input)
	crates := parseCrates(input[:rows], rows, cols)
	moveCrates9001(input[rows+2:], &crates)
	return getTopCrates(crates)
}

func main() {
	input := aoc2022.GetInput(5)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
	input = aoc2022.GetBigBoyInput(5)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
