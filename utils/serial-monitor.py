import serial
import time

a = serial.Serial('/dev/ttyUSB0', 1000000)
while True:
    b = time.perf_counter()
    print(a.read(int(1000000/8)))
    print("{} B/s".format(1000000/8/(time.perf_counter() - b)))
