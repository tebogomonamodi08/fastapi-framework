import asyncio, aiohttp, time


async def get(url : str, connection_number : int):
    log = {}
    start = time.time()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                data = (await response.text())[:30]
                response.raise_for_status()
    except aiohttp.ClientConnectionError as e:
        log[connection_number] = {'error' : e}
    except asyncio.TimeoutError as e:
        log[connection_number] = {'error': e}
    else:
        print(data)
    finally:
        end = time.time()
        duration = end - start
        log[connection_number] = {'Duration': duration,
                                  'Success': 'Yes!!!'
                                  }
        print(log)
    
async def main():
    session_1 = get('https://httpbin.org/delay/1', 1)
    session_2 = get('https://httpbin.org/delay/2', 2)
    session_3 = get('https://httpbin.org/delay/3', 3)
    await asyncio.gather(session_1,session_2,session_3)

asyncio.run(main())



