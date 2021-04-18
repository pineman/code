package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) (m map[string]int) {
	m = make(map[string]int)
	slice := strings.Fields(s)
	for _, v := range slice {
		m[v]++
	}
	return
}

func main() {
	wc.Test(WordCount)
}
