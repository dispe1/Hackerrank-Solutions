# Problem: https://www.hackerrank.com/challenges/special-palindrome-again/problem
# Difficulty : Medium
# Score : 40

import os

def substrCount(n, s):
    totalCount = 0
    count = 0
    arr = []
    prev = None

    for i in range(n):
        if s[i] == prev:
            count +=1
        else:
            if prev is not None:
                arr.append((prev, count))
            prev = s[i]
            count = 1
    arr.append((prev,count))

    for i in arr:
        totalCount += (i[1] * (i[1] + 1) ) // 2

    for i in range(1, len(arr) -1):
        if arr[i-1][0] == arr[i+1][0] and arr[i][1] == 1:
            totalCount += min(arr[i-1][1],arr[i+1][1])

    return totalCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()

    result = substrCount(n, s)

    fptr.write(str(result))
    fptr.close()
