# is use where continously streaming or logging is needed. Use carefully as it can drain memory.

# next()  → yield "Refill 1" → pause
# next()  → count += 1 → yield "Refill 2" → pause
# next()  → count += 1 → yield "Refill 3" → pause

def infinite_Chai():
    count = 1
    while True:
        yield f"Refill {count}" # 
        count+=1

refill_nargis = infinite_Chai()
refill_ajaz = infinite_Chai()

# usecase is it will go infinite time unless we call next so we added a condition to run it only 5 times.

# use _ instead of creating a variable if we are not going to use that it will not save in memory.
for _ in range(5):
    print(next(refill_nargis))

# benefit is it will keep a seperate track and wll run 6 times
for _ in range(6):
    print(next(refill_ajaz))