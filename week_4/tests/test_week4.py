#!/usr/bin/env python3
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# This test suite contains unit tests for testing mandatory and
# additional exercise components for week 4 exercise.

import unittest
import sys
from week4 import SimpleItem, CompositeItem, Item

class MockStdout:
    """This class is a stand-in for sys.stdout required in several 
    methods that produce output into command prompt/console.
    """

    def __init__(self):
        self.buffer = list()

    def write(self, text):
        self.buffer.append(text)

    def __repr__(self):
        return "".join(self.buffer)


class SimpleItemTest(unittest.TestCase):
    
    def setUp(self):
        self.pencil = SimpleItem("Pencil", 0.40)
        self.ruler = SimpleItem("Ruler", 1.60)
        self.eraser = SimpleItem("Eraser", 0.20)

    def test_create(self):
        self.assertEqual(self.pencil.name, "Pencil")
        self.assertAlmostEqual(self.pencil.price, 0.40)

    def test_composite(self):
        # TODO Implement me!
        # Hint: Try asserting that a simple (non-composite) object 
        # is not a composite object!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")


class CompositeItemTest(SimpleItemTest):

    def setUp(self):
        super().setUp()
        self.pencilSet = CompositeItem("Pencil Set", self.pencil, 
                self.ruler, self.eraser)
        self.box = SimpleItem("Box", 1.00)
        self.boxedPencilSet = CompositeItem("Boxed Pencil Set", 
                self.box, self.pencilSet)
        self.boxedPencilSet.add(self.pencil)

    def test_create(self):
        super().test_create()
        self.assertEqual(self.boxedPencilSet.name, "Boxed Pencil Set")
        self.assertAlmostEqual(self.boxedPencilSet.price, 3.60)

    def test_composite(self):
        # TODO Implement me!
        # Hint: Try asserting that a composite object is really a 
        # composite object!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.pencil = Item.create("Pencil", 0.40)
        self.ruler = Item.create("Ruler", 1.60)
        self.eraser = Item.create("Eraser", 0.20)
        self.pencilSet = Item.compose("Pencil Set", self.pencil,
                                      self.ruler, self.eraser)
        self.stdout = MockStdout()

    def test_create(self):
        # TODO Implement me!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")
        tipex = Item.create("Tipex", 1.00)
        self.assertEqual(tipex.name, "Tipex")
        self.assertAlmostEqual(tipex.price, 1.00)
        self.assertFalse(tipex.composite)

    def test_compose(self):
        # TODO Implement me!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")

    def test_composite(self):
        # TODO Implement me!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")

    def test_add_to_composite(self):
        lead = Item.create("Lead", 0.05)
        self.pencilSet.add(lead)
        self.assertAlmostEqual(self.pencilSet.price, 2.25)

        pen = Item.create("Pen", 0.25)
        self.pencilSet.add(pen)
        self.assertAlmostEqual(self.pencilSet.price, 2.50)

    def test_add_to_simple(self):
        lead = Item.create("Lead", 0.05)
        self.assertFalse(self.pencil.composite)
        self.pencil.add(lead)
        self.assertTrue(self.pencil.composite)
        self.assertAlmostEqual(self.pencil.price, 0.45)

    def test_remove_simple(self):
        lead = Item.create("Lead", 0.05)
        self.assertFalse(self.pencil.composite)
        self.pencil.add(lead)
        self.pencil.remove(lead)
        self.assertFalse(self.pencil.composite)

    def test_remove_not_in_composite(self):
        mysterious = Item.create("Wat", 9.99)
        with self.assertRaises(ValueError):
            self.pencilSet.remove(mysterious)

    def test_remove_from_composite(self):
        self.assertTrue(self.pencilSet.composite)
        self.pencilSet.remove(self.eraser)
        self.assertAlmostEqual(self.pencilSet.price, 2.00)
        self.pencilSet.remove(self.pencil)
        self.assertAlmostEqual(self.pencilSet.price, 1.60)
        self.pencilSet.remove(self.ruler)
        self.assertAlmostEqual(self.pencilSet.price, 0.00)
        self.assertFalse(self.pencilSet.composite)

    def test_price_getter(self):
        self.assertAlmostEqual(self.pencil.price, 0.40)
        self.assertAlmostEqual(self.ruler.price, 1.60)
        self.assertAlmostEqual(self.eraser.price, 0.20)
        self.assertAlmostEqual(self.pencilSet.price, 2.20)

    def test_price_setter(self):
        self.pencil.price = 1.23
        self.ruler.price = 4.56
        self.eraser.price = 7.89
        self.assertAlmostEqual(self.pencil.price, 1.23)
        self.assertAlmostEqual(self.ruler.price, 4.56)
        self.assertAlmostEqual(self.eraser.price, 7.89)

    def test_price_setter_composite(self):
        self.pencil.price = 0.50
        self.ruler.price = 1.70
        self.assertAlmostEqual(self.pencilSet.price, 2.40)

    def test_print_simple(self):
        # TODO Implement me!
        # Do not forget to replace self.fail() statement with 
        # correct assertion method(s)!
        self.fail("Not yet implemented.")


if __name__ == "__main__":
    unittest.main()
