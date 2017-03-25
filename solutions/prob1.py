# Sum of multiples of 3 or 5 below 1000
# https://projecteuler.net/problem=1

class SumOfMultiples(object):

    def sum_of_multiples(self):
        sum_list = []
        res = 0

        for num in range(1, 1000):
            if self.is_multiple(num):
                sum_list.append(num)

        for n in sum_list:
            res += n

        return res

    def is_multiple(self, number):
        if number % 3 == 0 or number % 5 == 0:
            return True
        return False

ob = SumOfMultiples()
print(ob.sum_of_multiples())
