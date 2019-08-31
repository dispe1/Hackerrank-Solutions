# Problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# Difficulty : Easy
# Score : 15

import os
import sys

def minimumAbsoluteDifference(arr):
    arr.sort()
    result = sys.maxsize

    for i in range(len(arr)-1):
        a = abs(arr[i] - arr[i+1])
        if a < result:
            result = a

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result))
    fptr.close()
