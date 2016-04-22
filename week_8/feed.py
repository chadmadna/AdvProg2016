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

import collections
import feedparser
import html
import socket
import urllib.request
import urllib.error

BODY_FMT = "<h2>{}</h2>\n"
ERROR_FMT = "Error: {}: {}"
LIST_LINK_FMT = '<li><a href="{}">{}</a></li>'
LIST_TITLE_FMT = "<li>{}</li>"

Feed = collections.namedtuple("Feed", "title url")


def iter(filename):
    name = None
    with open(filename, "rt", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.rstrip()

            if not line or line.startswith("#"):
                continue
            if name is None:
                name = line
            else:
                yield Feed(name, line)
                name = None


def read(feed, limit, timeout=10):
    try:
        with urllib.request.urlopen(feed.url, None, timeout) as web_page:
            data = web_page.read()

        body = parse(data, limit)
        if body:
            body = [BODY_FMT.format(html.escape(feed.title))] + body
            return True, body
        return True, None
    except (ValueError, urllib.error.HTTPError, urllib.error.URLError,
            socket.timeout) as error:
        return False, ERROR_FMT.format(feed.url, error)


def parse(data, limit):
    output = []
    feed = feedparser.parse(data) # Atom + RSS

    for entry in feed["entries"]:
        title = entry.get("title")
        link = entry.get("link")

        if title:
            if link:
                output.append(LIST_LINK_FMT.format(link, html.escape(title)))
            else:
                output.append(LIST_TITLE_FMT.format(html.escape(title)))

        if limit and len(output) == limit:
            break

    if output:
        return ["<ul>"] + output + ["</ul>"]
