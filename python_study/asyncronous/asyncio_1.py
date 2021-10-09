from time import time
from urllib.request import Request, urlopen
import asyncio

urls = ['https://www.google.co.kr/search?q=' +
        i for i in ['apple', 'pear', 'grape', 'pineapple', 'banana', 'orange']]


async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)


async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]

    result = await asyncio.gather(*futures)
    print(result)

begin = time()
"""syncronous
result = list()
for url in urls:
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

end = time()
print(f'run time: {end - begin:.3f}')
