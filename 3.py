import time


class MyClass:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("Время выполнения  " + str(end-self.start))


with MyClass():
    for i in range(3_000_000):
        i += 2
