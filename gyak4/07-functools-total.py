import functools


@functools.total_ordering
class Teglalap:
    def __init__(self, a, b=0):
        self.a = a
        self.b = (b if b > 0 else a)

    def terulet(self):
        return self.a * self.b

    def kerulet(self):
        return 2 * self.a + 2 * self.b

    def __eq__(self, other):
        if isinstance(other, Teglalap):
            return self.terulet() == other.terulet()
        return False

    def __lt__(self, other):
        if isinstance(other, Teglalap):
            return self.terulet() < other.terulet()
        return False


if __name__ == '__main__':
    t1 = Teglalap(6, 5)
    print(t1.terulet())
    print(t1.kerulet())

    t2 = Teglalap(5, 6)
    t3 = Teglalap(3, 10)
    print("---")

    print(t1 == t2)
    print(t1 < t2)
    print(t1 <= t2)
    print(t1 > t2)
    print(t1 >= t2)
    print(t1 != t2)
    print("---")

    print(t1 == t3)
    print(t1 < t3)
    print(t1 <= t3)
    print(t1 > t3)
    print(t1 >= t3)
    print(t1 != t3)
    print("---")

    t4 = Teglalap(8)
    print(t2 > t4)
    print(t2 <= t4)
