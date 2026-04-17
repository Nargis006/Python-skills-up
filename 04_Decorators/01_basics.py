from functools import wraps 

# decorators are wrappers around and existing functions when we want to perform anything before or after existing function call we can use it. We can pass params to it.

def my_decorator(func):
    @wraps(func) # it will persist metadata of calling function.
    def wrapper():
        print("Print sum of 2+2")
        sum = func()
        print(f"return sum of 2+2: {sum}")
    return wrapper

@my_decorator
def calculate_Sum():
    print("return sum to decorator")
    return 2+2

calculate_Sum()
print(calculate_Sum.__name__) # name gets overridden when we call via decorators to keep metadata of function we use an package called wrapper
