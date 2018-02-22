package main

import (
	"fmt"
)

func main() {
	var i int // Initialized as zero
	fmt.Println(i)

	var j = 2 // When an initialization is provided, `var` can be omitted.
	fmt.Println(j)

	k := 4
	fmt.Println(k)

	s := "hello"
	fmt.Println(s)
}
