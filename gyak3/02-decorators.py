#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


# Decorator tervezesi minta
# OOP tervezesi mintak koze tartozik
# Meglevo objektum funkcionalitasanak bovitese
# Emellett kozvetlenul nem befolyasolja a meglevo objektumot
# Annak tudta nelkul mukodik.
def first_decorator(func):
    def inner(x, y):
        print("< Before function call")
        func(x, y)
        print("< After function call")

    return inner


def first_decorator_keep_params(func):
    def inner(*args, **kwargs):
        print("< Before function call")
        func(*args, **kwargs)
        print("< After function call")

    return inner


def first_decorator_keep_params_indentity(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("< Before function call")
        func(*args, **kwargs)
        print("< After function call")

    return inner


@first_decorator
def foo(x, y):
    print("The parameters were: ", x, y)


def foo2(x, y):
    print("The parameters were: ", x, y)


# @first_decorator
@first_decorator_keep_params
def add_numbers(*args):
    """
    Adds infinite number of numbers
    :param args: the numbers
    :return: the sum of the numbers
    """
    print(sum(args))


@first_decorator_keep_params_indentity
def add_numbers2(*args):
    """
    Adds infinite number of numbers
    :param args: the numbers
    :return: the sum of the numbers
    """
    print(sum(args))

# Dekoralt funkcio meghivasa
foo("First run", 100)

# Dekoralas nelkuli funkcio meghivasa
method = foo2
method("Second run", 120)

# Kezzel alkalmazzuk a dekorator fuggvenyt
# Majd meghivjuk a dekoralt fuggvenyt
method = first_decorator(foo2)
method("Third run", 120)

add_numbers(2, 3, 4, 5)
add_numbers2(2, 3, 4, 5)

print(add_numbers.__name__)
print(add_numbers2.__name__)

print("--- Help ---")
print(help(add_numbers))

print("--- Help ---")
print(help(add_numbers2))