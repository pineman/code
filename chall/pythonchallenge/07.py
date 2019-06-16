from PIL import Image
from io import BytesIO
import requests

img = Image.open((BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content)))
pix = img.load()

r = ''
for x in range(4, img.width, 7):
    r += chr(pix[x, 43][0])
print(r)

r = ''
n = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for c in n:
    r += chr(c)
print(r)