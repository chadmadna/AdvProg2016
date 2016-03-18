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

# This program has been modified from its original source (observer.py,
# tabulator4.py) to fit in Advanced Programming 2016 week 5 exercise.

import argparse

import observer
import tabulator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", type=str,
                        help="pattern implementation to demonstrate")
    args = parser.parse_args()

    if args.pattern.lower() == "observer":
        observer.main()
    elif args.pattern.lower() == "strategy":
        tabulator.main()
    else:
        parser.error()


if __name__ == "__main__":
    main()
