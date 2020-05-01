package main

import (
	"time"

	"golang.org/x/sys/cpu"
	"golang.org/x/text/message"
)

type ballPad struct {
	hitsA int
	_pad  cpu.CacheLinePad
	hitsB int
}

func pingpongpad() {
	p := message.NewPrinter(message.MatchLanguage("en"))

	table := make(chan *ballPad)
	go playerPad(table, 0)
	go playerPad(table, 1)

	table <- new(ballPad)
	time.Sleep(10 * time.Second)

	ball := <-table
	total := ball.hitsA + ball.hitsB
	p.Println(total, "total pings")
	p.Println(total/10, "pings per second")
}

func playerPad(table chan *ballPad, id int) {
	for {
		ball := <-table
		if id == 0 {
			ball.hitsA++
		} else {
			ball.hitsB++
		}
		table <- ball
	}
}
