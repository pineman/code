from socket import *
#s = socket(AF_UNIX, SOCK_STREAM)
#s.connect('test')
#sent = s.sendto(b'a' * 5000, 'test')

i = 0
while True:
    s = socket(AF_UNIX, SOCK_DGRAM)
    sent = s.sendto(b'a' * int(2**17 + 81888), 'server')
    print(f"{i}: sent {sent} bytes")
    i += 1
