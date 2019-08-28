# Problem: https://www.hackerrank.com/challenges/count-triplets-1/problem
# Difficulty : Medium
# Score : 35

import os
import collections

def countTriplets(arr, r):
    result = 0
    r2 = collections.Counter()
    r3 = collections.Counter()

    for i in arr:
        if i in r3:
            result += r3[i]
        if i in r2:
            r3[i*r] += r2[i]
        r2[i*r] += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans))
    fptr.close()
