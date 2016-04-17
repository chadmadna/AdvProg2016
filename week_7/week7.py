#!/usr/bin/env python3
# Copyright 2015-16 Faculty of Computer Science Universitas Indonesia.
# All rights reserved.

# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# Week 7 Mandatory Tasks:
#
# 1. Identify the shared data used in the concurrent simulation.
# Answer: (write as Python comments)
#
##   i) The list 'methods' is shared among threads as read-only data.
##  ii) The variable Lender.balance in 'lender' is shared among threads
##      as read and write data.

# 2. Identify the critical section(s) in the concurrent simulation.
# Answer:
#
##   The methods lender.give_loan() in simulate_loan() and lender.receive_payment()
##   in simulate_pay_installment() are critical sections in the simulation because
##   both methods modify and read lender.balance as shared data.
##
##   Critical section in lender.give_loan():
##       def give_loan(self, customer, amount, method):
##           ...
##           current_balance = self.balance     # Read
##           ...                                # Loan processing
##           self.balance = current_balance     # Write
##           ...
##
##   Critical section in lender.receive_payment():
##       def receive_payment(self, customer, payment, method):
##           ...
##           current_balance = self.balance     # Read
##           ...                                # Payment processing
##           self.balance = current_balance     # Write
##           ...

# 3. Write down your suggestions to fix the problem in the concurrent
# simulation.
# Answer: (write as Python comments)
#
##   Implement a method-level locking system for all methods that
##   modify the shared data. Lock acquisition and release calls will
##   be placed inside methods in motor_finance.py, surrounding the
##   critical sections of each method that modify the shared data.

# Week 7 Additional Tasks:
# Space for writing answer:
# Answer:
#
##    Simulation running time pre-fix:
##        Concurrent: 1.08061 s
##        Sequential: 7.44859 s
##      Speedup: 6.89 x (faster)
##    Simulation running time post-fix:
##        Concurrent: 7.91162 s
##        Sequential: 7.67759 s
##      Speedup: 0.97 x (slower)
##
##    The fix made the concurrent simulation run slower
##    because of the overhead incurred by the locking
##    system and the minimal difference between the
##    serializable, concurrent implementation and the
##    sequential implementation.


import logging
import random
import threading
from motor_finance import Customer, Lender, PaymentMethod
from datetime import datetime

NUM_OF_CUSTOMERS = 20
BALANCE_AMOUNT = 10000

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] (%(threadName)-10s) %(message)s"
)


def simulate_loan(customer, lender, amount, method):
    lender.give_loan(customer, amount, method)
    customer.loan += amount


def simulate_pay_installment(customer, lender, amount, method):
    while customer.loan > 0:
        lender.receive_payment(customer, amount, method)
        customer.loan -= amount


def random_amount():
    half_amount = BALANCE_AMOUNT // NUM_OF_CUSTOMERS
    amount = random.choice(range(half_amount // 2, half_amount + 1))
    return amount


def create_customers(num):
    return [Customer("Customer#{}".format(str(i))) for i in range(num)]


def simulate_sequential():
    # Count start time
    t_start = datetime.now()
    
    lender = Lender(BALANCE_AMOUNT)
    customers = create_customers(NUM_OF_CUSTOMERS)
    methods = list(PaymentMethod)

    logging.debug("Begin sequential simulation")
    logging.debug("Initial balance: {}".format(str(lender.balance)))

    for customer in customers:
        loan_amount = random_amount()
        simulate_loan(customer, lender, loan_amount, random.choice(methods))

    for customer in customers:
        pay_amount = random_amount()
        simulate_pay_installment(customer, lender,
                                 pay_amount, random.choice(methods))
    
    logging.debug("Final balance: {}".format(str(lender.balance)))
    logging.debug("End sequential simulation")

    # Count end time and calculate elapsed time
    t_end = datetime.now()
    delta = t_end - t_start
    logging.debug("Elapsed time: {} s".format(delta.total_seconds()))


def simulate_concurrent():
    # Count start time
    t_start = datetime.now()
    
    lender = Lender(BALANCE_AMOUNT)
    customers = create_customers(NUM_OF_CUSTOMERS)
    methods = list(PaymentMethod)
    threads = []

    logging.debug("Begin concurrent simulation")
    logging.debug("Initial balance: {}".format(str(lender.balance)))

    # Take loan
    for customer in customers:
        loan_amount = random_amount()
        method = random.choice(methods)
        thread = threading.Thread(name="{}-{}".format(customer.name, method.name),
                                  target=simulate_loan,
                                  args=(customer, lender,
                                        loan_amount, method,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Pay loan
    threads = []
    for customer in customers:
        pay_amount = random_amount()
        method = random.choice(methods)
        thread = threading.Thread(name="{}-{}".format(customer.name, method.name),
                                  target=simulate_pay_installment,
                                  args=(customer, lender,
                                        pay_amount, method,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    logging.debug("Final balance: {}".format(str(lender.balance)))
    logging.debug("End concurrent simulation")

    # Count end time and calculate elapsed time
    t_end = datetime.now()
    delta = t_end - t_start
    logging.debug("Elapsed time: {} s".format(delta.total_seconds()))


if __name__ == "__main__":
    simulate_concurrent()
    simulate_sequential()
