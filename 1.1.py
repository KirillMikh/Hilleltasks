import time

#простая реализация
def is_prime(num):
    if num <= 2:
        print(num)
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False

    print(num)
    return True

time1=time.time()
for i in range(1_000_000):
    is_prime(i)
print('time= ',time.time()-time1)