#!/usr/bin/env python3
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# This test suite contains unit tests for testing mandatory and
# additional exercise components for week 5 exercise.

import sys
import types
import unittest
from command import Command, Macro
from unittest.mock import MagicMock

if sys.version_info[:2] < (3, 3):
    import collections
    def callable(function):
        return isinstance(function, collections.Callable)

class CommandTest(unittest.TestCase):

    def setUp(self):
        self.cmd1 = Command(lambda: None, lambda: None, "Sample Command 1")
        self.cmd2 = Command(lambda: None, lambda: None, "Sample Command 2")

    def test_init(self):
        self.assertIsInstance(self.cmd1.do, types.FunctionType)
        self.assertIsInstance(self.cmd1.undo, types.FunctionType)
        self.assertEqual(self.cmd1.description, "Sample Command 1")
        self.assertIsInstance(self.cmd2.do, types.FunctionType)
        self.assertIsInstance(self.cmd2.undo, types.FunctionType)
        self.assertEqual(self.cmd2.description, "Sample Command 2")

    def test_call(self):
        mock_cmd1 = MagicMock(self.cmd1)
        mock_cmd2 = MagicMock(self.cmd2)
        mock_cmd1()
        mock_cmd1.undo()
        mock_cmd2.do()
        mock_cmd2.undo()
        self.assertTrue(mock_cmd1.called)
        self.assertTrue(mock_cmd1.undo.called)
        self.assertTrue(mock_cmd2.do.called)
        self.assertTrue(mock_cmd2.undo.called)
        self.assertEqual(mock_cmd1.call_count, 1)
        self.assertEqual(len(mock_cmd1.method_calls), 1)
        self.assertEqual(len(mock_cmd2.method_calls), 2)

class MacroTest(unittest.TestCase):

    def setUp(self):
        self.mac1 = Macro("Sample Macro 1")

        for i in range(1, 6):
            self.mac1.add(Command(lambda: None, lambda: None, 
                "Sample Command {}".format(i)))

    def test_init(self):
        self.assertEqual(self.mac1.description, "Sample Macro 1")
        self.assertEqual(len(self.mac1), 5)

    def test_add(self):
        with self.assertRaises(TypeError):
            self.mac1.add(Macro())

        self.mac1.add(Command(lambda: None, lambda: None, "Test Add"))
        self.assertEqual(len(self.mac1), 6)

    # How to (mock) test do() and undo() in Macro?

if __name__ == "__main__":
    unittest.main()
