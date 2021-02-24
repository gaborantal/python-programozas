class A:
    def __init__(self):
        print('A')
        super().__init__()


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()


class X:
    def __init__(self):
        print('X')
        super().__init__()


class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()


class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()
        # X.__init__(self)
        # B.__init__(self)


if __name__ == '__main__':
    print(A.__mro__)
    print(B.__mro__)
    print(X.__mro__)
    print(Forward.__mro__)
    print(Backward.__mro__)

    # print("Create Backward")
    # Backward()
    # print()
    # print("Create Forward")
    # Forward()

    print(D.__mro__)
