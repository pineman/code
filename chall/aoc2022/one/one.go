package main

import (
	"fmt"
	"sort"
	"strconv"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func elves(input []string) []int {
	s := []int{}
	t := 0
	for _, v := range input {
		if v == "" {
			s = append(s, t)
			t = 0
		} else {
			i, _ := strconv.Atoi(v)
			t += i
		}
	}
	return s
}

func partOne(input []string) int {
	elves := elves(input)
	max := 0
	for _, v := range elves {
		if v > max {
			max = v
		}
	}
	return max
}

func partTwo(input []string) int {
	elves := elves(input)
	sort.Ints(elves)
	topThree := 0
	for _, v := range elves[len(elves)-3:] {
		topThree += v
	}
	return topThree
}

func main() {
	input := aoc2022.GetInput(1)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
