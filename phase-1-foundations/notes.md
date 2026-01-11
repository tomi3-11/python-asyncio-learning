# Notes on Asynchronous
def: This is the way of running functions together without waiting on each other, when a function needs waiting then you explicitely `await` it as others run.
### Difference between synchronous and asynchronous

### Synchronous
- Code runs line by line
- Each step must finish before the next starts
- Waiting blocks everthing

### Asynchronous
- Code can pause during waiting
- Other tasks can run meanwhile
- Efficient for I/O-heavy programs

### Hands on Example
`async_vs_sync.py`
```python
import time
import asyncio

def sync_task():
    print("Sync start")
    time.sleep(2)
    print("Sync stop")


def async_task():
    print("Async start")
    await asyncio.sleep(2)
    print("Async end")

sync_task()
asyncio.run(async_task())

```
