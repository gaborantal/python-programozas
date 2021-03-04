import functools

from contextlib import contextmanager
import time


# https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
@functools.lru_cache(50)
# @functools.lru_cache(None)
def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


@contextmanager
def timed():
    start_time = time.time()
    yield
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))


def main():
    with timed():
        for i in range(5000):
            factorial(3000 + (i % 50))


if __name__ == '__main__':
    main()
