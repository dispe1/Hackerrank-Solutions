# Problem: https://www.hackerrank.com/challenges/closest-numbers/problem
# Difficulty : Easy
# Score : 35

import os
import sys

def closestNumbers(arr):
    minDif = sys.maxsize
    ret = []
    arr.sort()

    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])

        if dif < minDif:
            minDif = dif
            ret = [arr[i], arr[i+1]]

        elif dif == minDif:
            ret.append(arr[i])
            ret.append(arr[i+1])

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()
