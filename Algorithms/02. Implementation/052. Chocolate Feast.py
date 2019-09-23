# Problem: https://www.hackerrank.com/challenges/chocolate-feast/problem
# Difficulty : Easy
# Score : 25

import os

def chocolateFeast(n, c, m):
    ret = n // c
    w = ret

    while w >= m:
        free = w // m
        w %= m
        w += free
        ret += free

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
