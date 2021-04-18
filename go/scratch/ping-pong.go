package main

import (
	"time"

	"golang.org/x/text/message"
)

type ball struct {
	hits [2]int
}

func pingpong() {
	p := message.NewPrinter(message.MatchLanguage("en"))

	table := make(chan *ball)
	go player(table, 0)
	go player(table, 1)

	table <- new(ball)
	time.Sleep(10 * time.Second)

	ball := <-table
	total := ball.hits[0] + ball.hits[1]
	p.Println(total, "total pings")
	p.Println(total/10, "pings per second")
}

func player(table chan *ball, id int) {
	for {
		ball := <-table
		// TODO
		// The two goroutines never increment at the same time, as they're
		// synchronized by the `table` channel.
		// But they could be running in two different CPUs at the same time,
		// right? So an increment of goroutine 0 could cause a cache line
		// eviction of the CPU where goroutine 1 is running (when it runs again
		// and increments). So how is this not false sharing?
		// I did an experiment with padding between the two `hit` variables
		// and it didn't change anything.
		// This assumes the two goroutines running on different CPUs is likely.
		// Maybe it isn't, and that assumption is not true for whatever
		// scheduling linux does.
		ball.hits[id]++
		table <- ball
	}
}
