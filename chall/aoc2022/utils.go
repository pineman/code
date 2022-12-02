package aoc2022

import (
	"fmt"
	"os"
	"strings"
)

const base string = "../input"

func getInput(file string) []string {
	input, err := os.ReadFile(file)
	if err != nil {
		panic(err)
	}
	s := strings.Split(string(input), "\n")
	if s[len(s)-1] == "" {
		s = s[:len(s)-1]
	}
	return s
}

func GetInput(day int) []string {
	file := fmt.Sprintf("%v/%v/input", base, day)
	return getInput(file)
}

func GetBigBoyInput(day int) []string {
	file := fmt.Sprintf("%v/%v/bigboy", base, day)
	return getInput(file)
}
