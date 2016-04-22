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
import multiprocessing
import os
import queue
import threading
import webbrowser

import feed

TITLE = "What's New - Multi Threading"


def main():
    limit, concurrency = handle_commandline()
    print("Starting...")
    filename = os.path.join(os.path.dirname(__file__), "whatsnew.dat")
    jobs = queue.Queue()
    results = queue.Queue()
    create_threads(limit, jobs, results, concurrency)
    todo = add_jobs(filename, jobs)
    process(todo, jobs, results, concurrency)


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit",
                        type=int,
                        default=0,
                        help="The maximum items per feed [default: unlimited]")
    parser.add_argument("-c", "--concurrency",
                        type=int,
                        default=multiprocessing.cpu_count() * 4,
                        help="Specify the concurrency (for debugging and "
                        "timing) [default: %(default)d]")
    args = parser.parse_args()
    return args.limit, args.concurrency


def create_threads(limit, jobs, results, concurrency):
    # TODO Implement me!
    # Do not forget to remove `pass` statement!
    for i in range(concurrency):
        thread = threading.Thread(target=worker, args=(limit, jobs, results))
        thread.daemon = True
        thread.start()


def worker(limit, jobs, results):
    while True:
        feed_source = jobs.get()
        ok, result = feed.read(feed_source, limit)

        if not ok:
            print(result)
        elif result is not None:
            print("Read {}".format(result[0][4:-6]))
            results.put(result)


def add_jobs(filename, jobs):
    for todo, feed_source in enumerate(feed.iter(filename), start=1):
        jobs.put(feed_source)

    return todo


def process(todo, jobs, results, concurrency):
    canceled = False
    try:
        jobs.join() # Wait for all the work to be done
    except KeyboardInterrupt: # May not work on Windows
        print("Canceling...")
        canceled = True

    if canceled:
        done = results.qsize()
    else:
        done, filename = output(results)
    
    print("Read {}/{} feeds using {} threads{}".format(done, todo, 
        concurrency, " [canceled]" if canceled else ""))
    print()

    if not canceled:
        webbrowser.open(filename)


def output(results):
    done = 0
    filename = "whatsnew.html"

    with open(filename, "wt", encoding="utf-8") as output_file:
        output_file.write("<!doctype html>\n")
        output_file.write("<html><head><title>{}</title></head>\n".format(TITLE))
        output_file.write("<body><h1>{}</h1>\n".format(TITLE))

        while not results.empty(): # Safe because all jobs have finished
            result = results.get_nowait()
            done += 1

            for item in result:
                output_file.write(item)

        output_file.write("</body></html>\n")

    return done, filename

if __name__ == "__main__":
    main()
