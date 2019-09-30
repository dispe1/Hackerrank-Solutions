# Problem: https://www.hackerrank.com/challenges/absolute-permutation/problem
# Difficulty : Medium
# Score : 40

import os

def absolutePermutation(n, k):
    if k == 0:
        return [i for i in range(1, n+1)]
    if n % (k*2) == 0:
        return [i+k if (i-1) % (2*k) < k else i-k for i in range(1, n+1)]

    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
