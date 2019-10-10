# Problem: https://www.hackerrank.com/challenges/sfunny-string/problem
# Difficulty : Easy
# Score : 30

import os

def countingSort(arr):
    ret = [0 for _ in range(100)]

    for i in arr:
        ret[i] += 1

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()
