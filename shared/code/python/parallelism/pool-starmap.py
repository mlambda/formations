import multiprocessing
import time


def long_operation(a, b):
    time.sleep(1)
    return a * b


with multiprocessing.Pool() as pool:
    start = time.time()
    print(pool.starmap(long_operation, zip(range(10), range(10))))
    print(f"L'appel a pris {time.time() - start:.2f}s")
