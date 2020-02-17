def call_counter(func):
   calls = 0
   def wrapper(*args, **kwargs):
       nonlocal calls
       calls += 1
       print('call %s to %s' % (calls, func.__name__))
       return func(*args, **kwargs)
   return wrapper


@call_counter
def string_function(str):
   print("Hello "+ str)

string_function("Kirill")
string_function("Oleg")
string_function("Artem")

