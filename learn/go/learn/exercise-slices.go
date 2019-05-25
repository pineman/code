package main

import (
	"bytes"
	"image"
	"image/png"
	"os"
)

func Show(f func(int, int) [][]uint8) {
	const (
		dx = 256
		dy = 256
	)
	data := f(dx, dy)
	m := image.NewNRGBA(image.Rect(0, 0, dx, dy))
	for y := 0; y < dy; y++ {
		for x := 0; x < dx; x++ {
			v := data[y][x]
			i := y*m.Stride + x*4
			m.Pix[i] = v
			m.Pix[i+1] = v
			m.Pix[i+2] = 255
			m.Pix[i+3] = 255
		}
	}
	WriteImageToPng(m)
}

func WriteImageToPng(m image.Image) {
	var buf bytes.Buffer
	err := png.Encode(&buf, m)
	if err != nil {
		panic(err)
	}
	//enc := base64.StdEncoding.EncodeToString(buf.Bytes())
	//fmt.Println(enc)
	f, err := os.Create("test.png")
	if err != nil {
		panic(err)
	}
	buf.WriteTo(f)
}

func Pic(dx, dy int) [][]uint8 {
	pic := make([][]uint8, dy, dy)
	for i := range pic {
		pic[i] = make([]uint8, dx, dx)
	}

	for i := range pic {
		for j := range pic[i] {
			//pic[i][j] = uint8(j)
			//pic[i][j] = uint8(j)
			//pic[i][j] = uint8(i + j)
			pic[i][j] = uint8((i + j) / 2)
			//pic[i][j] = uint8(i * j)
		}
	}

	return pic
}

func main() {
	Show(Pic)
}
