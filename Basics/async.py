import asyncio, aiohttp


async def fetch_data(url: str, retries: int):
    log = {}
    count = 1
    
    for n in range(retries+1):
        timeout = aiohttp.ClientTimeout(total=count)
        print('fetching data...')
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=timeout) as response:
                    log[n]={f'status from attempt {n}': response.status}
                    response.raise_for_status()
        except aiohttp.ClientError as e:
            print(e)
            log[n] = {'error': e}
        else:
            print('Successful')
            log[n] = {'Success': f'Try Number {n}'}
        count += 1
    return log


async def main():
   results =  await fetch_data('https://wikipedia', 3)
   print(results)

    

asyncio.run(main())
