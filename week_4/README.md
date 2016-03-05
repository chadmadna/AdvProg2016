Exercise 4: Composite & Decorator Pattern
=========================================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, March 4th 2016*

Your task in this exercise is to complete two kinds of Composite 
pattern implementation and implement two decorators. You are 
given a simple program that illustrates how simple and composite 
objects are created in each version of Composite pattern implementation 
as described in the textbook. Some parts of the source code have 
been omitted and need to be implemented.

During the course of this exercise, you are also asked to implement 
a function decorator (mandatory) and a class decorator (optional). 
The specification of both decorators are described in in-class 
worksheet that was distributed on Wednesday.

For extra credits, you are required to implement several unit 
tests and correctly implement the class decorator.

You can run the unit tests for this exercise by executing the
following command: `python -m unittest discover -s tests -v` 
in `week_4` directory.

Mandatory Checklist
-------------------

* [X] All unit tests (except `test_composite()`) related to methods in 
    `SimpleItem` pass without failures.
* [X] The state of work related to `SimpleItem` implementation is commited 
    and pushed to GitLab.
* [ ] All unit tests (except `test_composite()`) related to methods in 
    `CompositeItem` pass without failures.
* [ ] The state of work related to `CompositeItem` implementation is 
    commited and pushed to GitLab.
* [ ] All unit tests (except `test_create()`, `test_compose()`, 
    `test_composite()`, and `test_print_simple()`) related to methods in 
    `Item` pass without failures.
* [ ] The state of work related to `Item` implementation is 
    commited and pushed to GitLab.
* [ ] Implemented `logged()` function decorator.
* [ ] Decorated `make_item()` and `make_composite()` functions with 
    `logged()` function decorator.
* [ ] The `logged()` decorator is working properly when the program 
    calls `make_item()` and `make_composite()`.
* [ ] The state of work related to implementing function decorator is
    commited and pushed to GitLab.

Additional Checklist
--------------------

* [ ] Implemented `test_composite()` unit test in `SimpleItemTest`.
* [ ] Implemented `test_composite()` unit test in `CompositeItemTest`.
* [ ] Implemented remaining unit tests in `ItemTest`.
* [ ] Implemented `do_log()` class decorator.
* [ ] Decorated `Item` class with `do_log()` class decorator.
* [ ] The `do_log()` class decorator is working properly when the 
    program is run.

Additional Resources
--------------------

N/A

