package main

import (
	"fmt"
	"sort"
	"strconv"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func dayOne(input []string) []int {
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
	result := dayOne(input)
	t := 0
	for _, v := range result {
		if v > t {
			t = v
		}
	}
	return t
}

func partTwo(input []string) int {
	result := dayOne(input)
	sort.Ints(result)
	r := 0
	for _, v := range result[len(result)-3:] {
		r += v
	}
	return r
}

func main() {
	input := aoc2022.GetInput(1)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
