# Problem: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# Difficulty : Easy
# Score : 30

import math

def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

n = int(input())
ar = []
for i in range(n):
    ar.append(int(input()))

for i in ar:
    print(check_prime(i))
