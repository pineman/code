package main

import "fmt"

type I interface {
	M()
}

func main() {
	var i_empty interface{}
	var i_nil I
	describe(i_empty)
	describe(i_nil)
	i_nil.M()
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
