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

import sys

if sys.version_info[:2] < (3, 3):
    import collections
    def callable(function):
        return isinstance(function, collections.Callable)

class Command:

    def __init__(self, do, undo, description=""):
        assert callable(do) and callable(undo)
        # TODO Implement me!
        self.do = do
        self.undo = undo
        self.description = description

    def __call__(self):
        # TODO Implement me!
        self.do()

class Macro:

    def __init__(self, description=""):
        self.description = description
        self.__commands = []

    def add(self, command):
        # TODO Implement me!
        if not isinstance(command, Command):
            raise TypeError("Expected object of type Command, got {}".
                            format(type(command).__name__))

    def __len__(self):
        return len(self.__commands)

    def __call__(self):
        # TODO Implement me!
        for command in self.__commands:
            command()

    do = __call__

    def undo(self):
        # TODO Implement me!
        for command in reversed(self.__commands):
            command.undo()
