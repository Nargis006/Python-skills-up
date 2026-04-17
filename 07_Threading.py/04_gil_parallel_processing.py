from multiprocessing import Process, current_process
import os
import time
# Implement parallel processing using multiprocessing to bypass GIL limitations in CPU-bound tasks.
def prepare_chai():
    print(f"started {current_process().name} preparing chai")
    count = 0
    for i in range(100_000):
        count += 2  # Simulate time-consuming preparation
        # print(f"finished {current_process().name} chai for order {i}")

if __name__ == "__main__":
    p1 = Process(target=prepare_chai, name=f"Chai-Maker-1")
    p2 = Process(target=prepare_chai, name=f"Chai-Maker-2")

    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    endTime = time.time()
    print(f"{p1.name} with PID: {p1.pid} finished at time {endTime - start_time} seconds")