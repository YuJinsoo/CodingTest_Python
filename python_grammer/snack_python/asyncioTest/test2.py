import time
import asyncio

async def foo():
    res = 0

    for i in range(1, 10):
        res += i
        print(res)
        await asyncio.sleep(1)

    return res

start = time.time()
asyncio.run(asyncio.wait([foo(), foo()]))
end = time.time()
over_time = end - start
print(f'걸린 시간 : {over_time:.5f} 초')