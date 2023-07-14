import random
from time import sleep
import asyncio

def task(pid):
    """Synchronous non-deterministic task.

    """
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)

async def task_coro(pid):
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)

def synchronus():
    for i in range(1,10):
        task(i)

async def asynchronus():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1,10)]
    await asyncio.wait(tasks)

print('Synchronous:')
synchronus()

ioloop = asyncio.get_event_loop()
print('Asynchronous:')
ioloop.run_until_complete(asynchronus())

ioloop.close()