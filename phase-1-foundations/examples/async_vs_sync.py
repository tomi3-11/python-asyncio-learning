import time
import asyncio


def sync_task():
    '''Handles the synchronous behaviour of the function'''
    print('Sync start')
    time.sleep(2)
    print('Sync end')


async def async_task():
    '''Handles the asynchronous behaviour of the function'''
    print("Async Start")
    await asyncio.sleep(2)
    print("Async Stop")


sync_task()
asyncio.run(async_task())

