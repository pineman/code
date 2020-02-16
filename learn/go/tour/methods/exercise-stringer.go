package main

import "fmt"

type IPAddr [4]byte

func (ip IPAddr) String() (s string) {
	// TODO:
	// Hows does Sprintf convert a byte into an int?...
	// Also, what about network and host ordering?...
	return fmt.Sprintf("%d.%d.%d.%d\n", ip[0], ip[1], ip[2], ip[3])
}

func main() {
	hosts := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name, ip := range hosts {
		fmt.Printf("%v: %v\n", name, ip)
	}
}
