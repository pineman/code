package main

import (
	"fmt"

	aoc2022 "github.com/pineman/code/chall/aoc2022/go"
)

func itemMap(items string) map[rune]int {
	itemMap := map[rune]int{}
	for _, v := range items {
		itemMap[v] += 1
	}
	return itemMap
}

// Excessively general for this context
func intersectMap(a map[rune]int, b map[rune]int) map[rune]int {
	common := map[rune]int{}
	for k, v := range a {
		if b[k] > 0 {
			common[k] = v + b[k]
		}
	}
	return common
}

func getFirstKey(a map[rune]int) (key rune) {
	for k := range a {
		key = k
		break
	}
	return
}

func asciiToPriority(item rune) int {
	char := int(item)
	if char <= 90 {
		// Uppercase
		return char - 65 + 27
	} else {
		// Lowercase
		return char - 97 + 1
	}
}

func partOne(input []string) int {
	t := 0
	for _, v := range input {
		common := intersectMap(itemMap(v[:len(v)/2]), itemMap(v[len(v)/2:]))
		priority := asciiToPriority(getFirstKey(common))
		t += priority
	}
	return t
}

func partTwo(input []string) int {
	t := 0
	for i := 0; i < len(input); i += 3 {
		common := intersectMap(intersectMap(itemMap(input[i]), itemMap(input[i+1])), itemMap(input[i+2]))
		priority := asciiToPriority(getFirstKey(common))
		t += priority
	}
	return t
}

func main() {
	input := aoc2022.GetInput(3)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
