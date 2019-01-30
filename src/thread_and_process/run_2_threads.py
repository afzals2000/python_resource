import threading
import time

arr = [2,3,6,9]

def cal_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square of",n, "is", n*n, sep=" ")

def cal_cube(numbers):
    for n in numbers:
        time.sleep(1)
        print("cube of ", n, "is", n*n*n, sep=" ")

# Threads are best for IO tasks.
# multiple threads lives in a process. They share memory space using single process
# 2 threads cannot execute code simultaneously in the same python program
t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()  #join the main Thread to finish. Can add t2 so will wait for t2 to finish
t2.join()

print("done")