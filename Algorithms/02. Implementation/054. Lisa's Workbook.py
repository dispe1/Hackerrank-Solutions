# Problem: https://www.hackerrank.com/challenges/lisa-workbook/problem
# Difficulty : Easy
# Score : 25

import os
import math

def workbook(n, k, arr):
    ret = 0
    pageNumber = 1

    for i in range(len(arr)):
        page = math.ceil(arr[i] / k)

        for j in range(0, page):
            if pageNumber in [num for num in range(j*k+1, min(arr[i]+1,(j+1)*k+1))]:
                ret += 1
            pageNumber += 1

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
