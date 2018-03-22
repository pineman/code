import serial
import time

a = serial.Serial('/dev/ttyACM1', 1000000)
while True:
    b = time.perf_counter()
    print(a.read())
