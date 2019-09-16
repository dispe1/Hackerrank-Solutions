# Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem
# Difficulty : Easy
# Score : 20

import os
import collections

def equalizeArray(arr):
    c = collections.Counter(arr)

    return len(arr) - c.most_common()[0][1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result))
    fptr.close()
