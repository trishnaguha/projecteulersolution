# https://projecteuler.net/problem=3
# Largest prime factor of the number 600851475143

import math


class LargestPrimeFactor(object):

    def __init__(self, number):
        self.number = number
        self.num_list = []

    def factors(self):
        i = self.number
        while i > 0:
            if self.number % i == 0:
                yield i
            i -= 1

    def factor_generator(self):
        operator = self.factors()
        next(operator)

        for value in operator:
            if self.is_prime(value):
                self.num_list.append(value)

        print("The list is: {}".format(self.num_list))
        print(max(self.num_list))

    def is_prime(self, fact):
        if fact <= 1:
            return
        elif fact == 2:
            return True
        elif fact % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(fact) + 1), 2):
            if fact % current == 0:
                return False
        return True



ob = LargestPrimeFactor(600851475143)
ob.factor_generator()
