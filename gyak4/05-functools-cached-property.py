import functools
from contextlib import contextmanager
import time


@contextmanager
def timed():
    start_time = time.time()
    yield
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))


# def factorial(n):
#     return n * factorial(n - 1) if n else 1

def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


class SzamStatisztika:

    def __init__(self, szam):
        self.szam = szam

    def jegyek_szama(self):
        return len(str(self.szam))

    @functools.cached_property
    # @property
    def faktorialis(self):
        return factorial(self.szam)


if __name__ == '__main__':
    szam1 = SzamStatisztika(30)
    print(szam1.faktorialis)

    with timed():
        szam2 = SzamStatisztika(80000)
        szam2.faktorialis
        szam2.faktorialis
