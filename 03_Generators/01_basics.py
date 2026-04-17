# generators are fast it doesnot run immediatly instead it keep reference of the function. when we call next it call the finction when we call next time it resumes from where it was stopped last time.
# Yield is a keyword use for it.

def get_Chai():
    return ["cup1","cup2","cup3"]

def get_chai_generator():
    yield "cup1"
    yield "cup2"
    yield "cup3"

# it will return us value immediatly
print(f"get chai", get_Chai())

# where as generator will not return us value instead will give object reference which it points to.
cup = get_chai_generator()
print(f"get generator value", cup)

# to get value of generator we need to call next.
print(next(cup)) # return cup1
print(next(cup)) # return cup2
print(next(cup)) # return cup3
print(next(cup)) # return error StopIteration as limit has reached it has only 3 cups.

