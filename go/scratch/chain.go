package main

import "fmt"

func f(left, right chan int) {
	right <- 1 + <-left
}

func chain() {
	const N = 1e6
	leftmost := make(chan int)
	left := leftmost
	right := leftmost
	for i := 0; i < N; i++ {
		right = make(chan int)
		go f(left, right)
		left = right
	}
	leftmost <- 1
	fmt.Println(<-right)
}
