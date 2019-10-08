# Problem: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Difficulty : Easy
# Score : 30

import statistics
from scipy.stats import mode

n = int(input())

i = input()
l = i.split()
l = [int(i) for i in l]

print(statistics.mean(l) )
print(statistics.median(l))
print(int(mode(l)[0]))
