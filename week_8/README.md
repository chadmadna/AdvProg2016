Exercise 08: Thread-safe queue & concurrent.futures module
==========================================================

IKI20810 - Advanced Programming @ Faculty of Computer Science 
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, April 22nd 2016*

Your main tasks in this week exercise is to fix a multi-threaded program that 
is using thread-safe queue and complete the implementation of the same program 
using `concurrent.futures` module. The programs function as a RSS feeds 
aggregator that read headlines and its URL from a provided input text file. 

Since the program in this week exercise require an external package and we want 
to introduce one of best practice in Python development, you will be guided to 
create a virtual environment before doing the actual exercise. Virtual environment 
allows you to have an independent Python runtime environment that only contains 
required packages that relevant to your work/project and isolated from the 
machine-wide (i.e. default) Python runtime environment.

Setting-up Virtual Environment
------------------------------

1. Go to the `week_8` exercise directory by using command prompt/shell. 
We are going to set up a virtual environment that will be used for week 8 
exercise.
2. Execute the following command inside `week_8` directory to make a virtual 
environment called **week-8-env**: `python -m venv week-8-env`
3. Ensure that a new directory called **week-8-env** is present in 
`week_8` directory.
4. Since we do not want to add Python packages that will be stored in the virtual 
environment into Git repository, we need to tell Git so that it will not add 
the virtual environment directory and its contents into the repository whenever 
we commited and pushed our works. Create a new file named **.gitignore** file 
in the `week_8` directory and add this following line in the file: `week-8-env/`
5. At this point, you already have a virtual environment that is still 
empty. To begin working on this virtual environment, execute the following 
statement in your command prompt/shell: (VENV is the path to the virtual 
environment directory>)
    - (Windows cmd.exe): VENV`\Scripts\activate.bat`
    - (POSIX bash/zsh): `source` VENV`/bin/activate`
6. Notice that you will have `week-8-env` prepended in the beginning of 
your command prompt/shell. It means that the virtual environment is activated 
and any commands to the Python interpreter will be handled by the interpreter 
in the virtual environment. 
7. Since this week exercise requires a specific version of `feedparser` package 
that is defined in `requirements.txt` file, execute the following command to 
install the required packages listed in the `requirements.txt`: 
`pip install -r requirements.txt`
8. Ensure that `feedparser` package is installed successfully in current virtual 
environment by executing the following command: `pip list`
9. If you want to work on another virtual environment or other project that 
uses system-wide Python packages, you can deactivate current virtual environment 
by executing the following statement in your command prompt/shell:
    - (Windows cmd.exe): VENV`\Scripts\deactivate.bat`
    - (POSIX bash/zsh): `deactivate`
10. If you want to use virtual environment from within PyCharm, you can do so by 
adding new project-specific interpreter via **File** - **Settings...** - 
**Project** - **Project Interpreter** menu. Choose the gear-shaped icon, pick 
**Add Local**, and find the Python interpreter executable in the virtual environment 
using the file chooser window.

Mandatory Tasks Description
---------------------------

There are 3 program variations that you need to take a look and try to execute:

- `week8.py`: Non-concurrent version of RSS feeds aggregator.
- `week8_threading.py`: Multi-threaded version of `week8.py` that uses thread-safe queue (`queue` module).
- `week8_future.py`: Multi-threaded version of `week8.py` that uses `concurrent.futures` module.

Each programs will read a input text file (`whatsnew.dat`) which contains several tech news sites and the 
URL to its RSS feed. Each RSS feeds then will be handled accordingly by the programs. The non-concurrent 
version tries to parse each feeds sequentially while the concurrent versions use multi-threaded mechanisms to 
parse each feeds. The results of each programs are written to an HTML file called `whatsnew.html`.

However, at its current state, the multi-threaded versions (`week8_threading.py` and `week8_future.py`) 
are not working properly. The `week8_threading.py` is not creating threads and has a bug that 
makes the program cannot terminate properly. Similarly, `week8_future.py` is not properly implemented. 
Therefore, you are asked to fix both multi-threaded versions.

Mandatory Checklist
-------------------

Write your written answers in the `week8.py`. For the implementation/coding 
part, write your codes in the correct module.

- [X] Setup a new virtual environment for week 8 exercise.
- [X] Successfully installed `feedparser` package in virtual environment.
- [X] Properly 'ignored' virtual environment directory from being tracked by Git.
- [X] Implement the threads creation in `week8_threading.py`
- [X] Identify the bug in `week8_threading.py`. Hint: Try using PyCharm concurrency diagram and 
read `queue` module documentation carefully, especially regarding `get()` function!
- [X] Write down the cause of the bug in the provided space in `week8.py`.
- [X] Commit your writing to Git repository.
- [X] Fix the bug in `week8_threading.py`.
- [X] Commit and push your work realted to `week8_threading.py` to Git repository.
- [ ] Complete the implementation of `week8_future.py`.
- [ ] Run `week8_future.py` and ensure it is working properly.
- [ ] Commit and push your work related to `week8_future.py` to Git repository.

Additional Checklist
--------------------

Write your answer in the provided space in `week8.py`. Please also include 
data that supports your answer, e.g. screenshot taken from profiler, by 
adding it in the Git repository.

- [ ] All programming works related to week 8 exercise are done in virtual environment.
- [ ] Measure running time of `week8.py`, `week8_thread.py`, and `week8_future.py`.
- [ ] Compare the running time of `week8.py` with one of multi-threaded version 
and try to answer the following questions:
    - How much is the speedup achieved by using multi-threaded approach compared 
    to the non-concurrent approach?

Additional Resources
--------------------

- [queue module documentation](https://docs.python.org/3/library/queue.html)
- [conccurent.futures module documentation](https://docs.python.org/3/library/concurrent.futures.html)
- "[Lightweight Virtual Environments in Python 3.4](http://www.drdobbs.com/architecture-and-design/lightweight-virtual-environments-in-pyth/240167069)" article on Dr. Dobb's.
- "[Don't Make Us Say We Told You So: virtualenv for New Pythonistas](https://www.youtube.com/watch?v=Xdv7vwIIThY)" talk by Renee Chu and Matt Makai at PyCon 2015. Note that this talk discussed third-party packages (e.g. `virtualenv`, `virtualenv-wrapper`) that predated `venv` package offered by Python standard library. `venv` only introduced recently in Python 3.3 and these third-party packages have been available before Python 3.3.
- "[Creating Virtual Environments](https://www.jetbrains.com/help/pycharm/2016.1/creating-virtual-environment.html)" in PyCharm documentation.
