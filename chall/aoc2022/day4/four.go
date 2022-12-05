package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func partOne(input []string) int {
	t := 0
	for _, v := range input {
		aMin, aMax, bMin, bMax := 0, 0, 0, 0
		fmt.Sscanf(v, "%d-%d,%d-%d", &aMin, &aMax, &bMin, &bMax)
		if bMin >= aMin && bMax <= aMax || aMin >= bMin && aMax <= bMax {
			t++
		}
	}
	return t
}

func partTwo(input []string) int {
	t := 0
	for _, v := range input {
		aMin, aMax, bMin, bMax := 0, 0, 0, 0
		fmt.Sscanf(v, "%d-%d,%d-%d", &aMin, &aMax, &bMin, &bMax)
		if (bMin <= aMax && bMax >= aMin) || (aMin <= bMax && aMax >= bMin) {
			t++
		}
	}
	return t
}

func main() {
	input := aoc2022.GetInput(4)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
