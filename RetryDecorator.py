import  requests
import random
def decorator_maker(attempts):
    def decorator_req(func):
        sent_requests = 0
        def wrapper(list1):
            nonlocal sent_requests
            for i in range(attempts):
                if func(list1)!= 200:
                    sent_requests +=1
                else:
                    return "Все ок 200 код"
            return "Не ок! не 200!"

        sent_requests = 0
        return wrapper
    return decorator_req


codes =[200,300,403,404,500]


@decorator_maker(3)
def request_sender(codes):
    random_code = random.choice(codes)
    return requests.get("https://httpbin.org/status/"+str(random_code)).status_code


print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))
print(request_sender(codes))