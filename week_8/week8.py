#!/usr/bin/env python
# Copyright 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# This program has been modified from its original source to fit in 
# Advanced Programming 2016 week 8 exercise.

import argparse
import os
import webbrowser
import feed

# Week 8 Mandatory Tasks
# 1. What is the cause of the bug in week8_threading.py?
# Answer (write as Python comments):
# ...

# Week 8 Additional Tasks
# Spaces for writing answer:
# ...
# ...

TITLE = "What's New - No Concurrency"

def main():
    limit = handle_commandline()
    filename = "whatsnew.html"
    canceled = False
    todo = done = 0

    with open(filename, "wt", encoding="utf-8") as output_file:
        output_file.write("<!doctype html>\n")
        output_file.write("<html><head><title>{}</title></head>\n".format(TITLE))
        output_file.write("<body><h1>{}</h1>\n".format(TITLE))

        todo, done, canceled = write_body(output_file, limit)
        output_file.write("</body></html>\n")

    print()
    if not canceled:
        webbrowser.open(filename)


def write_body(target_file, limit):
    canceled = False
    todo = done = 0
    filename = os.path.join(os.path.dirname(__file__), "whatsnew.dat")

    for feed_source in feed.iter(filename):
        todo += 1
        try:
            ok, result = feed.read(feed_source, limit)
            if not ok:
                print("Failed to read:", result)
            elif result is not None:
                print("Read {} at {}".format(feed_source.title, feed_source.url))

                for item in result:
                    target_file.write(item)

                done += 1
        except KeyboardInterrupt:
            print("Cancelling...")
            canceled = True
            break

    return todo, done, canceled


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit",
                        type=int,
                        default=0,
                        help="The maximum items per feed [default: unlimited]")
    args = parser.parse_args()
    return args.limit

if __name__ == "__main__":
    main()
