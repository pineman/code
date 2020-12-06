package aoc2020

import (
	"fmt"
	"io/ioutil"
	"strings"
)

var base string = "/home/pineman/code/chall/aoc2020/input/"

func getInput(file string) []string {
	input, err := ioutil.ReadFile(file)
	if err != nil {
		panic(err)
	}
	s := strings.Split(string(input), "\n")
	if s[len(s)-1] == "" {
		s = s[:len(s)-1]
	}
	return s
	// dynamic copy without len, probably slower than apriori make with len and copy()
	// return append([]string{}, s...)
}

// GetInput returns the string of a day's input file
func GetInput(day int) []string {
	file := fmt.Sprintf("%v/%v/input", base, day)
	return getInput(file)
}

// GetBigBoy is the same as GetInput for bigboy inputs
func GetBigBoy(day int) []string {
	file := fmt.Sprintf("%v/%v/bigboy", base, day)
	return getInput(file)
}
