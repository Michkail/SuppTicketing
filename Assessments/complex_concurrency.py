import asyncio
import concurrent.futures


def blocking_io():
    with open('test.txt', 'w') as f:
        for i in range(10000):
            f.write('test')

    return 'IO task completed successfully'


async def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(executor, blocking_io)
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
