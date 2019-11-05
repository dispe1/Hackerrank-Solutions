# Problem: https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Difficulty : Easy
# Score : 30

import os

def hourglassSum(arr):
    ret = -1000
    x = len(arr)
    y = len(arr[0])
    shape = [(0,0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]

    for i in range(x-2):
        for j in range(y-2):
            value = sum(arr[i+a][j+b] for a,b in shape)
            ret = max(ret, value)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result))
    fptr.close()
