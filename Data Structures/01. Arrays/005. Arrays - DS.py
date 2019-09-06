# Problem: https://www.hackerrank.com/challenges/arrays-ds/problem
# Difficulty : Easy
# Score : 10

import os

def reverseArray(a):
    return list(reversed(a))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.close()
