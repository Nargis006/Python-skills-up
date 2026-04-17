import threading
import time
#implement GIL(Global Interpreter Lock) in threading it will not run parallelly instead it will context switch between them.
def prepare_chai(name):
    print(f"started {threading.current_thread().name} preparing chai")
    count = 0
    for i in range(100_000):
        count += 2  # Simulate time-consuming preparation
        # print(f"finished {threading.current_thread().name} chai for order {i}")

thread1 = threading.Thread(target=prepare_chai, args=("Masala",), name="Chai-Thread-1")

thread2 = threading.Thread(target=prepare_chai, args=("Masala",), name="Chai-Thread-2")

startTime = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

endTime = time.time()
print(f"All chai orders are ready! at time {endTime - startTime} seconds")