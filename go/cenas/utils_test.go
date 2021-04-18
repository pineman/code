package cenas

import "testing"

func TestCenas(t *testing.T) {
	a := Cenas()
	if a == 2 {
		t.Fatalf("o teste cenas falhou")
	}
}
