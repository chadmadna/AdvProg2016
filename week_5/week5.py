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

# This program has been modified from its original source (grid.py, 
# Command.py) to fit in Advanced Programming 2016 week 5 exercise.

import argparse
from collections import OrderedDict
from grid import UndoableGrid

_COMMAND_EXAMPLE_FILENAME = "command_example.html"
_INTERPRETER_EXAMPLE_FILENAME = "interpreter_example.html"
_VALID_COMMAND = {"/start": None, "/create cell": None, 
        "/create rect": None, "/undo": None, "/help": None, 
        "/exit": None}

def command_example():
    html = []
    grid = UndoableGrid(8, 3)   # (1) Empty
    html.append(grid.as_html("(1) Empty"))
    redLeft = grid.create_cell_command(2, 1, "red")
    redRight = grid.create_cell_command(5, 0, "red")
    redLeft()                   # (2) Do Red Cells
    redRight.do()               # OR: redRight()
    html.append(grid.as_html("(2) Do Red Cells"))
    greenLeft = grid.create_cell_command(2, 1, "lightgreen")
    greenLeft()                 # (3) Do Green Cell
    html.append(grid.as_html("(3) Do Green Cell"))
    rectangleLeft = grid.create_rectangle_macro(1, 1, 2, 2, "lightblue")
    rectangleRight = grid.create_rectangle_macro(5, 0, 6, 1, "lightblue")
    rectangleLeft()             # (4) Do Blue Squares
    rectangleRight.do()         # OR: rectangleRight()
    html.append(grid.as_html("(4) Do Blue Squares"))
    rectangleLeft.undo()        # (5) Undo Left Blue Square
    html.append(grid.as_html("(5) Undo Left Blue Square"))
    greenLeft.undo()
    html.append(grid.as_html("(6) Undo Left Green Cell"))
    rectangleRight.undo()       # (7) Undo Right Blue Square
    html.append(grid.as_html("(7) Undo Right Blue Square"))
    redLeft.undo()              # (8) Undo Red Cells
    redRight.undo()
    html.append(grid.as_html("(8) Undo Red Cells"))

    with open(_COMMAND_EXAMPLE_FILENAME, "w") as fh:
        fh.write('<table border="0"><tr><td>{}</td></tr></table>'.format(
        "</td><td>".join(html)))

def interpreter_example():
    context = OrderedDict()
    context["html"] = []
    context["running"] = True
    context["grid"] = None
    context["commands"] = []

    while context['running']:
        user_input = input("AdvProg2016>> ")
        command_func = get_valid_function(user_input)

        if command_func is None:
            print("Provide a valid command!")
            do_help(user_input, context)
        else:
            command_func(user_input, context)

    with open(_INTERPRETER_EXAMPLE_FILENAME, "w") as fh:
        if len(context["html"]) > 0:
            fh.write('<table border="0"><tr><td>{}</td></tr></table>'.format(
            "</td><td>".join(context["html"])))

def get_valid_function(user_input):
    for name in _VALID_COMMAND.keys():
        if user_input.startswith(name):
            return _VALID_COMMAND[name]

    return None

def do_start(user_input, context):
    args = user_input.split(" ")
    try:
        width, height = int(args[1]), int(args[2])
        # TODO Implement me!
        context["grid"] = UndoableGrid(width, height)
    except ValueError:
        print("Incorrect argument(s) type were passed.")
    except IndexError:
        print("Incorrect arguments position.")

def do_create_cell(user_input, context):
    # TODO Implement me!
    args = user_input.split(" ")
    try:
        x, y, color = int(args[2]), int(args[3]), str(args[4])
        command = context["grid"].create_cell_command(x, y, color)
        context["commands"].append(command)
    except ValueError:
        print("Incorrect argument(s) type were passed.")
    except IndexError:
        print("Incorrect arguments position.")

def do_create_rect(user_input, context):
    # TODO Implement me!
    args = user_input.split(" ")
    try:
        x0, y0, x1, y1, color = int(args[2]), int(args[3]),\
                                int(args[4]), int(args[5]), str(args[6])
        macro = context["grid"].create_rectangle_macro(x0, y0, x1, y1, color)
        context["commands"].append(macro)
    except ValueError:
        print("Incorrect argument(s) type were passed.")
    except IndexError:
        print("Incorrect arguments position.")

def do_undo(user_input, context):
    # TODO Implement me!
    undo_command = context["commands"][-1].undo
    context["commands"].append(undo_command)

def do_help(user_input, context):
    print("""Valid commands: 
        /start [width] [height]
        /create cell [x] [y] [colour]
        /create rect [x0] [y0] [x1] [y1] [colour]
        /undo
        /exit""")

def do_exit(user_input, context):
    # TODO Implement me!
    for command in context["commands"]:
        command()
    context["html"].append(context["grid"].as_html("Interpreter Grid"))
    context["running"] = False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", type=str, 
            help="pattern implementation to demonstrate")
    args = parser.parse_args()

    if args.pattern.lower() == "command":
        print("Running Command pattern example...")
        command_example()
        print("Done. See command_example.html")
    elif args.pattern.lower() == "interpreter":
        print("Preparing functions table...")
        _VALID_COMMAND["/start"] = do_start
        _VALID_COMMAND["/create cell"] = do_create_cell
        _VALID_COMMAND["/create rect"] = do_create_rect
        _VALID_COMMAND["/undo"] = do_undo
        _VALID_COMMAND["/help"] = do_help
        _VALID_COMMAND["/exit"] = do_exit
        print("Running Interpreter pattern example...")
        interpreter_example()
        print("Done. See interpreter_example.html")
    else:
        parser.error()

if __name__ == "__main__":
    main()
