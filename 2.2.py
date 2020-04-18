import itertools
import datetime
import time
import zipfile
import string
import multiprocessing as mp
from multiprocessing import Queue
#реализация через процессы
PROCESSORS = 6
zip_file = zipfile.ZipFile("C:\\Users\\Admin\\Desktop\\lesson6.zip", 'r')


def extract_file(pswd:str):
    try:
        pswd = pswd.encode('utf8')
        zip_file.extract(r"lesson6/file_18.txt", "directory", pwd=pswd)#для пример чтобы сэкономить время вместо распаковки всего архива,
        # достаним один файл
        return True
    except:
        return False


def worker(q: Queue,wid):
    print(f'worker {wid} started ')
    while True:
        pswd = q.get()
        if pswd is None:
            break
        if extract_file(pswd):
            print('The password =  '+pswd)
    print(f'worker {wid} stopped\n ')


def generator(q: Queue):
    print('generator start')
    max_queue_size = 35
    for it in itertools.product(string.ascii_lowercase, repeat=3):
        it = str(it[0]+it[1]+it[2])
        while q.qsize() >= max_queue_size:
            time.sleep(0.000001)
        q.put(it)
    for i in range(PROCESSORS):
        q.put(None)
    print('generator exit')


if __name__ == '__main__':
    start = datetime.datetime.now()

    q = Queue()
    pr = mp.Process(target=generator, args=(q,))

    workers = []
    for i in range(PROCESSORS):
        w = mp.Process(target=worker, args=(q, i))
        w.daemon = True
        w.start()
        workers.append(w)

    pr.start()
    pr.join()

    for i in range(PROCESSORS):
        workers[i].join()

    finish = datetime.datetime.now()
    print(f'finish: {finish - start}')#на 6-ти ядрах работает 13 секунд, процессор был загружен на 100 процентов
