import threading
import time

# Threads are best for IO tasks.
# multiple threads lives in a process. They share memory space using single process
# 2 threads cannot execute code simultaneously in the same python program
def thread_task(name, n):
    time.sleep(1)
    print("In ", name, sep="=>")
    for i in range(n):
        print(name,i,sep="=>")


for i in range(5):
    T = threading.Thread(target=thread_task, args=("thread"+str(i),i))
    print("starting thread",T.getName(),sep="=>")
    T.start()

time.sleep(10)
