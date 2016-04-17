Exercise 7: Ensuring Correctness in Concurrent Program
======================================================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, April 15th 2016*

Your main task in this exercise is to analyse and fix a concurrent 
program. You are given a program that simulates multiple customers 
trying to loan money from lender and paying it back in installments. 

The classes used throughout the program is defined in `motor_finance` 
module. The classes are as follow:

- `PaymentMethod`: This class represents varieties of payment transfer 
methods. It is actually an enumeration of decimal values that models the 
length of delay that might happened during taking and paying back loans.
- `Lender`: This class represents the lender. It provides the money and 
handles bookkeeping for each customers.
- `Customer`: This class represents the customer. It simply keeps the 
name and amount of debt.

The program uses `motor_finance` module amongst several packages in 
standard library and written in `week7` module. The main focus in the 
`week7` module is `simulate_sequential()` and `simulate_concurrent()` 
functions. As its name suggests, `simulate_sequential()` run the 
simulation by having all transactions regarding taking and paying back 
loans are done sequentially. The `simulate_concurrent()` also run the 
simulation similarly with `simulate_sequential()`. However, it uses 
multiple threads where each transactions done by customers are run 
in a thread. Thus, it simulates concurrent transactions and supposed to 
be run faster than its sequential counterpart.

The simulation begin with all customers taking loans from the lender. 
Once every customers have taken loans, they pay the loans back in 
installments until their debt is cleared.

The following is an output example generated when running 
`simulate_sequential()` function:

```
[DEBUG] (MainThread) Begin sequential simulation
[DEBUG] (MainThread) Initial balance: 10000
[DEBUG] (MainThread) Final balance: 10000
[DEBUG] (MainThread) End sequential simulation
```

The program prints the initial and final balance of lender to ensure 
the amount of money is correct. As can be seen in the example above, 
the amount of money is correct before and after running the simulation.

However, if we try to run `simulate_concurrent()` function, the output 
is not correct. One example of the output is as follows:

```
[DEBUG] (MainThread) Begin concurrent simulation
[DEBUG] (MainThread) Initial balance: 10000
[DEBUG] (MainThread) Final balance: 10027
[DEBUG] (MainThread) End concurrent simulation
```

The amount of money at the end of simulation is different. The expected 
amount of money at the end of simulation should be equal to amount of money 
at the beginning of simulation. It means we have issues in the implementation 
of concurrent simulation, which will be analysed and fixed in this exercise.

Mandatory Checklist
-------------------

Write your answers directly in the `week7.py`. For the implementation 
part, write your implementation in the correct module.

- [X] Identify and write the shared data used in the concurrent simulation.
- [X] Identify and write the critical section(s) in the concurrent simulation. 
- [X] Based on what you have learned in the class (and previous courses), write 
down your suggestions to fix the problem present in the concurrent simulation.
- [X] Commit and push your writings to Git repo.
- [X] Implement your suggestions in the program.
- [X] Ensure the program is producing correct output.
- [X] Commit and push your fix to Git repo.

Additional Checklist
--------------------

Write your answer in the provided space in `week7.py`. Please also include 
data that supports your answer, e.g. screenshot taken from profiler, by 
adding it in the Git repo.

- [X] Measure running time of `simulate_sequential()` and 
`simulate_concurrent()` **BEFORE** fixing the program. 
- [X] Measure running time of `simulate_sequential()` and 
`simulate_concurrent()` **AFTER** fixing the program. 
- [X] Try to answer the following questions:
    - How much is the speedup achieved by `simulate_concurrent()` 
    compared to its sequential counterpart?
    - Does `simulate_concurrent()` run faster after you fixed 
    the program? Why?

Hint: You can use cProfile profiler in PyCharm to have finer-grained 
measurement on every calls done in the program.

Additional Resources
--------------------

- [Snippets in PyMOTW](https://pymotw.com/3/threading/index.html) related to threading module
- threading module [documentation](https://docs.python.org/3/library/threading.html)
- Presentations by David Beazley regarding Python Concurrency, e.g. 
[1](http://www.slideshare.net/dabeaz/an-introduction-to-python-concurrency) and 
[2](https://www.youtube.com/watch?v=Obt-vMVdM8s)