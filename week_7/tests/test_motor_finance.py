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

import unittest
from week_7.motor_finance import Lender, PaymentMethod
from week_7.motor_finance import Customer

TEST_CUSTOMER_NAME = "dummy"
TEST_BALANCE = 100
EMPTY_BALANCE = 0
TEST_AMOUNT = 10
TEST_METHOD = PaymentMethod.EMONEY


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.lender = Lender(TEST_BALANCE)
        self.brokeLender = Lender(EMPTY_BALANCE)


class LenderTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_init(self):
        self.assertEqual(self.lender.balance, TEST_BALANCE)
        self.assertEqual(self.lender.ledger[TEST_CUSTOMER_NAME], 0)

    def test_give_loan(self):
        self.lender.give_loan(TEST_CUSTOMER_NAME, TEST_AMOUNT, TEST_METHOD)
        self.assertTrue(TEST_CUSTOMER_NAME in self.lender.ledger)
        self.assertEqual(self.lender.balance, TEST_BALANCE - TEST_AMOUNT)
        self.assertEqual(self.lender.ledger[TEST_CUSTOMER_NAME], TEST_AMOUNT)

    def test_receive_payment(self):
        self.lender.give_loan(TEST_CUSTOMER_NAME, TEST_AMOUNT, TEST_METHOD)
        self.lender.receive_payment(TEST_CUSTOMER_NAME, 1, TEST_METHOD)
        self.assertEqual(self.lender.ledger[TEST_CUSTOMER_NAME], TEST_AMOUNT - 1)
        self.lender.receive_payment(TEST_CUSTOMER_NAME, 5, TEST_METHOD)
        self.assertEqual(self.lender.ledger[TEST_CUSTOMER_NAME], TEST_AMOUNT - 6)

    def test_receive_overpayment(self):
        self.lender.give_loan(TEST_CUSTOMER_NAME, TEST_AMOUNT, TEST_METHOD)
        self.lender.receive_payment(TEST_CUSTOMER_NAME, TEST_AMOUNT + 25, TEST_METHOD)
        self.assertEqual(self.lender.ledger[TEST_CUSTOMER_NAME], 0)
        self.assertEqual(self.lender.balance, TEST_BALANCE)

    def test_customer_count(self):
        self.assertEqual(self.lender.customer_count, 0)
        self.lender.give_loan(TEST_CUSTOMER_NAME, TEST_AMOUNT, TEST_METHOD)
        self.assertEqual(self.lender.customer_count, 1)
        self.lender.give_loan("dummy2", TEST_AMOUNT, TEST_METHOD)
        self.assertEqual(self.lender.customer_count, 2)

    def test_total_debt(self):
        self.assertEqual(self.lender.total_loan, 0)
        self.assertEqual(self.brokeLender.total_loan, 0)
        self.lender.give_loan(TEST_CUSTOMER_NAME, TEST_AMOUNT, TEST_METHOD)
        self.assertEqual(self.lender.total_loan, TEST_AMOUNT)
        self.lender.give_loan("dummy2", 50, TEST_METHOD)
        self.assertEqual(self.lender.total_loan, TEST_AMOUNT + 50)


class CustomerTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.customer = Customer(TEST_CUSTOMER_NAME)

    def test_init(self):
        self.assertEqual(self.customer.name, TEST_CUSTOMER_NAME)
        self.assertEqual(self.customer.loan, 0)

