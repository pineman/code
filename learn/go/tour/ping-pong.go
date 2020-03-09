package main

import (
	"fmt"
	"time"
)

const TIME = 2

type Ball struct {
	hits int
}

func main() {
	table := make(chan *Ball)
	go player("ping", table)
	go player("pong", table)

	table <- new(Ball) // game on; toss the ball
	time.Sleep(TIME * time.Second)

	ball := <-table // game over; grab the ball
	fmt.Println(ball.hits/TIME, "pings per second")
}

func player(name string, table chan *Ball) {
	for {
		ball := <-table
		ball.hits++
		//fmt.Println(name, ball.hits)
		//time.Sleep(100 * time.Millisecond)
		table <- ball
	}
}
