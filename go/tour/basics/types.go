package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

var (
	ToBe bool = false
	MaxInt uint64 = 1<<64 - 1
	Z complex128 = cmplx.Sqrt(-5 + 12i)
	Str string = "hello!"
	Char rune = '😃' // rune is aliased to int32.
	TwoNibbles byte = 255
)

func main() {
	fmt.Printf("Type: %T, Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T, Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T, Value: %v\n", Z, Z)
	fmt.Printf("Type: %T, Value: %v\n", Str, Str)
	fmt.Printf("Type: %T, Value: %U\n", Char, Char)
	fmt.Printf("Type: %T, Value: %v\n", TwoNibbles, TwoNibbles)

	// Type conversions (must be explicit)
	x, y := 3, 4
	f := math.Sqrt(float64(x*x+y*y)) + 0.8
	z := uint(f)
	fmt.Println(f, z)

	const pi = 3.14
	fmt.Println(pi)

    // Constant expressions perform arithmetic with
    // arbitrary precision.
    const (
		n = 500005151356.19432
		d = 3.15e229 / n
	)
    fmt.Printf("Type: %T, Value: %v\n", d, d)

	const (
		// Create a huge number by shifting a 1 bit left 100 places.
		// In other words, the binary number that is 1 followed by 100 zeroes.
		big = 1 << 100
		// Shift it right 100 places, so we end up with 1 again.
		small = big >> 100
	)

	//fmt.Println(int(big))
	fmt.Println(int(small))
	fmt.Println(float64(big))
	fmt.Println(float64(small))
}
