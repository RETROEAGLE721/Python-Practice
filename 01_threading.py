import threading
import time

start_time = time.time()
def thread_01():
    print("This is from thread 1 befor timeout")
    time.sleep(2)
    print("This is from thread 1 after timeout")

def thread_02():
    print("This is from thread 2 befor timeout")
    time.sleep(2)
    print("This is from thread 2 after timeout")
    
thread_01 = threading.Thread(target=thread_01,daemon=True)
thread_02 = threading.Thread(target=thread_02,daemon=True)
print("This is from Main thread")
thread_01.start()
print("This is from Main thread After starting thread 1")
thread_02.start()
print("This is from Main thread After starting thread 2")
thread_01.join()
print("Thread 1 stoped ")
thread_02.join()
print("Thread 2 stoped ")
print(time.time() - start_time)