# Fibonacci sequence whose values do not exceed four million(4000000), find the sum of the even-valued terms.
# https://projecteuler.net/problem=2


class SumFibonacci(object):


    def __init__(self, endrange):
        self.endrange = endrange
        self.num_list = []

    def fib(self):
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    def is_even(self, number):
        if number % 2 == 0:
            return True
        return False

    def fib_generator(self):
        operator = self.fib()
        next(operator)

        for i in range(self.endrange):
            value = next(operator)
            if value > 4000000:
                continue
            if self.is_even(value):
                self.num_list.append(value)

            print(value)

        self.calculate()

    def calculate(self):
        res = 0
        print("List of Even values: {}".format(self.num_list))

        for n in self.num_list:
            res += n
        print("Sum of even numbers is: {}".format(res))



if __name__ == '__main__':
    range_input = int(input("Enter end range as large as you like: "))
    ob = SumFibonacci(range_input)
    ob.fib_generator()
