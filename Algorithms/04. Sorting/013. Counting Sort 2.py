# Problem: https://www.hackerrank.com/challenges/countingsort2/problem
# Difficulty : Easy
# Score : 30

import os

def countingSort(arr):
    s = [0 for _ in range(100)]
    ret = []

    for i in arr:
        s[i] += 1

    for i in range(len(s)):
        for j in range(s[i]):
            ret.append(i)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()
