# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Difficulty : Easy
# Score : 10


import os
from functools import reduce
from math import gcd

def getTotalX(a, b):
    lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
    gcd_b = reduce(gcd, b)

    return sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total))
    f.close()
