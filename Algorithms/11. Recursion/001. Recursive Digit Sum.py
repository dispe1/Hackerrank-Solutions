# Problem: https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# Difficulty : Medium
# Score : 30

import os

def superDigit(n, k):
    l = len(n)

    while l != 1:
        t = 0
        for i in n:
            t += int(i)

        n = str(t * k)
        k //= k
        l = len(n)

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = nk[0]
    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result))
    fptr.close()
