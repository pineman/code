// https://boards.4channel.org/g/thread/90054330#p90054330
package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
	"strconv"
)

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Sum() int {
	sum := 0
	for _, v := range *h {
		sum += v
	}
	return sum
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func heap_main() {
	f, err := os.Open("../../input/1/input")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	currentCalories := 0

	h := make(IntHeap, 0)
	heap.Init(&h)

	for scanner.Scan() {
		if scanner.Text() == "" {
			heap.Push(&h, currentCalories)
			if h.Len() > 3 {
				heap.Pop(&h)
			}
			currentCalories = 0
			continue
		}

		calories, _ := strconv.Atoi(scanner.Text())
		currentCalories += calories
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(h.Sum())
}
