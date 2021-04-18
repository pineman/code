package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
// Also, the return function is a closure.
func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return b
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 20; i++ {
		fmt.Println(f())
	}
}
