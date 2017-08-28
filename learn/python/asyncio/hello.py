import asyncio
loop = asyncio.get_event_loop()

async def hello():
    print('Hello')
    # This function must wait for this thing to complete, so,
    # return control to the event loop to allow other stuff to run while
    # this funtion waits.
    # This would be IO or anything that naturally takes time
    await asyncio.sleep(3)
    print('World!')

if __name__ == '__main__':
    loop.run_until_complete(hello())
