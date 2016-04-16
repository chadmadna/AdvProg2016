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

import collections
import enum
import time


class PaymentMethod(enum.Enum):

    EMONEY = 0.05
    CASH = 0.10
    CREDIT = 0.15
    TRANSFER = 0.20
    BITCOIN = 0.25


class Lender:

    def __init__(self, balance=10000):
        self.balance = balance
        self.ledger = collections.defaultdict(lambda: 0)

    def give_loan(self, customer, amount, method):
        current_balance = self.balance
        current_balance -= amount

        # time.sleep simulates delay in transaction that might happened
        # when using certain payment method
        # DO NOT REMOVE
        time.sleep(method.value)
        self.balance = current_balance
        self.ledger[customer] += amount

    def receive_payment(self, customer, payment, method):
        current_balance = self.balance
        debt = self.ledger[customer]

        if debt - payment < 0:
            payment = payment + (debt - payment)

        # time.sleep simulates delay in transaction that might happened
        # when using certain payment method
        # DO NOT REMOVE
        time.sleep(method.value)
        debt -= payment
        current_balance += payment
        self.balance = current_balance
        self.ledger[customer] = debt

    @property
    def customer_count(self):
        return len(self.ledger)

    @property
    def total_loan(self):
        return sum(self.ledger.values())


class Customer:

    def __init__(self, name):
        self.name = name
        self.loan = 0
