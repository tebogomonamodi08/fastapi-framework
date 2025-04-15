import asyncio, aiohttp #import the asynchronous library to create coroutine and import aiohttp to make seperate request


async def get(url : str):
    '''This function takes a url as input and send a get request to the url
    in a seperate session(tab) in browser terms'''
    print('Starting Session')
    try:
        async with aiohttp.ClientSession as session: #This class create a object that will send http requests from
            async with session.get(url) as response: #Twe create a response object for the session above
                print(response.status) #print the status of the rsponse object
                response.raise_for_status() #raise an exception for errors that are not 200

    except aiohttp.ClientConnectionError() as e:
        print(e)
    
    finally:
        print('Session Completed')
    

async def main():
    task_1 = get('https://wikipeadia.com') #create future objects
    task_2 = get('https://youtube.com')
    task_3 = get('https://he.there.xo')

    await asyncio.gather(task_1,task_2,task_3) #load futures into the event loop and wait for the output from the eventloop

asyncio.run(main()) #start the main loop