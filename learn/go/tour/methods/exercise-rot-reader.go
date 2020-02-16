package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func Rot13(v int, b int) int {
	d := 26 // Count of letters from a to z (or A to Z)
	return (v-b+13)%d + b
}

func (r rot13Reader) Read(b []byte) (int, error) {
	buf := make([]byte, 1)
	i := 0
	for i = range b {
		_, err := r.r.Read(buf)
		if err == io.EOF {
			break
		}
		v := int(buf[0])
		if v >= 'a' && v <= 'z' {
			b[i] = byte(Rot13(v, 'a'))
		} else if v >= 'A' && v <= 'Z' {
			b[i] = byte(Rot13(v, 'A'))
		} else {
			b[i] = buf[0]
		}
	}
	return i, io.EOF
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
