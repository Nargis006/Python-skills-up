from multiprocessing import Process, current_process
import time

def brew_chai(order_name):
    print(f"{current_process().name} started brewing {order_name} chai.")
    time.sleep(3)  # Simulate time-consuming brewing process
    # print(f"{current_process().name} finished brewing {order_name} chai.")

# if file runs directly then only run this code python multiprocessing.py then __name__ == "__main__": 
# if we import this file in another file then __name__ will be equal to file name not __main__ so this code will not run. eg import app then __name__ == "app"
if __name__ == "__main__":
    chai_makers = [
    Process(target=brew_chai, args=("Masala",), name=f"Chai-Maker-{i}") 
    for i in range(3)]

# start all processes it starts the process processing for each chai maker in parallel.
    for maker in chai_makers:
        maker.start()
    
    # wait for all processes to finish
    for maker in chai_makers:
        maker.join()
    
    print("All chai orders are ready!")