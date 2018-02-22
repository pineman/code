package main

import (
	"fmt"
)

func square_and_cube(x int) (return_value1, return_value2 int) {
	return_value1 = x * x
	return_value2 = return_value1 * return_value1
	return
}

func main() {
	fmt.Println(square_and_cube(4)
	//fmt.Println(square_and_cube(4), 4)

	a, b := square_and_cube(5)
}
