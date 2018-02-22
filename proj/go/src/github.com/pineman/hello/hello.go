package main

import (
	"fmt"
	//"vendor_stringutil"
	"github.com/pineman/stringutil"
	//"github.com/pineman/hello/stringutil"
)

func main() {
	fmt.Printf("Hello world!\n")
	fmt.Printf(stringutil.Reverse("\nHello world!"))
}
