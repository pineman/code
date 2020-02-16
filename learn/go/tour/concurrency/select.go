/*
Select
The select statement lets a goroutine wait on multiple communication operations.

A select blocks until one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.
*/

package main

import "fmt"

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		// By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit locks or condition variables.
		case c <- x: // Send to channel c
			x, y = y, x+y
		case <-quit: // Receive from channel quit
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c) // Receive from channel c
		}
		quit <- 0 // Send to channel quit
	}()
	fibonacci(c, quit)
}
