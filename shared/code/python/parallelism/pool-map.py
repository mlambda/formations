import multiprocessing
import time


def long_operation(a):
    time.sleep(1)
    return a ** 2


with multiprocessing.Pool() as pool:
    start = time.time()
    print(pool.map(long_operation, range(10)))
    print(f"L'appel a pris {time.time() - start:.2f}s")
