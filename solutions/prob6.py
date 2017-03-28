#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=6
# Sum square difference of first 100 natural numbers

import math


class SumSquareDiff(object):

    def __init__(self, endrange):
        self.endrange = endrange

    def cal_square(self, no):
        return no * no

    def sum_upto_endrange(self):
        temp = 0
        for i in range(1, self.endrange + 1):
            temp += i
        return temp

    def sum_of_squares(self):
        sum_square = 0
        for i in range(1, self.endrange + 1):
            sum_square = sum_square + self.cal_square(i)
        return sum_square

    def diff(self):
        return self.cal_square(self.sum_upto_endrange()) \
            - self.sum_of_squares()


ob = SumSquareDiff(100)
print(ob.diff())
