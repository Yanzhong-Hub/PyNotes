"""
Script Name Here

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time

start = time.perf_counter()


def do_something(n):
    print(f'Sleeping {n} second...')
    time.sleep(n)
    return f'Done Sleeping...{n}'


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:

        secs = [5, 4, 3, 2, 1]

        # submit method
        # results = [executor.submit(do_something, _) for _ in secs]
        #
        # for p in concurrent.futures.as_completed(results):
        #     print(p.result())

        # map method
        results = executor.map(do_something, secs)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
