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
import concurrent.futures
import multiprocessing
import webbrowser

import feed

TITLE = "What's New - Futures"


def main():
    limit, concurrency = handle_commandline()
    print("Starting...")
    filename = "whatsnew.dat"
    futures = set()

    with concurrent.futures.ThreadPoolExecutor(
            max_workers=concurrency) as executor:

        # TODO Fix me!
        # BEGIN Write correct implementation here
        for feed_source in feed.iter(filename):
            future = executor.submit(feed.read, feed_source, limit)
            futures.add(future)
        done, filename, canceled = process(futures)
        if canceled:
            executor.shutdown()
        # END

    print("Read {}/{} feeds using {} threads{}".format(done,
        len(futures), concurrency, " [canceled]" if canceled else ""))
    print()
    if not canceled:
        webbrowser.open(filename)


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


def process(futures):
    canceled = False
    done = 0
    filename = "whatsnew.html"
    with open(filename, "wt", encoding="utf-8") as output_file:
        output_file.write("<!doctype html>\n")
        output_file.write("<html><head><title>{}</title></head>\n".format(TITLE))
        output_file.write("<body><h1>{}</h1>\n".format(TITLE))

        canceled, results = wait_for(futures)
        if not canceled:
            for result in (result for ok, result in results if ok and 
                    result is not None):
                done += 1
                for item in result:
                    output_file.write(item)
        else:
            done = sum(1 for ok, result in results if ok and 
                    result is not None)
            output_file.write("</body></html>\n")

    return done, filename, canceled


def wait_for(futures):
    # TODO Implement me!
    # Do not forget to remove `pass` statement!
    canceled = False
    results = []
    try:
        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                ok, result = future.result()
                if not ok:
                    print(result)
                elif result is not None:
                    print("Read {}".format(result[0][4:-6]))
                results.append((ok, result))
            else:
                raise err # Unanticipated
    except KeyboardInterrupt:
        print("canceling...")
        canceled = True
        for future in futures:
            future.cancel()
    return canceled, results

if __name__ == "__main__":
    main()
