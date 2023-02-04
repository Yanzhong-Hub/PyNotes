"""
Example

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import multiprocessing
import time


def do_something(n):
    print(f'Sleeping {n} second...')
    time.sleep(n)
    print('Done Sleeping...')


if __name__ == '__main__':
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        # create the process
        p = multiprocessing.Process(target=do_something, args=(3, ))
        processes.append(p)

        # start the process
        p.start()

    # make program wait until the process finish
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} seconds')
