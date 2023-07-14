import asyncio

async def process_stream(stream):
    async for data in stream:
        # process data

async def main():
    streams = [open(f'file_{i}.txt', 'r') for i in range(10)]
    tasks = [asyncio.create_task(process_stream(stream)) for stream in streams]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())