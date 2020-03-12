from contextlib import contextmanager
import time
@contextmanager
def foo():
    begin=time.time()
    try:
        yield "hello"
    except Exception as e:
        pass
    print(time.time()-begin)


with foo() as f1:
    time.sleep(1)