package main

import (
	"testing"
)

func BenchmarkPingPong(b *testing.B) {
	pingpong()
}

func BenchmarkPingPongPad(b *testing.B) {
	pingpongpad()
}
