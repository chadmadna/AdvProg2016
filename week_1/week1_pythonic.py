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

# This program has been modified from its original source (diagram1.py) 
# to fit in Advanced Programming 2016 week 1 lab session.

# Week 1 exercise:
#
# 1. Fill in the blanks in SvgDiagramFactory class - DONE
# 2. Test the program to ensure text- and SVG-based diagrams are 
#    successfully created - DONE
# 3. Implement a new factory class for creating HTML-based diagram
# 4. Modify and test the program to demonstrate that the program can 
#    write HTML-based diagram - DONE
# 5. Refactor this program following the "a more Pythonic Abstract 
#    Factory" described in textbook ch. 1 pg. 9 - 11 - DONE

def main():
    
    textFilename = "diagram.txt"
    svgFilename = "diagram.svg"
    htmlFilename = "diagram.html"

    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(textFilename)
    print("Wrote:", textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)
    print("Wrote:", svgFilename) 

    htmlDiagram = create_diagram(HtmlDiagramFactory)
    htmlDiagram.save(htmlFilename)
    print("Wrote:", htmlFilename)

def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")

    diagram.add(rectangle)
    diagram.add(text)

    return diagram

class DiagramFactory:

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white",
                       stroke="black"):
        return Class.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)
	
    BLANK = " "
    CORNER = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"

    class Diagram:

        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.diagram = DiagramFactory._create_rectangle(self.width,
                    self.height, DiagramFactory.BLANK)

        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char
        
        def save(self, filenameOrFile):
            aFile = None if isinstance(filenameOrFile, str) else \
                    filenameOrFile

            try:
                if aFile is None:
                    aFile = open(filenameOrFile, "w", encoding="utf-8")

                for row in self.diagram:
                    print("".join(row), file=aFile)
            finally:
                if isinstance(filenameOrFile, str) and aFile is not None:
                    aFile.close()

    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            self.x = x
            self.y = y
            self.rows = DiagramFactory._create_rectangle(width, height, 
                        DiagramFactory.BLANK if fill == "white" else "%")

    class Text:

        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]

    def _create_rectangle(width, height, fill):
        rows = [[fill for _ in range(width)] for _ in range(height)]

        for x in range(1, width - 1):
            rows[0][x] = DiagramFactory.HORIZONTAL
            rows[height - 1][x] = DiagramFactory.HORIZONTAL
        
        for y in range(1, height - 1):
            rows[y][0] = DiagramFactory.VERTICAL
            rows[y][width - 1] = DiagramFactory.VERTICAL
        
        for y, x in ((0, 0), (0, width - 1), (height - 1, 0), 
                    (height - 1, width - 1)):
            rows[y][x] = DiagramFactory.CORNER

        return rows


class SvgDiagramFactory(DiagramFactory):

    SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
            "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
    <svg xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
            width="{pxwidth}px" height="{pxheight}px">"""

    SVG_END = "</svg>\n"

    SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
    height="{height}" fill="{fill}" stroke="{stroke}"/>"""

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
    font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20

    class Diagram:
        
        def __init__(self, width, height):
            pxwidth = width * SvgDiagramFactory.SVG_SCALE
            pxheight = height * SvgDiagramFactory.SVG_SCALE
            self.diagram = [SvgDiagramFactory.SVG_START.format(**locals())]
            outline = SvgDiagramFactory.Rectangle(0, 0, width, height, "lightgreen", 
                            "black")
            self.diagram.append(outline.svg)
        
        def add(self, component):
            self.diagram.append(component.svg)
        
        def save(self, filenameOrFile):
            aFile = None if isinstance(filenameOrFile, str) else \
                    filenameOrFile

            try:
                if aFile is None:
                    aFile = open(filenameOrFile, "w", encoding="utf-8")

                aFile.write("\n".join(self.diagram))
                aFile.write("\n" + SvgDiagramFactory.SVG_END)
            finally:
                if isinstance(filenameOrFile, str) and aFile is not None:
                    aFile.close()

    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            width *= SvgDiagramFactory.SVG_SCALE
            height *= SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_RECTANGLE.format(**locals())

    class Text:

        def __init__(self, x, y, text, fontsize):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())

# TODO Create a new factory called HtmlDiagramFactory
# BEGIN Write your HtmlDiagramFactory class and other required classes 
# in the following empty area
# HINT 1 These CSS properties might useful in positioning your HTML 
# diagram elements: padding-top, padding-left, position, left, top
# HINT 2 Use absolute positioning. It (maybe) very difficult to 
# complete the HTML diagram using default (i.e. relative) positioning, 
# considering the nature how the diagram is built in create_diagram() 
# and HTML DOM.

class HtmlDiagramFactory(DiagramFactory):

    HTML_START = """<html><body>"""

    HTML_END = """</body></html>"""

    HTML_RECTANGLE = """<div style="left:{x}; top:{y}; width:{width}; \
                                     height:{height}; border:1px solid {stroke};
                                     background-color:{fill}; position:absolute;"></div>"""

    HTML_TEXT = """<div style="left:{x}; top:{y}; font-size:{fontsize}; \
                            font-family:sans-serif; text-align:left; \
                            position:absolute;">{text}</div>"""

    HTML_SCALE = 20

    class Diagram:
        
        def __init__(self, width, height):
            pxwidth = width * HtmlDiagramFactory.HTML_SCALE
            pxheight = height * HtmlDiagramFactory.HTML_SCALE
            self.diagram = [HtmlDiagramFactory.HTML_START.format(**locals())]
            outline = HtmlDiagramFactory.Rectangle(0, 0, width, height, "lightgreen", 
                            "black")
            self.diagram.append(outline.html)
        
        def add(self, component):
            self.diagram.append(component.html)
        
        def save(self, filenameOrFile):
            aFile = None if isinstance(filenameOrFile, str) else \
                    filenameOrFile

            try:
                if aFile is None:
                    aFile = open(filenameOrFile, "w", encoding="utf-8")

                aFile.write("\n".join(self.diagram))
                aFile.write("\n" + HtmlDiagramFactory.HTML_END)
            finally:
                if isinstance(filenameOrFile, str) and aFile is not None:
                    aFile.close()

    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            x *= HtmlDiagramFactory.HTML_SCALE
            y *= HtmlDiagramFactory.HTML_SCALE
            width *= HtmlDiagramFactory.HTML_SCALE
            height *= HtmlDiagramFactory.HTML_SCALE
            self.html = HtmlDiagramFactory.HTML_RECTANGLE.format(**locals())

    class Text:

        def __init__(self, x, y, text, fontsize):
            x *= HtmlDiagramFactory.HTML_SCALE
            y *= HtmlDiagramFactory.HTML_SCALE
            fontsize *= HtmlDiagramFactory.HTML_SCALE // 10
            self.html = HtmlDiagramFactory.HTML_TEXT.format(**locals())

# END HtmlDiagramFactory implementation

if __name__ == "__main__":
	main()

