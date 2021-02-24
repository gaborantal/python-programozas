def add_simple(a, b, c):
    return a + b + c


# def add_simple(a: int, b: int, c: int) -> int:
#     return a + b + c

def add_list(simple_list):
    return sum(simple_list)


# def add_list(simple_list: list) -> int:
#     return sum(simple_list)

def add_args_default(a, b=0, c=0):
    return a + b + c


def add_args(*args):
    print("type:", type(args))
    return sum(args)


def card(**data):
    print("type:", type(data))

    for key, value in data.items():
        # print("{} is {}".format(key, value))
        print(f"{key.title()}: {value}")


def card_args_kwargs(*args, **data):
    print("type1:", type(args))
    print("type2:", type(data))

    for key, value in data.items():
        # print("{} is {}".format(key, value))
        print(f"{key.title()}: {value}")

def set_object(refresh_time, timeout, **kwargs):
    #  beallitunk minden
    if kwargs.get("alma"):
        print("alma volt benne")

if __name__ == '__main__':
    print("Simple add")
    print(add_simple(1, 2, 4))
    print(add_simple(1, 2.5, 4))

    print("Add (list)")
    # print(add_list(1))
    print(add_list([1, 2, 3]))

    print("Add (simple, default)")
    print(add_args_default(1))
    print(add_args_default(1, 2))
    print(add_args_default(1, 2, 3))

    print("Add (*args)")
    print(add_args(1, 2, 3, 4, 5))
    # print(add_args(1, 2, 3, 4, 56, 6, 7, 8, nyolcadik=12))

    card(name="John Rambo", phone="+0036705554433", address="N/A", email="info@rambo.com")

    print(sum("asd", "asd"))
