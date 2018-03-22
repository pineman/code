package main

import (
	"crypto/sha256"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const numWorkers int = 10

func concurrent() {
	rand.Seed(time.Now().UnixNano())
	var wg sync.WaitGroup

	wg.Add(numWorkers)
	for i := 1; i <= 10; i++ {
		go func(number int) {
			defer wg.Done()

			//var n = rand.Int() % 10000000
			var n = number * number * 100000
			fmt.Printf("this is goroutine #%02v doing %v iterations!\n", number, n)

			for j := 0; j < n; j++ {
				// Should change to some other computation!
				sha256.Sum256([]byte("ASDFASDF"))
			}

			fmt.Printf("goroutine #%02v\n", number)
		}(i)
	}
	wg.Wait()
}

// TODO
func serial() {
}

func main() {
	concurrent()
}
