def indian_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def international_chai():
    yield "International Masala Chai"
    yield "international Chai"

def full_menu():
    yield from indian_chai() # we can import from other funtions.
    yield from international_chai()


# will list all the tea menu
# for menu in full_menu():
#     print(menu)

# if we want to pause at some level we can call next
def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
            #print(f"Preparing: {order}")
    except:
        print("Sorry! We are closed.") #The second message appears because Python automatically closes the generator at program termination, which raises a GeneratorExit exception. The bare except catches it and prints the message. Ideally we should close by ourself

stall = chai_stall()
print(next(stall))
stall.close()

