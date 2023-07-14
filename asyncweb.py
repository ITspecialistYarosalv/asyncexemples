import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://www.youtube.com', 'https://www.google.com']
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    result =await asyncio.gather(*tasks)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())