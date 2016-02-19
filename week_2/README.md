Exercise 2: Builder Pattern
===========================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, February 19th 2016*

Your task in this exercise is to continue an example of Builder 
pattern implementation. You are required to complete several methods 
in the given code template and able to demonstrate your program can 
generate the output similar to the example in the book. Additionally, 
you are also asked to add new functionality into the Builder class 
so that it can add new element into the form.

This exercise is based on the example program that can be found in 
the textbook chapter 1 page 11 - 16.

Mandatory Checklist
-------------------

* [X] All methods except `add_text()` have been implemented correctly.
* [X] The program is able to create HTML- and TK-based login form.
* [X] `create_register_form()` function is implemented correctly.
* [X] The program is able to create HTML- and TK-based register form.

Additional Checklist
--------------------

* [X] `add_text()` abstract method is added into `AbstractFormBuilder` class correctly.
* [X] Implement `add_text()` method on both `HtmlFormBuilder` and `TkFormBuilder` class.
* [X] The program is able to create a form in which one of its element is created via `add_text()` call.
* [X] The program is able to create a form other than login and register form.
* [X] Student is able to briefly explain the purpose of Builder Pattern and how it is implemented in the exercise program.

Additional Resources
--------------------

N/A

