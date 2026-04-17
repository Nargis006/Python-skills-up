def chai_customer():
    print(f"enter the type of chai you want!")
    order = yield # it will wait for the user to send input if user has not enter anything this line of code will not execute will pause and wait.

    while True:
        print(f"Preparing: {order}") # preparing: Masala Chai
        order = yield # pause here again if we give send it will run if we comment it it will never pause and become infinite loop.

chai_order_stall = chai_customer()
next(chai_order_stall)

chai_order_stall.send("Masala Chai")
chai_order_stall.send("Leamon Tea")