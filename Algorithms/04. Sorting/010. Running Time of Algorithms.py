# Problem: https://www.hackerrank.com/challenges/runningtime/problem
# Difficulty : Easy
# Score : 30

import os

def runningTime(arr):
    ret = 0
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
            ret += 1

        arr[j+1] = tmp

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result))
    fptr.close()
