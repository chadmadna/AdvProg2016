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
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape


WINNERS = ("Nikolai Andrianov", "Matt Biondi", "BjÃ¸rn DÃ¦hlie",
        "Birgit Fischer", "Sawao Kato", "Larisa Latynina", "Carl Lewis",
        "Michael Phelps", "Mark Spitz", "Jenny Thompson")


def main():
    htmlLayout = Layout(html_tabulator)
    for rows in range(2, 6):
        print(htmlLayout.tabulate(rows, WINNERS))
    textLayout = Layout(text_tabulator)
    for rows in range(2, 6):
        print(textLayout.tabulate(rows, WINNERS))
    alternateLayout = Layout(alternate_table_row_color_html_tabulator)
    for rows in range(2, 6):
        print(alternateLayout.tabulate(rows, WINNERS))


class Layout:

    def __init__(self, tabulator):
        self.tabulate = tabulator

# HOW TO PUT BREAKPOINT ON PYCHARM
# Click on the space beside the line number of the
# line of code you want to stop before while
# debugging. The debugger will halt execution
# just before the breakpoint, so that you can
# inspect code while stepping through line-by-line
# execution.

def html_tabulator(rows, items):    # Broken!

    columns, remainder = divmod(len(items), rows)
    if remainder:
        columns += 1
    column = 0
    table = ['<table border="1">\n']
    for item in items:
        # Originally: 'if column != 0:'
        # Supposed to check if column counter is on zero,
        # indicating the start of a new row.
        if column == 0:
            table.append("<tr>")
        table.append("<td>{}</td>".format(escape(str(item))))
        column += 1
        if column == columns:
            table.append("</tr>\n")
        # Originally: 'column //= columns'
        # Supposed to reset column counter back to 0 by
        # modulo upon reaching column count limit.
        column %= columns
    if table[-1][-1] != "\n":
        table.append("</tr>\n")
    table.append("</table>\n")
    return "".join(table)


def text_tabulator(rows, items):
    columns, remainder = divmod(len(items), rows)
    if remainder:
        columns += 1
        remainder = (rows * columns) - len(items)
        if remainder == columns:
            remainder = 0
    column = columnWidth = 0
    for item in items:
        columnWidth = max(columnWidth, len(item))
    columnDivider = ("-" * (columnWidth + 2)) + "+"
    divider = "+" + (columnDivider * columns) + "\n"
    table = [divider]
    for item in items + (("",) * remainder):
        if column == 0:
            table.append("|")
        table.append(" {:<{}} |".format(item, columnWidth))
        column += 1
        if column == columns:
            table.append("\n")
        column %= columns
    table.append(divider)
    return "".join(table)


def alternate_table_row_color_html_tabulator(rows, items):
    # TODO Implement me!
    columns, remainder = divmod(len(items), rows)
    if remainder:
        columns += 1
    column = 0
    row = 0
    table = ['<table border="1">\n']
    for item in items:
        color = 'blue' if row % 2 else 'red'
        if column == 0:
            table.append("<tr bgcolor={}>".format(color))
        table.append("<td>{}</td>".format(escape(str(item))))
        column += 1
        if column == columns:
            table.append("</tr>\n")
            row += 1
        column %= columns
    if table[-1][-1] != "\n":
        table.append("</tr>\n")
    table.append("</table>\n")
    return "".join(table)

if __name__ == "__main__":
    main()
