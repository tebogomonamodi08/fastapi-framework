
import asyncio
"""

async def task(t : int, n: int):
    '''definition of a asynchronous function that take parameter t as time and n as the task number and yields
    control to the event loop after the first line'''
    print('Download...')
    await asyncio.sleep(t)
    print(f'Downloading task {n} Complete')

async def main():
    '''The entry point of the event loop we will gather the tasks in here and await them
    to complete'''
    task_1 = task(4,1)
    task_2 = task(2,2)
    await asyncio.gather(task_1,task_2)


asyncio.run(main())"""

async def task(t : float, n : int):
    '''This is a asynchronous function that simulates fetching data'''
    print('Fetching data...')
    await asyncio.sleep(t) #simulate the time in t seconds
    if n==2:
        raise ValueError('Eish')
    return f'Data from task {n}' #return this when the wait is finished

async def main():
    task_1 = task(4,1)
    task_2 = task(5,2)
    task_3 = task(3, 3)

    results = await asyncio.gather(task_1,task_2,task_3, return_exceptions=True)
    print(results)


asyncio.run(main())