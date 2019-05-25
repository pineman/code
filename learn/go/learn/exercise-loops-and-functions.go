// flowcontrol/8
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	if x < 0 {
		return 0 // Error
	}

	const Delta = 1e-15
	const InitialGuess = 1.0

	z := InitialGuess
	step := func() float64 {
		return (z*z - x) / (2 * x)
	}

	for t := step(); math.Abs(t) > Delta; t = step() {
		//fmt.Println(z, t)
		z -= t
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
