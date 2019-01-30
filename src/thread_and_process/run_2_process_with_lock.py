import time
import multiprocessing


def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        #balance.value += 1 =>Unpredictable output without lock
        lock.acquire(); balance.value += 1; lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        #balance.value -= 1 =>Unpredictable output without lock
        lock.acquire(); balance.value -= 1; lock.release()

def main():
    openingBalance = 150

    balance = multiprocessing.Value("i", openingBalance)
    #Queue = multiprocessing.Queue() => Multiprocessing supports Queue
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw,args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)


if __name__ == "__main__":
    main()



