# https://projecteuler.net/problem=6
# Sum square difference of first 100 natural numbers

import math

class sumSquareDiff(object):
	
	def __init__(self, number):
        	self.number = number

	def square(self, no):
        	return no*no

	def sum(self):
		sum1=0
		N = self.number
        	for i in range(1,N+1):
			sum1=sum1+i
		return sum1
	
   	def sumofsquares(self):
		sumofsquare=0
        	N = self.number
        	for i in range(1,N+1):
			sumofsquare=sumofsquare+ self.square(i)
		return sumofsquare

		
	def diff(self):
		print(self.square(self.sum())-self.sumofsquares())
		

ob = sumSquareDiff(100)
ob.diff()
