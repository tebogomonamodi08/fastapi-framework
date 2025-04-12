import asyncio


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


asyncio.run(main())