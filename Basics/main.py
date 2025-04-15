'''
            Write an async function that:
-Fetches from https://httpbin.org/delay/3 (delays for 3 sec).
-Sets a timeout to 2 sec.
-Gracefully handles the timeout and prints "Timeout occurred" when it happens.
'''
import asyncio, aiohttp

async def fetch_data(url: str, delay : int):
    '''This function takes input: url-> str and delay: int
        and returns data from the request'''
    timeout = aiohttp.ClientTimeout(total=delay)
    try:
        async with aiohttp.ClientSession(timeout = timeout) as session:
            async with session.get(url) as response:
                data = (await response.text())[:30]
                print(data)
                return data
    except (asyncio.TimeoutError, aiohttp.ClientError):
        print('Timeout Occured.')
    except Exception as e:
        print(e)
    


async def main():
    url = 'https://httpbin.org/delay/'
    print(f'fetching data from {url}...')
    await fetch_data(url+'3',delay=2)
    print('Connection Terminated.')

asyncio.run(main())

            
