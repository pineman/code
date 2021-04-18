package main

import (
	"fmt"
	"math"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %v\n", float64(e))
}

func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}

	const Delta = 1e-12
	const InitialGuess = 1.0

	z := InitialGuess
	step := func() float64 {
		return (z*z - x) / (2 * x)
	}

	for t := step(); math.Abs(t) > Delta; t = step() {
		z -= t
	}
	return z, nil
}

func main() {
	// Doesn't compile if ErrNegativeSqrt doesn't implement the `error` interface.
	var _ error = (*ErrNegativeSqrt)(nil)
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2))
}
