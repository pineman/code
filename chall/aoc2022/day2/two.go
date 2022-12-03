package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func scoreMyShape(me string) int {
	var scoreMyShapeMap = map[string]int{
		"X": 1,
		"Y": 2,
		"Z": 3,
	}
	return scoreMyShapeMap[me]
}

func scoreOutcome(outcome string) int {
	var scoreOutcomeMap = map[string]int{
		"X": 0,
		"Y": 3,
		"Z": 6,
	}
	return scoreOutcomeMap[outcome]
}

func inferMyShape(them string, outcome string) string {
	var inferMyShapeMap = map[string]string{
		"A X": "Z",
		"A Y": "X",
		"A Z": "Y",
		"B X": "X",
		"B Y": "Y",
		"B Z": "Z",
		"C X": "Y",
		"C Y": "Z",
		"C Z": "X",
	}
	return inferMyShapeMap[them+" "+outcome]
}

func inferOutcome(them string, me string) string {
	var inferOutcomeMap = map[string]string{
		"A X": "Y",
		"A Y": "Z",
		"A Z": "X",
		"B X": "X",
		"B Y": "Y",
		"B Z": "Z",
		"C X": "Z",
		"C Y": "X",
		"C Z": "Y",
	}
	return inferOutcomeMap[them+" "+me]
}

func partOne(input []string) int {
	s := 0
	for _, v := range input {
		var them, me, outcome string
		fmt.Sscanf(v, "%s %s", &them, &me)
		outcome = inferOutcome(them, me)
		s += scoreMyShape(me)
		s += scoreOutcome(outcome)
	}
	return s
}

func partTwo(input []string) int {
	s := 0
	for _, v := range input {
		var them, me, outcome string
		fmt.Sscanf(v, "%s %s", &them, &outcome)
		me = inferMyShape(them, outcome)
		s += scoreMyShape(me)
		s += scoreOutcome(outcome)
	}
	return s
}

func main() {
	input := aoc2022.GetInput(2)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
