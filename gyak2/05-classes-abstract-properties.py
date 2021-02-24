#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc


class Drink(abc.ABC):
    def __init__(self, dl=0.0):
        self.dl = dl

    # @abc.abstractproperty
    # def price(self):
    #     """
    #     :return: price of the drink
    #     """
    #     pass

    @property
    @abc.abstractmethod
    def price(self):
        """
        :return: price of the drink
        """
        pass


class CarbonatedDrink(Drink):
    def __init__(self, dl=0.0, bubbles=100):
        super(CarbonatedDrink, self).__init__(dl)
        self.bubbles = bubbles

    def __str__(self):
        return 'CarbonatedDrink [dl=%f, bubbles=%d]' % (self.dl, self.bubbles)

    @property
    def price(self):
        return self.dl * 50 + ((100 - self.bubbles) / 5)


def main():
    sth = CarbonatedDrink(3, 100)
    print(sth)
    print(sth.price)


if __name__ == '__main__':
    main()
