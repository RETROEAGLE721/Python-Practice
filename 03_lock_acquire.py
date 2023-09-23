import threading 
import time 
start_time = time.time()

def trying_something_1(a = 10):
    print("++++", a ,"++++",end="\n")
    time.sleep(2)
    a = a + 1
    print("****",a,"****",end="\n")


thread_1 = threading.Thread(target=trying_something_1,daemon=True)
thread_2 = threading.Thread(target=trying_something_1,daemon=True)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(time.time()-start_time)