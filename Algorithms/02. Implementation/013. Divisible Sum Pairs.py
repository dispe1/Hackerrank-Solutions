# Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Difficulty : Easy
# Score : 10

import os

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(n-1):
        for j in ar[i+1:]:
            if (ar[i] + j) % k == 0:
                result += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result))
    fptr.close()
