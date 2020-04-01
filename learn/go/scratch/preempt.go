package main

import "fmt"

func preempt() {
	done := false

	go func() {
		done = true
	}()

	for !done {
	}
	fmt.Println("done!")
}
