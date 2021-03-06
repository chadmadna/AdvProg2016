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
from inspect import getmembers, ismethod

def logged(function):
    # TODO Implement me!
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        comma = ', ' if kwargs else ''
        print("You called {}({}{}{})".format(function.__name__,
                                              str(args).strip('()'), comma,
                                              str(kwargs).strip('{}')))
        ret = function(*args, **kwargs)
        print("It returned {}".format(ret))
        return ret
    return wrapper

def do_log(Class):
    # TODO Implement me!
    # Hint: `inspect` module might be useful in implementing this
    # class decorator
    class_methods = getmembers(Class, predicate=ismethod)
    for name, method in class_methods:
        setattr(Class, name, logged(method))
    return Class

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
        self.children.append(first)
        if items:
            self.children.extend(items)

    def remove(self, item):
        # TODO Implement me!
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)


class CompositeItem(AbstractCompositeItem):

    def __init__(self, name, *items):
        super().__init__(*items)
        self.name = name

    @property
    def composite(self):
        # TODO Implement me!
        return True
    
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


@do_log
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
        return Class(name, price=price)

    @classmethod
    def compose(Class, name, *items):
        # TODO Implement me!
        return Class(name, *items)

    @property
    def composite(self):
        # TODO Implement me!
        return bool(self.children)

    def add(self, first, *items):
        # TODO Implement me!
        self.children.extend(itertools.chain((first,), items))

    def remove(self, item):
        # TODO Implement me!
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)

    @property
    def price(self):
        # TODO Implement me!
        return (self.__price + sum(item.price for item in self) if self.children else
                self.__price)

    @price.setter
    def price(self, price):
        # TODO Implement me!
        self.__price = price

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name),
                file=file)
        for child in self:
            # Passed the file parameter to child.print() calls
            # in order to make print() more properly testable
            child.print(indent + "      ", file=file)

    def __repr__(self):
        return "{}:${}".format(self.name, self.price)


@logged
def make_item(name, price):
    # TODO Add logged function decorator!
    return Item(name, price=price)

@logged
def make_composite(name, *items):
    # TODO Add logged function decorator!
    return Item(name, *items)

if __name__ == "__main__":
    main()
