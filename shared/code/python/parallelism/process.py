import multiprocessing
import time


def long_operation(a):
    time.sleep(1)
    print(a ** 2)


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=long_operation, args=(i,))
        for i in range(10)
    ]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
