import time
import multiprocessing

# Processes speed up Python operations that are CPU intensive because they benefit from multiple cores
# Processes can have multiple threads and can execute code simultaneously in the same python program
def cal_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square of",n, "is", n*n, sep=" ")

def cal_cube(numbers):
    for n in numbers:
        time.sleep(1)
        print("cube of ", n, "is", n*n*n, sep=" ")


if __name__ == "__main__":
    arr = [2,3,6,9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    p2 = multiprocessing.Process(target=cal_cube, args=(arr,))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done")



