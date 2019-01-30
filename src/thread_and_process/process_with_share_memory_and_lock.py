import time
import multiprocessing

def timesBy(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum


def main():
    #Test time to process concurrently(
    startTime = time.time()
    p = multiprocessing.Pool() #Pool divide works among multiple cores of computer.
    result = p.map(timesBy, range(10000)) #pool.map takes a function and iterable
    p.close(); p.join(); print("Pool took:", time.time() - startTime)

if __name__ == "__main__":
    main()



