import fire


def add_simple(a, b, c):
    return a + b + c


def add_args_default(a, *args):
    return a + sum(args)


if __name__ == '__main__':
    fire.Fire({'add3': add_simple, 'add': add_args_default})
