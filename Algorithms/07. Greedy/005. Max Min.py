# Problem: https://www.hackerrank.com/challenges/angry-children/problem
# Difficulty : Medium
# Score : 35

import os
import sys

def maxMin(k, arr):
    arr.sort()
    minUnfairness = sys.maxsize

    for i in range(len(arr)-k+1):
        unfairness = arr[i+k-1] - arr[i]
        if unfairness < minUnfairness:
            minUnfairness = unfairness

    return minUnfairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result))
    fptr.close()
