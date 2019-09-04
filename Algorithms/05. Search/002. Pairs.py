# Problem: https://www.hackerrank.com/challenges/pairs/problem
# Difficulty : Medium
# Score : 50

import os

def pairs(k, arr):
    return len(set(arr) & set(x + k for x in arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result))
    fptr.close()
