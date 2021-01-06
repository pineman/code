import os
from PIL import Image


def write_to_file(data: bytes, out_filename: str = "data.bin") -> None:
    with open(out_filename, "wb") as f:
        f.write(data)


def encode(data: bytes, out_filename: str = "data.png") -> bytes:
    assert len(data) % 3 == 0
    img = Image.frombuffer("RGB", (len(data) // 3, 1), data)
    img.save(out_filename)


def decode(in_filename="data.png") -> bytes:
    img = Image.open(in_filename)
    pixels = list(img.getdata())
    d = bytearray()
    for p in pixels:
        d.extend([p[0], p[1], p[2]])
    return bytes(d)


#a = os.urandom(100 * (2 ** 20 - 1))
a = os.urandom(90)
write_to_file(a)
encode(a)
b = decode()
assert a == b
