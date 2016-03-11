Exercise 5: Command & Interpreter Pattern
=========================================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, March 11th 2016*

Your main task in this exercise is to complete a program that uses 
Command pattern. The program also contains code skeleton for 
implementing Interpreter pattern that left for additional exercise. 
The program constructs a grid visualisation in HTML where the cells 
are colored by executing a series of `Command` objects.

![Output example of Command pattern implementation](/img/sample-1.png)

The picture above depicts the sample output when rendered in a 
web browser. It displays the grid's state after executing one or 
more `Command` objects. 

To test run the Command pattern implementation, execute the following 
command in your OS interactive shell: `python week5.py command` The 
program will run your implementation of Command pattern and produce an 
HTML file named `command_example.html`.

Once you have finished implementing the Command pattern, you can get 
extra credits by completing code skeleton for implementing Interpreter.
It is to allow user control the program via interactive prompt.

The valid commands that accepted by the interpreter are as follow:

* `/start [width] [height]` This command starts the program by constructing 
an empty grid with dimension set to given `width` and `height`.
* `/create cell [x] [y] [color]` This command sets the cell in given 
`x` and `y` position to the given `color`.
* `/create rect [x0] [y0] [x1] [y1] [color]` This command constructs 
a `color`ed rectangle that starts from given `x0` and `y0` to `x1` and 
`y1`.
* `/undo` This command undo the most recent `/create cell` or 
`/create rect` command.
* `/help` This command displays list of valid commands that can be 
executed by user.
* `/exit` This command terminates the program by writing the HTML 
representation of the grid to a file.

The following picture is an example showing the program when accepting 
user commands.

![Accepting user commands in Interpreter mode](/img/sample-2.png)

The program was given 9 commands via the interactive prompt. For each 
`/create` and `/undo` commands, the program creates the HTML table 
representation of the grid and stores it in a list. The strings in the 
list will be concatenated and written into an HTML file when user exits 
the program. 

An example of generated HTML when rendered in a Web browser can be 
seen in the following picture.

![The output when rendered in a Web browser](/img/sample-3.png) 

To test run the Interpreter implementation, execute the following 
command in your OS interactive shell: `python week5.py interpreter` 
The program will begin providing the interactive prompt that will 
accept user commands via standard input.

For more extra credits, there is a test case that is left blank for you 
to implement. It is a test case for testing the implementation of 
`as_html()` method in `test_grid.py`. The skeleton for the test case 
has been provided where you need to provide correct regex assertions.

Mandatory Checklist
-------------------

* [X] Completed all TODO in `command.py`.
* [X] All tests in `test_command.py` pass without failures.
* [X] Commited and pushed changes in `command.py` to GitLab.
* [X] Completed all TODO in `grid.py`.
* [X] All tests except `test_as_html()` in `test_grid.py` 
pass without failures.
* [X] The program is able to produce HTML file containing the result 
of executing `Command` objects.
* [X] Commited and pushed changes in `grid.py` to GitLab.

Additional Checklist
--------------------

* [X] Implemented `do_start()` function in `week5.py`.
* [ ] Implemented `do_create_cell()` function in `week5.py`.
* [ ] Implemented `do_create_rect()` function in `week5.py`.
* [ ] Implemented `do_undo()` function in `week5.py`.
* [ ] Implemented `do_exit()` function in `week5.py`.
* [ ] The program can undo a `/create cell` command. Check the generated HTML file.
* [ ] The program can undo a `/create rect` command. Check the generated HTML file.
* [ ] Completed `test_as_html()` test case in `test_grid.py` using 
regex assertions.

Additional Resources
--------------------

* [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) provides a gentle introduction to regular expression (regex) in Python. The section about matching characters, repeating things, and grouping may help you in finishing the unit test that using regular expression test.
* You may also want to refer to unit tests in previous exercises to see how regex assertions were used.
