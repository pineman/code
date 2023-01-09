package main

import (
	"sync"
	"time"
	"log"
	"net/http"
	_ "net/http/pprof"
)

var (
	lock1 sync.Mutex
	lock2 sync.Mutex
)

func main() {
    // https://www.youtube.com/watch?v=9j0oQkqzhAE
    // Though I disagree with some things in the talk or they're not explained
    // adequately IMO.
	go func() {
		for {
			lock1.Lock()
			lock2.Lock()
			lock2.Unlock()
			lock1.Unlock()
		}
	}()
	go func() {
		for {
			lock2.Lock()
			lock1.Lock()
			lock1.Unlock()
			lock2.Unlock()
		}
	}()
	// Defeat the deadlock detector
	go time.Sleep(time.Minute)
	// sending SIGQUIT or CTRL-\ (backslash) produces a backtrace
	// Or use the pprof http server at /debug/pprof
	go func () {
		log.Println(http.ListenAndServe("localhost:6060", nil))
	}()
	select {}
}
