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

import unittest
from command import Command, Macro
from grid import Grid, UndoableGrid

class GridTest(unittest.TestCase):

    def setUp(self):
        self.squareGrid = Grid(5, 5)
        self.rectangleGrid = Grid(4, 5)

    def test_cell_getter(self):
        self.assertEqual("white", self.squareGrid.cell(0, 0))
        self.assertEqual("white", self.rectangleGrid.cell(2, 2))

    def test_cell_setter(self):
        self.squareGrid.cell(0, 0, "red")
        self.rectangleGrid.cell(2, 2, "blue")
        self.assertEqual("red", self.squareGrid.cell(0, 0))
        self.assertEqual("blue", self.rectangleGrid.cell(2, 2))

    def test_rows(self):
        self.assertEqual(5, self.squareGrid.rows)
        self.assertEqual(5, self.rectangleGrid.rows)

    def test_columns(self):
        self.assertEqual(5, self.squareGrid.columns)
        self.assertEqual(4, self.rectangleGrid.columns)

    def test_as_html(self):
        from re import findall
        
        # Get generated HTML document
        html_result = self.squareGrid.as_html()

        # TODO Implement me!

        # Has <table> tag and may contain tag properties
        # TODO Write correct assertion here!
        self.assertRegex(html_result, r'<table\s*(\w*="[^>]*")>')

        # Contains more than one <tr> tags
        # TODO Write correct assertion here!
        self.assertTrue(len(findall(r'(<tr>)', html_result)) > 1)

        # Has closed </table> tag
        # TODO Write correct assertion here!
        self.assertRegex(html_result, r'<table\s*(\w*="[^>]*")>(.|\s)*</table>')

class UndoableGridTest(GridTest):

    def setUp(self):
        self.squareGrid = UndoableGrid(5, 5)
        self.rectangleGrid = UndoableGrid(4, 5)

    def test_create_cell_command(self):
        cmd1 = self.squareGrid.create_cell_command(0, 0, "red")
        cmd2 = self.squareGrid.create_cell_command(0, 1, "blue")
        cmd3 = self.rectangleGrid.create_cell_command(1, 0, "red")
        cmd4 = self.rectangleGrid.create_cell_command(1, 1, "blue")
        self.assertIsInstance(cmd1, Command)
        self.assertIsInstance(cmd2, Command)
        self.assertIsInstance(cmd3, Command)
        self.assertIsInstance(cmd4, Command)

    def test_create_rectangle_macro(self):
        mac1 = self.squareGrid.create_rectangle_macro(0, 0, 1, 1, "red")
        mac2 = self.squareGrid.create_rectangle_macro(2, 2, 3, 3, "blue")
        mac3 = self.rectangleGrid.create_rectangle_macro(3, 3, 4, 4, "red")
        mac4 = self.rectangleGrid.create_rectangle_macro(4, 4, 5, 5, "blue")
        self.assertIsInstance(mac1, Macro)
        self.assertIsInstance(mac2, Macro)
        self.assertIsInstance(mac3, Macro)
        self.assertIsInstance(mac4, Macro)

if __name__ == "__main__":
    unittest.main()
