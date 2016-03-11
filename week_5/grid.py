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

from command import Command, Macro

class Grid:

    def __init__(self, width, height):
        self.__cells = [ ["white" for _ in range(height)] 
                for _ in range(width) ]

    def cell(self, x, y, color=None):
        # TODO Implement me!
        pass

    @property
    def rows(self):
        return len(self.__cells[0])

    @property
    def columns(self):
        return len(self.__cells)

    def as_html(self, description=None):
        table = ['<table border="1" style="font-family: fixed">']
        if description is not None:
            table.append('<tr><td colspan="{}">{}</td></tr>'.format(
                self.columns, description))
        for y in range(self.rows):
            table.append("<tr>")
            for x in range(self.columns):
                color = self.__cells[x][y]
                name = color if not color.startswith("light") else color[5:]
                char = (name[0].upper() if color != "white" else
                        '<font color="white">X</font>')
                table.append('<td style="background-color: {}">{}</td>'
                        .format(color if color != "red" else "pink", char))
            table.append("</tr>")
        table.append("</table>")
        table = "\n".join(table)

        return table

class UndoableGrid(Grid):

    def create_cell_command(self, x, y, color):
        # TODO Implement me!
        pass
    
    def create_rectangle_macro(self, x0, y0, x1, y1, color):
        # TODO Implement me!
        pass
