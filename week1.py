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
# 1. Fill in the blanks in SvgDiagramFactory class
# 2. Test the program to ensure text- and SVG-based diagrams are 
#    successfully created
# 3. Implement a new factory class for creating HTML-based diagram
# 4. Modify and test the program to demonstrate that the program can 
#    write HTML-based diagram
# 5. Refactor this program following the "a more Pythonic Abstract 
#    Factory" described in textbook ch. 1 pg. 9 - 11

def main():

        textFilename = "diagram.txt"
	svgFilename = "diagram.svg"

	txtDiagram = create_diagram(DiagramFactory())
	txtDiagram.save(textFilename)
	print("Wrote:", textFilename)

	svgDiagram = create_diagram(SvgDiagramFactory())
	svgDiagram.save(svgFilename)
	print("Wrote:", svgFilename)

	# TODO Modify this program so that it can write diagram using 
	# the new HtmlDiagramFactory

	htmlFilename = "diagram.html"

	htmlDiagram = create_diagram(HtmlDiagramFactory())
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

	def make_diagram(self, width, height):
		return Diagram(width, height)

	def make_rectangle(self, x, y, width, height, fill="white", 
			stroke="black"):
		return Rectangle(x, y, width, height, fill, stroke)

	def make_text(self, x, y, text, fontsize=12):
		return Text(x, y, text, fontsize)

# TODO Fill in the blanks in SvgDiagramFactory class definition
class SvgDiagramFactory(DiagramFactory):

	def make_diagram(self, width, height):
		# TODO Implement me!
		return SvgDiagram(width, height)

	def make_rectangle(self, x, y, width, height, fill="white", 
			stroke="black"):
		# TODO Implement me!
		return Rectangle(x, y, width, height, fill, stroke)
	
	def make_text(self, x, y, text, fontsize=12):
		# TODO Implement me!
		return Text(x, y, text, fontsize)

	# REMINDER Do not forget to remove 'pass' statement once you have 
	# implemented the method! Replace it with correct statement(s)!
	
BLANK = " "
CORNER = "+"
HORIZONTAL = "-"
VERTICAL = "|"

def _create_rectangle(width, height, fill):
	rows = [[fill for _ in range(width)] for _ in range(height)]

	for x in range(1, width - 1):
		rows[0][x] = HORIZONTAL
		rows[height - 1][x] = HORIZONTAL
	
	for y in range(1, height - 1):
		rows[y][0] = VERTICAL
		rows[y][width - 1] = VERTICAL
	
	for y, x in ((0, 0), (0, width - 1), (height - 1, 0), 
			(height - 1, width - 1)):
		rows[y][x] = CORNER
	
	return rows

class Diagram:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.diagram = _create_rectangle(self.width, self.height, BLANK)
	
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
		self.rows = _create_rectangle(width, height, 
				BLANK if fill == "white" else "%")

class Text:

	def __init__(self, x, y, text, fontsize):
		self.x = x
		self.y = y
		self.rows = [list(text)]

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

class SvgDiagram:

	def __init__(self, width, height):
		pxwidth = width * SVG_SCALE
		pxheight = height * SVG_SCALE
		self.diagram = [SVG_START.format(**locals())]
		outline = SvgRectangle(0, 0, width, height, "lightgreen", 
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
			aFile.write("\n" + SVG_END)
		finally:
			if isinstance(filenameOrFile, str) and aFile is not None:
				aFile.close()

class SvgRectangle:

	def __init__(self, x, y, width, height, fill, stroke):
		x *= SVG_SCALE
		y *= SVG_SCALE
		width *= SVG_SCALE
		height *= SVG_SCALE
		self.svg = SVG_RECTANGLE.format(**locals())

class SvgText:

	def __init__(self, x, y, text, fontsize):
		x *= SVG_SCALE
		y *= SVG_SCALE
		fontsize *= SVG_SCALE // 10
		self.svg = SVG_TEXT.format(**locals())

# TODO Create a new factory called HtmlDiagramFactory
# BEGIN Write your HtmlDiagramFactory class and other required classes 
# in the following empty area
# HINT 1 These CSS properties might useful in positioning your HTML 
# diagram elements: padding-top, padding-left, position, left, top
# HINT 2 Use absolute positioning. It (maybe) very difficult to 
# complete the HTML diagram using default (i.e. relative) positioning, 
# considering the nature how the diagram is built in create_diagram() 
# and HTML DOM.





# END HtmlDiagramFactory implementation

if __name__ == "__main__":
	main()

