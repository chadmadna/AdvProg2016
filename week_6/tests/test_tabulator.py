#!/usr/bin/env python3
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import unittest

from week_6.tabulator import Layout
from week_6.tabulator import html_tabulator, text_tabulator
from week_6.tabulator import alternate_table_row_color_html_tabulator

DATA = ( "Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Veni", "Vedi", "Vici",
         "Carpe", "Diem")


def parse_tr(string):
    rows = string.split("\n")
    return [row for row in rows if row.startswith("<tr")]


def parse_text(string):
    rows = string.split("\n")
    return [row for row in rows if row.endswith("|")]


class HtmlTabulatorTest(unittest.TestCase):

    def setUp(self):
        self.layout = Layout(html_tabulator)

    def test_algorithm_2_rows(self):
        output = self.layout.tabulate(2, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 2)

    def test_algorithm_3_rows(self):
        output = self.layout.tabulate(3, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 3)

    def test_algorithm_4_rows(self):
        output = self.layout.tabulate(4, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 4)

    def test_algorithm_5_rows(self):
        output = self.layout.tabulate(5, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 5)


class TextTabulatorTest(unittest.TestCase):

    def setUp(self):
        self.layout = Layout(text_tabulator)

    def test_algorithm_2_rows(self):
        output = self.layout.tabulate(2, DATA)
        rows = parse_text(output)
        self.assertEqual(len(rows), 2)

    def test_algorithm_3_rows(self):
        output = self.layout.tabulate(3, DATA)
        rows = parse_text(output)
        self.assertEqual(len(rows), 3)

    def test_algorithm_4_rows(self):
        output = self.layout.tabulate(4, DATA)
        rows = parse_text(output)
        self.assertEqual(len(rows), 4)

    def test_algorithm_5_rows(self):
        output = self.layout.tabulate(5, DATA)
        rows = parse_text(output)
        self.assertEqual(len(rows), 5)


class AlternateTableRowHtmlTabulatorTest(HtmlTabulatorTest):

    def setUp(self):
        self.layout = Layout(alternate_table_row_color_html_tabulator)

    def test_algorithm_2_rows(self):
        output = self.layout.tabulate(2, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 2)

        for i in range(len(rows)):
            if i % 2 != 0:
                self.assertRegex(rows[i], r".*(color)*blue.*</tr>$")
            else:
                self.assertRegex(rows[i], r".*(color)*red.*</tr>$")

    def test_algorithm_3_rows(self):
        output = self.layout.tabulate(3, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 3)

        for i in range(len(rows)):
            if i % 2 != 0:
                self.assertRegex(rows[i], r".*(color)*blue.*</tr>$")
            else:
                self.assertRegex(rows[i], r".*(color)*red.*</tr>$")

    def test_algorithm_4_rows(self):
        output = self.layout.tabulate(4, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 4)

        for i in range(len(rows)):
            if i % 2 != 0:
                self.assertRegex(rows[i], r".*(color)*blue.*</tr>$")
            else:
                self.assertRegex(rows[i], r".*(color)*red.*</tr>$")

    def test_algorithm_5_rows(self):
        output = self.layout.tabulate(5, DATA)
        rows = parse_tr(output)
        self.assertEqual(len(rows), 5)

        for i in range(len(rows)):
            if i % 2 != 0:
                self.assertRegex(rows[i], r".*(color)*blue.*</tr>$")
            else:
                self.assertRegex(rows[i], r".*(color)*red.*</tr>$")

if __name__ == "__main__":
    unittest.main()
