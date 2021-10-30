import asyncio
import time
import threading



async def main():
    print('Hello ...')
    # await asyncio.sleep(5)
    time.sleep(10)
    print('... World!')

print('a')
x = threading.Thread(target=main)
x.start()
# asyncio.ensure_future(main())
# a = await main
print('b')