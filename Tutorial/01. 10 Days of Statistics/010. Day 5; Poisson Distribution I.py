# Problem: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
# Difficulty : Easy
# Score : 30

import math

e = 2.71828

mean = 2.5
x = 5

print( ((mean ** x) * math.exp(-mean) ) / math.factorial(x) )
