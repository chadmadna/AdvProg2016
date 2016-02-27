#!/usr/bin/env python3
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# This test suite contains unit tests for testing mandatory and
# additional exercise components for week 3 exercise.

import sys
import unittest
from week3 import Page, TextRenderer, HtmlWriter, HtmlRenderer
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape

class MockRenderer:

    def header(self, title):
        print(title)

    def paragraph(self, text):
        print(text)

    def footer(self):
        print("footer")

class MockOutput:

    def __init__(self):
        self.buffer = list()

    def write(self, text):
        self.buffer.append(text)

class PageTest(unittest.TestCase):

    def setUp(self):
        self.page = Page("Test Page", MockRenderer())

    def test_title(self):
        self.assertEqual(self.page.title, "Test Page")

    def test_add_paragraph(self):
        self.page.add_paragraph("Lorem ipsum dolor sit amet.")
        self.assertTrue(len(self.page.paragraphs) > 0)

class TextRendererTest(unittest.TestCase):

    def setUp(self):
        self.renderer = TextRenderer(80, MockOutput())

    def test_header(self):
        title = "Test Header\n"
        self.renderer.header(title)
        output = "".join(self.renderer.file.buffer)
        self.assertRegex(output, title)

    def test_paragraph(self):
        title = "Test Header\n"
        p1 = "Paragraph 1\n"
        self.renderer.header(title)
        self.renderer.paragraph(p1)
        output = "".join(self.renderer.file.buffer)
        self.assertRegex(output, p1)

    def test_footer(self):
        title = "Test Header\n"
        p1 = "Paragraph 1\n"
        self.renderer.header(title)
        self.renderer.paragraph(p1)
        self.renderer.footer()
        output = "".join(self.renderer.file.buffer)
        self.assertRegex(output, r".*END OF TEXT PAGE$")

class HtmlWriterTest(unittest.TestCase):

    def setUp(self):
        self.writer = HtmlWriter(MockOutput())

    def test_header(self):
        self.writer.header()
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r"^<!doctype html>\s*<html>")

    def test_title(self):
        text = escape("Test Title")
        self.writer.title(text)
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r".*<head>\s*<title>\s*{}\s*</title>\s*</head>".format(text))

    def test_start_body(self):
        self.writer.start_body()
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r".*<body>")

    def test_body(self):
        text = escape("Lorem ipsum dolor sit amet")
        self.writer.body(text)
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r".*<p>\s*{}\s*</p>".format(text))

    def test_end_body(self):
        self.writer.end_body()
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r".*</body>")

    def footer(self):
        self.writer.footer()
        output = "".join(self.writer.file.buffer)
        self.assertRegex(output, r".*</html>")

class HtmlRendererTest(unittest.TestCase):

    def setUp(self):
        self.mockFile = MockOutput()
        self.renderer = HtmlRenderer(HtmlWriter(self.mockFile))

    def test_header(self):
        title = escape("Test Header and Title")
        self.renderer.header(title)
        output = "".join(self.mockFile.buffer)
        self.assertRegex(output, r"<title>\s*{}\s*</title>".format(title))

    def test_paragraph(self):
        p1 = escape("Test lorem ipsum dolor sit amet")
        self.renderer.paragraph(p1)
        output = "".join(self.mockFile.buffer)
        self.assertRegex(output, r"<p>\s*{}\s*</p>".format(p1))

    def test_multiple_paragraphs(self):
        p1 = escape("Test 1 Lorem ipsum")
        p2 = escape("Test 2 Dolor sit")
        p3 = escape("Test 3 Amet")

        self.renderer.paragraph(p1)
        self.renderer.paragraph(p2)
        self.renderer.paragraph(p3)

        output = "".join(self.mockFile.buffer)
        self.assertRegex(output, r"<p>\s*{}\s*</p>\s*<p>\s*{}\s*</p>\s*<p>\s*{}\s*</p>".format(p1, p2, p3))

    def test_footer(self):
        self.renderer.footer()
        output = "".join(self.mockFile.buffer)
        self.assertRegex(output, r".*</body>\s*</html>")


if __name__ == "__main__":
    unittest.main()
