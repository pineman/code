package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func partOne(input []string) int {
	t := 0
	for _, v := range input {
		firstMap, secondMap := buildCompartmentMaps(v)
		common := firstIntersection(firstMap, secondMap)
		priority := asciiToPriority(common)
		t += priority
	}
	return t
}

func buildCompartmentMaps(v string) (map[string]int, map[string]int) {
	firstMap, secondMap := map[string]int{}, map[string]int{}
	d := len(v)
	for c := 0; c < d/2; c++ {
		firstMap[string(v[c])] += 1
	}
	for c := d / 2; c < d; c++ {
		secondMap[string(v[c])] += 1
	}
	return firstMap, secondMap
}

func asciiToPriority(item string) int {
	char := int(item[0])
	if char <= 90 {
		// Uppercase
		return char - 65 + 27
	} else {
		// Lowercase
		return char - 97 + 1
	}
}

func firstIntersection(firstMap map[string]int, secondMap map[string]int) (common string) {
	for k := range firstMap {
		if secondMap[k] > 0 {
			common = k
		}
	}
	return
}

func main() {
	input := aoc2022.GetInput(3)
	fmt.Println(partOne(input))
}
