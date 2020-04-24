import time
import threading
import datetime
from urllib3.exceptions import ConnectTimeoutError
import requests
import queue


site = 'http://httpbin.org'
max_running = 100
q_size = 50

def worker(q):
    while True:
        proxy = q.get()
        proxy = {'http': proxy}
        if proxy is None:
            break
        try:
            r = requests.Session().get(site, timeout=1, proxies=proxy)
            print("{0}\n".format(r.status_code))

        except (ConnectTimeoutError,
                ConnectionResetError,
                ConnectionAbortedError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ProxyError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.TooManyRedirects,
                requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError) as e:

            print(" {0} \n".format(e), end="")


def generator(q):
    file_proxy = open("C:\\Users\\Admin\\Desktop\\proxies.txt", 'r')#прокси с того сайта что был в примере
    line = file_proxy.readline()
    while line:
        while q.qsize() > q_size:
            time.sleep(0.00001)
        proxy = line.strip()
        q.put( 'http://{0}'.format(proxy))
        line = file_proxy.readline()
    file_proxy.close()
    for i in range(max_running):
        q.put(None)


start = datetime.datetime.now()

q1 = queue.Queue()
q_thread = threading.Thread(target=generator, args=(q1,))
q_thread.start()


workers = []
for i in range(max_running):
    w = threading.Thread(target=worker, args=(q1,))
    w.start()
    workers.append(w)
q_thread.join()

for i in workers:
    i.join()
finish = datetime.datetime.now()
print(f'finish: {finish - start}')

