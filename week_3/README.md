Exercise 3: Adapter Pattern
===========================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, February 26th 2016*

Your task in this exercise is to complete an implementation of 
Adapter pattern. You are given a program template that will 
produce a page of text whose output depends on the given Renderer 
type. Some parts of the program are left blank and need to be 
implemented.

For extra credits in this exercise, you are asked to implement a 
writer and adapter for a different text format called Markdown. It 
is the text format that is used to write this document.

Starting from this week's exercise, the code template also provides 
a unit test suite that can be executed to ensure your code is 
working matches with the solution. To execute the unit test suite, 
run: `python -m unittest tests/test_week3.py` in your command prompt.

Mandatory Checklist
-------------------

* [ ] `add_paragraph()` in `Page` is implemented correctly and passed the unit test.
* [ ] `footer()` in `TextRenderer` is implemented correctly and passed the unit test.
* [ ] The program is able to produce output correctly using `TextRenderer`.
* [ ] The state of work after completing all mandatory tasks above is commited and pushed to GitLab.
* [ ] All methods in `HtmlRenderer` are implemented correctly and passed the related unit tests.
* [ ] The program is able to produce output correctly using `HtmlRenderer`.
* [ ] The state of work after implementing method(s) in `HtmlRenderer` is commited and pushed to GitLab.

Additional Checklist
--------------------

* [ ] All methods in `MarkdownWriter` are implemented correctly.
* [ ] All methods in `MarkdownRenderer` are implemented correctly.
* [ ] The program is able to produce output correctly using `MarkdownRenderer`.
* [ ] The state of work after completing `MarkdownWriter` and `MarkdownRenderer` is commited and pushed to GitLab.

Additional Resources
--------------------

N/A

