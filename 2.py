import asyncio
import itertools
import datetime
import zipfile
import string
from asyncio import Queue

TCOUNT = 6
zip_file = zipfile.ZipFile("C:\\Users\\Admin\\Desktop\\lesson6.zip", 'r')

async def extract_file(pswd:str):
   try:
       pswd=pswd.encode('utf8')
       zip_file.extract(r"lesson6/file_18.txt", "directory", pwd=pswd)#для пример чтобы сэкономить время вместо распаковки всего архива, достаним один файл
       return True
   except:
       return False

async def worker(q: Queue,wid):
    print(f'worker {wid} started ')
    while True:
        pswd = await q.get()
        if pswd is None:
            break
        if await extract_file(pswd):
            print('The password =  '+pswd)
    print(f'worker {wid} stopped\n ')


async def generator(q: Queue):
    print('generator start')
    max_queue_size = 35
    for it in itertools.product(string.ascii_lowercase, repeat=3):
        it=str(it[0]+it[1]+it[2])
        while q.qsize() >= max_queue_size:
            await asyncio.sleep(0)
        await q.put(it)
    for i in range(TCOUNT):
        await q.put(None)
    print('generator exit')


start = datetime.datetime.now()

q = Queue()
loop1 = asyncio.get_event_loop()
tasks = asyncio.gather(generator(q), *[worker(q, i) for i in range(TCOUNT)])
print(tasks)
loop1.run_until_complete(tasks)
finish = datetime.datetime.now() - start
print(finish)#с 6 потоками асинхронно  работает примерно 50 секунд