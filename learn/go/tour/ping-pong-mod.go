package main

import (
	"fmt"
	"time"
)

type Ball struct {
	hits int
}

func main() {
	table := make(chan *Ball)
	go player("ping", table)
	go player("pong", table)
	go player("ping2", table)
	go player("pong2", table)
	go player("ping3", table)
	go player("pong3", table)
	go player("ping4", table)
	go player("pong4", table)
	go player("ping5", table)
	go player("pong5", table)
	go player("ping6", table)
	go player("pong6", table)
	go player("ping7", table)
	go player("pong7", table)
	go player("ping8", table)
	go player("pong8", table)

	table <- new(Ball) // game on; toss the ball
	time.Sleep(1 * time.Second)
	fmt.Println("main: Grabbing ball")
	<-table // game over; grab the ball
}

func player(name string, table chan *Ball) {
	for {
		fmt.Println(name, "Waiting for ball")
		ball := <-table
		fmt.Println(name, "Got ball")
		ball.hits++
		fmt.Println(name, ball.hits)
		time.Sleep(100 * time.Millisecond) // TODO: random sleep time
		fmt.Println(name, "Sending ball")
		table <- ball
	}
}
