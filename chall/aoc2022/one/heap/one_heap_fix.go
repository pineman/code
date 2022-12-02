// Don't pop if len > 3, instead push n times and pop 3 times, using a MaxHeap instead of MinHeap.
// Confusing to implement a Sum() method when it's not required by the interface
package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
	"strconv"
)

type MaxHeap []int

func (h MaxHeap) Len() int {
	return len(h)
}

func (h MaxHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func heap_fix_main() {
	f, err := os.Open("../../input/1/input")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	currentCalories := 0

	h := make(MaxHeap, 0)
	heap.Init(&h)

	for scanner.Scan() {
		if scanner.Text() == "" {
			heap.Push(&h, currentCalories)
			currentCalories = 0
			continue
		}

		calories, _ := strconv.Atoi(scanner.Text())
		currentCalories += calories
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(heap.Pop(&h).(int) + heap.Pop(&h).(int) + heap.Pop(&h).(int))
}
