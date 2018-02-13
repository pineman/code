import asyncio
loop = asyncio.get_event_loop()

# Generators:
# `yield` allows a function (a generator) to be resumed at the `yield`
# by calling `next(generator)` (it calls the __next__ method on it),
# returning a value and suspending execution of the generator, saving
# local state.

# TODO: implement async hello without async/await sugar
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
