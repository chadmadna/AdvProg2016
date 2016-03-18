#!/usr/bin/env python3
# Copyright 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import abc
import datetime
import itertools
import sys
import time


def main():
    historyView = HistoryView()
    liveView = LiveView()
    alertView = AlertView(threshold=20)
    model = SliderModel(0, 0, 40)  # minimum, value, maximum
    model.observers_add(historyView, liveView, alertView)  # liveView produces output
    for value in (7, 23, 37):
        model.value = value  # liveView produces output
    for value, timestamp in historyView.data:
        print("{:3} {}".format(value, datetime.datetime.fromtimestamp(
            timestamp)), file=sys.stderr)
    for value, timestamp in alertView.data:
        print("Exceeded threshold *{}* {:3} {}".format(alertView.threshold,
            value, datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)


class Observed:
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        # TODO Implement me!
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        # TODO Implement me!
        for observer in self.__observers:
            observer.update(self)

class SliderModel(Observed):
    def __init__(self, minimum, value, maximum):
        super().__init__()
        # These must exist before using their property setters
        self.__minimum = self.__value = self.__maximum = None
        self.minimum = minimum
        self.value = value
        self.maximum = maximum

    @property
    def value(self):
        # TODO Implement me!
        return self.__value

    @value.setter
    def value(self, value):
        # TODO Implement me!
        if self.__value != value:
            self.__value = value
            self.observers_notify()

    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, value):
        # TODO Implement me!
        if self.__minimum != value:
            self.__minimum = value
            self.observers_notify()

    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, value):
        # TODO Implement me!
        if self.__maximum != value:
            self.__maximum = value
            self.observers_notify()


class AbstractView(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, model):
        pass


class HistoryView(AbstractView):
    def __init__(self):
        self.data = []

    def update(self, model):
        self.data.append((model.value, time.time()))


class LiveView(AbstractView):
    def __init__(self, length=40):
        self.length = length

    def update(self, model):
        # TODO Fix me!
        tippingPoint = round(model.value * self.length /
                             (model.maximum - model.minimum))
        td = '<td style="background-color: {}">&nbsp;</td>'
        html = ['<table style="font-family: monospace" border="0"><tr>']
        html.extend(td.format("darkblue") * tippingPoint)
        html.extend(td.format("cyan") * (self.length - tippingPoint))
        html.append("<td>{}</td></tr></table>".format(model.value))
        print("".join(html), file=sys.stdout)


class AlertView(HistoryView):

    def __init__(self, threshold=40):
        # TODO Implement me!
        pass

    def update(self, model):
        # TODO Implement me!
        pass


if __name__ == "__main__":
    main()
