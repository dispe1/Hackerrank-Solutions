# Problem: https://www.hackerrank.com/challenges/solve-me-first/problem
# Difficulty : Medium
# Score : 40

import os

def minimumSwaps(arr):
    result = 0
    idx = 0
    while idx < len(arr):
        if arr[idx] != (idx+1):
            temp = arr[idx]
            arr[idx] = arr[temp-1]
            arr[temp-1] = temp
            idx -= 1
            result += 1

        idx += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res))
    fptr.close()
