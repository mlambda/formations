import threading
import time


def long_operation(a):
    time.sleep(1)
    print(a ** 2)


if __name__ == "__main__":
    threads = [threading.Thread(target=long_operation, args=(i,))
               for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
