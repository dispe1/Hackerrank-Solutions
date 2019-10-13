# Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
# Difficulty : Easy
# Score : 30

import math

m = 250
n = 100
mean = n * 2.4
std = (n ** 0.5) * 2.0

cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * ( 2 ** 0.5))))

print(cdf(m))
