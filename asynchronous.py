import aiohttp
import asyncio
import time
import random

async def fetch(url, session, index):
    # Introduce a random delay
    async with session.get(url) as response:
        data = await response.text()
        print(f"get response from microservice {index}")
        return data

async def asynchronous_get(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session, index) for index, url in enumerate(urls)]
        start_time = time.time()

        # Using as_completed to get results as they are available
        for future in asyncio.as_completed(tasks):
            result = await future
            print(result[:10])  # Taking the first 150 characters as an example

        end_time = time.time()
        print(f"Asynchronous total elapsed time: {end_time - start_time:.2f}s")

# Example usage
urls = [
    "https://e6156-402914.ue.r.appspot.com/static/index.html",
    "http://ec2-18-234-220-207.compute-1.amazonaws.com:8011/",
    "http://34.30.27.130:8011/",
]

# Run the async function
async def main():
    await asynchronous_get(urls)

# Python 3.7+
asyncio.run(main())
