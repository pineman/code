/*
Exercise: Images
Remember the picture generator you wrote earlier? Let's write another one, but this time it will return an implementation of image.Image instead of a slice of data.

Define your own Image type, implement the necessary methods, and call pic.ShowImage.

Bounds should return a image.Rectangle, like image.Rect(0, 0, w, h).

ColorModel should return color.RGBAModel.

At should return a color; the value v in the last picture generator corresponds to color.RGBA{v, v, 255, 255} in this one.
*/

package main

import (
	"image"
	"image/color"

	"golang.org/x/tour/pic"
)

type Image struct {
	x, y int
}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, i.x, i.y)
}

func (i Image) At(x, y int) color.Color {
	b := uint8(x + y)
	return color.RGBA{b, b, 255, 255} // This struct implements color.Color
}

func main() {
	m := Image{255, 255}
	pic.ShowImage(m)
}
