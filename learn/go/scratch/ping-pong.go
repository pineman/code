package main

import (
	"time"

	"golang.org/x/text/message"
)

const TIME = 10

type Ball struct {
	hits [2]int
}

func pingpong() {
	p := message.NewPrinter(message.MatchLanguage("en"))

	table := make(chan *Ball)
	go player(table, 0)
	go player(table, 1)

	table <- new(Ball)
	time.Sleep(TIME * time.Second)

	ball := <-table
	total := 0
	for i, v := range ball.hits {
		p.Printf("goroutine %d has %d hits\n", i, v)
		total += v
	}
	p.Println(total, "total pings")
	p.Println(total/TIME, "pings per second")
}

func player(table chan *Ball, id int) {
	for {
		ball := <-table
		ball.hits[id]++
		table <- ball
	}
}
