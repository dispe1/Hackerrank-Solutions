# Problem: https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
# Difficulty : Hard
# Score : 65

import sys

n = int(input().strip())

for _ in range(n):
    size,mod = [int(val) for val in input().strip().split(' ')]
    arr = [int(val) for val in input().strip().split(' ')]

    sums = [-1] * size
    temp = [-1] * 2
    temp[0] = arr[0] % mod
    temp[1] = 0
    sums[0] = temp

    for pos in range(1, size): # calculate prefix sums
        temp = [-1] * 2
        temp[0] = (sums[pos-1][0] + arr[pos]) % mod
        temp[1] = pos
        sums[pos] = temp

    sums = sorted(sums)
    minimum = sys.maxsize

    for pos in range(0, size-1): #determine the minimum
        if sums[pos][1] > sums[pos+1][1] and (sums[pos+1][0] - sums[pos][0] < minimum):
            minimum = sums[pos+1][0] - sums[pos][0]

    if mod - sums[size-1][0] < minimum: #edge case
        minimum = mod - sums[size-1][0]

    print(mod - minimum)
