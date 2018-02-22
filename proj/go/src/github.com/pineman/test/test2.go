// https://nathanleclaire.com/blog/2014/02/15/how-to-wait-for-all-goroutines-to-finish-executing-before-continuing/
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	messages := make(chan int)
	var wg sync.WaitGroup

	// you can also add these one at
	// a time if you need to

	wg.Add(3)
	go func() {
		defer wg.Done()
		time.Sleep(time.Second * 3)
		messages <- 1
	}()
	go func() {
		defer wg.Done()
		time.Sleep(time.Second * 2)
		messages <- 2
	}()
	go func() {
		defer wg.Done()
		time.Sleep(time.Second * 1)
		messages <- 3
	}()
	go func() {
		for i := range messages {
			fmt.Println(i)
		}
	}()

	for {
		fmt.Println("here forever")
		time.Sleep(time.Second)
	}

	wg.Wait()
}
