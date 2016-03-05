#!/usr/bin/env python3
# Copyright 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# This program has been modified from its original source
# (stationery1, stationery2.py) to fit in Advanced Programming 2016 
# week 4 exercise.

import abc
import functools
import itertools
import sys

def logged(function):
    # TODO Implement me!
    pass

def do_log(Class):
    # TODO Implement me!
    # Hint: `inspect` module might be useful in implementing this
    # class decorator
    pass

def main():
    pencil = Item.create("Pencil", 0.40)
    ruler = Item.create("Ruler", 1.60)
    eraser = make_item("Eraser", 0.20)
    pencilSet = Item.compose("Pencil Set", pencil, ruler, eraser)
    box = Item.create("Box", 1.00)
    boxedPencilSet = make_composite("Boxed Pencil Set", box, 
            pencilSet)
    boxedPencilSet.add(pencil)
    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print()


class AbstractItem(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def composite(self):
        pass

    def __iter__(self):
        return iter([])


class SimpleItem(AbstractItem):

    def __init__(self, name, price=0.00):
        self.name = name
        self.price = price

    @property
    def composite(self):
        # TODO Implement me!
        return False

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name), 
            file=file)


class AbstractCompositeItem(AbstractItem):

    def __init__(self, *items):
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        # TODO Implement me!
        pass

    def remove(self, item):
        # TODO Implement me!
        pass

    def __iter__(self):
        return iter(self.children)


class CompositeItem(AbstractCompositeItem):

    def __init__(self, name, *items):
        super().__init__(*items)
        self.name = name

    @property
    def composite(self):
        # TODO Implement me!
        pass
    
    @property
    def price(self):
        return sum(item.price for item in self)

    def print(self, indent="", file=sys.stdout):
        print("{}${:.sf} {}".format(indent, self.price, self.name), 
                file=file)
        for child in self:
            # Passed the file parameter to child.print() calls
            # in order to make print() more properly testable
            child.print(indent + "      ", file)


class Item:
# TODO Add do_log class decorator!

    def __init__(self, name, *items, price=0.00):
        self.name = name
        self.price = price
        self.children = []
        if items:
            self.add(*items)

    @classmethod
    def create(Class, name, price):
        # TODO Implement me!
        pass

    @classmethod
    def compose(Class, name, *items):
        # TODO Implement me!
        pass

    @property
    def composite(self):
        # TODO Implement me!
        pass

    def add(self, first, *items):
        # TODO Implement me!
        pass

    def remove(self, item):
        # TODO Implement me!
        pass

    def __iter__(self):
        return iter(self.children)

    @property
    def price(self):
        # TODO Implement me!
        pass

    @price.setter
    def price(self, price):
        # TODO Implement me!
        pass

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name),
                file=file)
        for child in self:
            # Passed the file parameter to child.print() calls
            # in order to make print() more properly testable
            child.print(indent + "      ", file=file)

    def __repr__(self):
        return "{}:${}".format(self.name, self.price)


def make_item(name, price):
    # TODO Add logged function decorator!
    return Item(name, price=price)

def make_composite(name, *items):
    # TODO Add logged function decorator!
    return Item(name, *items)

if __name__ == "__main__":
    main()
