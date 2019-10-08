# Problem: https://www.hackerrank.com/challenges/s10-standard-deviation/problem
# Difficulty : Easy
# Score : 30

import math

n = int(input())

l = [int(i) for i in input().split()]

average = sum(l) / n

ar = [(i-average) ** 2 for i in l]

mean = math.sqrt(sum(ar)/n)

print(mean)
