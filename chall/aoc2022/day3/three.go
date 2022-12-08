package main

import (
	"fmt"
	"strings"
	"unicode"

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

func partOne_set(input []string) int {
	t := 0
	for _, v := range input {
		common := intersectMap(itemMap(v[:len(v)/2]), itemMap(v[len(v)/2:]))
		priority := priority(getFirstKey(common))
		t += priority
	}
	return t
}

func partTwo_set(input []string) int {
	t := 0
	for i := 0; i < len(input); i += 3 {
		common := intersectMap(intersectMap(itemMap(input[i]), itemMap(input[i+1])), itemMap(input[i+2]))
		priority := priority(getFirstKey(common))
		t += priority
	}
	return t
}

func priority(item rune) int {
	if unicode.IsUpper(item) {
		return int(item) - 'A' + 27
	} else {
		return int(item) - 'a' + 1
	}
}

func partOne(input []string) int {
	t := 0
	for _, v := range input {
		first := v[:len(v)/2]
		second := v[len(v)/2:]
		for _, c := range first {
			if strings.ContainsRune(second, c) {
				t += priority(c)
				break
			}
		}
	}
	return t
}

func partTwo(input []string) int {
	t := 0
	for i := 0; i < len(input); i += 3 {
		first := input[i]
		second := input[i+1]
		third := input[i+2]
		for _, c := range first {
			if strings.ContainsRune(second, c) && strings.ContainsRune(third, c) {
				t += priority(c)
				break
			}
		}
	}
	return t
}

func main() {
	input := aoc2022.GetInput(3)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
	input = aoc2022.GetBigBoyInput(3)
	fmt.Println(partOne(input))
	fmt.Println(partTwo(input))
}
