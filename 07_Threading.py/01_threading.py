import threading
import time

def prepare_chai(name):
    for i in range(1,3):
        print(f"Preparing {name} chai for order {i}")
        # Simulate time-consuming preparation        
        time.sleep(2)
        print(f"{name} for order {i} chai is ready!")

def prepare_sandwich(name):
    for i in range(1,3):
        print(f"Preparing {name} sandwich for order {i}")
        # Simulate time-consuming preparation
        time.sleep(4)
        print(f"{name} sandwich for order {i} is ready!")

# create threads for chai and sandwich preparation it will not run parallelly its context switch between them. first chai starts then sandwich starts while chai is waiting for sleep sandwich will run and vice versa.
chai_thread = threading.Thread(target=prepare_chai, args=("Masala",))
chai_thread.start()
# create and start the threads another way to start thread
sandwitch_Thread = threading.Thread(target=prepare_sandwich, args=("Veggie",))
sandwitch_Thread.start()

chai_thread.join()  # wait for chai thread to finish
sandwitch_Thread.join()  # wait for sandwich thread to finish

print("All orders are ready!")
