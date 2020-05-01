package main

import (
	"fmt"
	"time"
)

var c chan int

func handle(int) {}

func after() {
	time.AfterFunc(time.Second, func() { fmt.Println("afterfunc"); time.Sleep(1000) })
	select {
	case m := <-c:
		handle(m)
	case <-time.After(2 * time.Second):
		fmt.Println("timed out")
	}
}
