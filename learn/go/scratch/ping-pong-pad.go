package main

import (
	"time"

	"golang.org/x/sys/cpu"
	"golang.org/x/text/message"
)

type BallPad struct {
	hits_a int
	_pad   cpu.CacheLinePad
	hits_b int
}

func pingpongpad() {
	p := message.NewPrinter(message.MatchLanguage("en"))

	table := make(chan *BallPad)
	go player_pad(table, 0)
	go player_pad(table, 1)

	table <- new(BallPad)
	time.Sleep(10 * time.Second)

	ball := <-table
	total := ball.hits_a + ball.hits_b
	p.Println(total, "total pings")
	p.Println(total/TIME, "pings per second")
}

func player_pad(table chan *BallPad, id int) {
	for {
		ball := <-table
		if id == 0 {
			ball.hits_a++
		} else {
			ball.hits_b++
		}
		table <- ball
	}
}
