#!/usr/bin/env python3
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import unittest
import unittest.mock as mock
from week_6.observer import AbstractView, Observed, SliderModel, HistoryView, LiveView, AlertView


class ObservedTest(unittest.TestCase):

    def setUp(self):
        self.emptyModel = Observed()
        self.model = Observed()
        self.observers = [mock.Mock(spec=AbstractView) for _ in range(5)]

        for obs in self.observers:
            self.model.observers_add(obs)
            obs.update.reset_mock()

    def test_cannot_instantiate_abstract_view(self):
        with self.assertRaises(TypeError):
            obj = AbstractView()
            obj.update()

    def test_observers_add(self):
        obs1 = mock.Mock(spec=AbstractView)
        self.emptyModel.observers_add(obs1)
        obs1.update.assert_called_once_with(self.emptyModel)

        obs2 = mock.Mock(spec=AbstractView)
        self.model.observers_add(obs2)
        obs2.update.assert_called_once_with(self.model)

    def test_observer_discard(self):
        pass

    def test_observers_notify(self):
        self.model.observers_notify()
        for obs in self.observers:
            obs.update.assert_called_once_with(self.model)


class SliderModelTest(unittest.TestCase):

    def setUp(self):
        self.model1 = SliderModel(0, 5, 10)
        self.model2 = SliderModel(10, 20, 50)

    def test_value_property(self):
        self.assertEqual(self.model1.value, 5)
        self.assertEqual(self.model2.value, 20)

    def test_value_setter(self):
        self.model1.value = 7
        self.model2.value = 42
        self.assertEqual(self.model1.value, 7)
        self.assertEqual(self.model2.value, 42)

    def test_minimum_property(self):
        self.assertEqual(self.model1.minimum, 0)
        self.assertEqual(self.model2.minimum, 10)

    def test_minimum_setter(self):
        self.model1.minimum = 3
        self.model2.minimum = 19
        self.assertEqual(self.model1.minimum, 3)
        self.assertEqual(self.model2.minimum, 19)

    def test_maximum_property(self):
        self.assertEqual(self.model1.maximum, 10)
        self.assertEqual(self.model2.maximum, 50)

    def test_maximum_setter(self):
        self.model1.maximum = 15
        self.model2.maximum = 55
        self.assertEqual(self.model1.maximum, 15)
        self.assertEqual(self.model2.maximum, 55)


class HistoryViewTest(unittest.TestCase):

    def setUp(self):
        self.defaultHistoryView = HistoryView()
        self.model = SliderModel(0, 50, 100)

    def test_update(self):
        self.assertTrue(len(self.defaultHistoryView.data) == 0)
        self.defaultHistoryView.update(self.model)
        self.assertTrue(len(self.defaultHistoryView.data) == 1)
        self.defaultHistoryView.update(self.model)
        self.assertTrue(len(self.defaultHistoryView.data) == 2)


class LiveViewTest(unittest.TestCase):

    def setUp(self):
        self.live1 = LiveView()
        self.live2 = LiveView(length=60)
        self.model = SliderModel(0, 50, 100)

    def test_update(self):
        pass


class AlertViewTest(unittest.TestCase):

    def setUp(self):
        self.defaultAlertView = AlertView()
        self.alertView = AlertView(75)
        self.model = SliderModel(0, 50, 100)


    def test_update(self):
        self.defaultAlertView.update(self.model)
        self.alertView.update(self.model)
        self.assertTrue(len(self.defaultAlertView.data) > 0)
        self.assertTrue(len(self.alertView.data) == 0)


if __name__ == '__main__':
    unittest.main()
