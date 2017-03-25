# https://projecteuler.net/problem=6
# Sum square difference of first 100 natural numbers

import math
N= 100
sumofsq=0
sq=0
sum=0
for i in range(1,N+1):
	sq=i*i
	sumofsq=sumofsq+sq
	sum=sum+i
diff=(sum*sum)-sumofsq
print(diff)

