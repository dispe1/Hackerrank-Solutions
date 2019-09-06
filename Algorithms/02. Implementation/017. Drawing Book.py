# Problem: https://www.hackerrank.com/challenges/drawing-book/problem
# Difficulty : Easy
# Score : 10

import os

def pageCount(n, p):
    if p - 1 < n - p:
        return p // 2
    else:
        if n % 2 == 0:
            return (1+n-p) // 2
        else:
            return (n-p) // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result))
    fptr.close()
