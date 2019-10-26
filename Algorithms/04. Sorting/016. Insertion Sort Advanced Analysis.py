# Problem: https://www.hackerrank.com/challenges/insertion-sort/problem
# Difficulty : Advanced
# Score : 50

import os

def getShift(data, i, size):
    j, s = i, 0

    while i > 0:
        s += data[i]
        i &= i-1

    while j < size:
        data[j] += 1
        j += (j & -j)

    return s

def insertionSort(arr):
    size = 10 ** 7
    data = [0 for _ in range(size)]

    return sum(i-getShift(data, v, size) for i, v in enumerate(arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
