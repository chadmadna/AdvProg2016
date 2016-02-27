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

# This program has been modified from its original source
# (renderer2.py) to fit in Advanced Programming 2016 week 3 exercise.

import abc
import sys
import textwrap
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape
import Qtrac


@Qtrac.has_methods("header", "paragraph", "footer")
class Renderer(metaclass=abc.ABCMeta):
    pass


MESSAGE = """This is a very short {} paragraph that demonstrates
the simple {} class."""


def main():
    paragraph1 = MESSAGE.format("plain-text", "TextRenderer")
    paragraph2 = """This is another short paragraph just so that we can
see two paragraphs in action."""
    title = "Plain Text"
    textPage = Page(title, TextRenderer(22))
    textPage.add_paragraph(paragraph1)
    textPage.add_paragraph(paragraph2)
    textPage.render()

    print()

    paragraph1 = MESSAGE.format("HTML", "HtmlRenderer")
    title = "HTML"
    file = sys.stdout
    htmlPage = Page(title, HtmlRenderer(HtmlWriter(file)))
    htmlPage.add_paragraph(paragraph1)
    htmlPage.add_paragraph(paragraph2)
    htmlPage.render()

    paragraph1 = MESSAGE.format("Markdown", "MarkdownRenderer")
    paragraph2 = """This is another short paragraph just so that we can
see two paragraphs in action."""
    title = "Markdown"
    markdownPage = Page(title, MarkdownRenderer(MarkdownWriter(sys.stdout)))
    markdownPage.add_paragraph(paragraph1)
    markdownPage.add_paragraph(paragraph2)
    markdownPage.render()

    print()

    try:
        page = Page(title, HtmlWriter())
        page.render()
        print("ERROR! rendering with an invalid renderer")
    except TypeError as err:
        print(err)


class Page:

    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError("Expected object of type Renderer, got {}".
                    format(type(renderer).__name__))
        self.title = title
        self.renderer = renderer
        self.paragraphs = []


    def add_paragraph(self, paragraph):
        """
        Adds a new paragraph into its respective collection. The 
        collection (i.e. list of `paragraphs`) contains all paragraphs 
        that will be written into the page.
        """
        # TODO Implement me!
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()


class TextRenderer:

    FMT_FOOTER = "END OF TEXT PAGE"

    def __init__(self, width=80, file=sys.stdout):
        self.width = width
        self.file = file
        self.previous = False


    def header(self, title):
        self.file.write("{0:^{2}}\n{1:^{2}}\n".format(title,
                "=" * len(title), self.width))


    def paragraph(self, text):
        if self.previous:
            self.file.write("\n")
        self.file.write(textwrap.fill(text, self.width))
        self.file.write("\n")
        self.previous = True


    def footer(self):
        """
        Adds a new line containing string "END OF TEXT PAGE" at the end 
        of written text.
        """
        # TODO Implement me!
        if self.previous:
            self.file.write("\n")
        self.file.write(self.FMT_FOOTER)


class HtmlWriter:

    def __init__(self, file=sys.stdout):
        self.file = file


    def header(self):
        self.file.write("<!doctype html>\n<html>\n")


    def title(self, title):
        self.file.write("<head><title>{}</title></head>\n".format(
                escape(title)))

    def start_body(self):
        self.file.write("<body>\n")


    def body(self, text):
        self.file.write("<p>{}</p>\n".format(escape(text)))


    def end_body(self):
        self.file.write("</body>\n")


    def footer(self):
        self.file.write("</html>\n")


class HtmlRenderer:

    def __init__(self, htmlWriter):
        # TODO Implement me!
        self.writer = htmlWriter

    def header(self, title):
        # TODO Implement me!
        self.writer.header()
        self.writer.title(title)
        self.writer.start_body()

    def paragraph(self, text):
        # TODO Implement me!
        self.writer.body(text)

    def footer(self):
        # TODO Implement me!
        self.writer.end_body()
        self.writer.footer()

class MarkdownRenderer:

    def __init__(self, markdownWriter):
        # TODO Implement me!
        pass

    def header(self, title):
        # TODO Implement me!
        pass

    def paragraph(self, text):
        # TODO Implement me!
        pass

    def footer(self):
        pass

class MarkdownWriter:

    def __init__(self, file=sys.stdout):
        self.file = file

    def header_level_1(self, text):
        """
        Writes a 1st level heading text in Markdown format. Example 
        of 1st level heading:
        
        Lorem Ipsum Dolor Sit Amet
        ==========================

        Notice that the heading text is followed by a sequence of 
        '=' symbols whose length is equal to the lenght of the 
        heading text. Both heading text and sequence of '=' symbols 
        are also appended with a new line symbol ('\n')
        """
        # TODO Implement me!
        pass

    def paragraph(self, text):
        """
        Writes a paragraph text in Markdown format. The text is 
        simply written and appended with a new line symbol ('\n')
        """
        # TODO Implement me!
        pass

if __name__ == "__main__":
    main()
