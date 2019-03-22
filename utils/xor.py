from sys import argv

k = 0xca

with open(argv[1], 'rb') as i, open(argv[2], 'wb') as o:
    o.write(bytes((x ^ k for x in b''.join(i.readlines()))))
