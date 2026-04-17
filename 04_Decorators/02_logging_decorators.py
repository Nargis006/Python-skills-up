from functools import wraps

def log_activity(func):
    @wraps(func)
    # * takes unknown number of parameters and we dont know the order. internally its tupil. eg func which we are calling can take 2 arg 3 or any number of arguments this wrapper will not break. Collects positional arguments into a tuple
    # ** Collects keyword arguments into a dictionary when we pass func(name = 'nargis', age= 30) // can be any it will be last in order.
    def wrapper(*args, **kwargs):
        print(f"🚀 Clling: {func.__name__}")
        result = func(*args, **kwargs)
        print("✅ Successfully called and got response")
        print(result)
    return wrapper

@log_activity
def brewCoffee(type, milk="no", canCustamize = False):
    print(f"Cofee brewing started! selected {type} with {milk} Milk. Can we Customize? {canCustamize}")
    return True

brewCoffee("GingerTea", "Mild")
brewCoffee("international", "NO",True)