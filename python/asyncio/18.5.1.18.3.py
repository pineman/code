import asyncio
import socket

# TODO: how to make this an accept() loop and bind reader() to read event?

s = socket.socket()
s.bind(('localhost', 3000))
s.listen()
rsock = s.accept()[0]
print('accepted ', rsock)

def reader():
    data = rsock.recv(100)
    print("Received:", data.decode())
    # We are done: unregister the file descriptor
    #loop.remove_reader(rsock)
    # Stop the event loop
    #loop.stop()


loop = asyncio.get_event_loop()

# Register the file descriptor for read event
loop.add_reader(rsock, reader)

# Simulate the reception of data from the network
#loop.call_soon(wsock.send, 'abc'.encode())

# Run the event loop
loop.run_forever()

# We are done, close sockets and the event loop
rsock.close()
loop.close()
