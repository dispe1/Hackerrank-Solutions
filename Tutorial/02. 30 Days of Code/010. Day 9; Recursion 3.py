# Problem: https://www.hackerrank.com/challenges/30-recursion/problem
# Difficulty : Easy
# Score : 30

import os

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    result = factorial(n)

    fptr.write(str(result))
    fptr.close()
