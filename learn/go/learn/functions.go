package main

import (
	"fmt"
)

func squareAndCube(x int) (square, cube int) {
	square = x * x
	cube = square * square
	return
}

func main() {
	fmt.Println(squareAndCube(4))

	a, b := squareAndCube(5)
	fmt.Println(a, b)
}
