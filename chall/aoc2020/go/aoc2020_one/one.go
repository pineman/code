package main

import (
	"errors"
	"fmt"
	"sort"
	"strconv"

	aoc2020 "github.com/pineman/code/chall/aoc2020/go"
)

func getInput() []int {
	return intInput(aoc2020.GetInput(1))
}

func getBigBoy() []int {
	return intInput(aoc2020.GetBigBoy(1))
}

func intInput(input []string) []int {
	intInput := make([]int, len(input))
	for i, v := range input {
		v, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}
		intInput[i] = v
	}
	return intInput
}

func twoSum(input []int, target int) (int, int, error) {
	sort.Ints(input)
	l, r := 0, len(input)-1
	for l != r {
		s := input[l] + input[r]
		if s == target {
			return input[l], input[r], nil
		} else if s < target {
			l++
		} else {
			r--
		}
	}
	return -1, -1, errors.New("twoSum: could not find two numbers in input that sum to target")
}

func threeSum(input []int, target int) (int, int, int, error) {
	sort.Ints(input)
	for i, v := range input {
		a, b, _ := twoSum(append(input[:i], input[i+1:]...), target-v)
		if a+b+v == target {
			return a, b, v, nil
		}
	}
	return -1, -1, -1, errors.New("threeSum: could not find three numbers in input that sum to target")
}

func partOne(input []int, target int) int {
	a, b, err := twoSum(input, target)
	if err != nil {
		panic(err)
	}
	return a * b
}

func partTwo(input []int, target int) int {
	a, b, c, err := threeSum(input, target)
	if err != nil {
		panic(err)
	}
	return a * b * c
}

func main() {
	input := getInput()
	fmt.Println(partOne(input, 2020))
	fmt.Println(partTwo(input, 2020))

	bigBoy := getBigBoy()
	fmt.Println(partOne(bigBoy, 99920044))
	// fmt.Println(partTwo(bigBoy, 99920044))
}
