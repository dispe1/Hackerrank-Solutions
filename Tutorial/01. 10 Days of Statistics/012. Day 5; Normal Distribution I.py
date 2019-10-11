# Problem: https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
# Difficulty : Easy
# Score : 30

import math

mean = 20
std = 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * ( 2 ** 0.5))))

print(cdf(19.5))
print(cdf(22) - cdf(20))
