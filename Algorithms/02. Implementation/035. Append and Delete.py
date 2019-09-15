# Problem: https://www.hackerrank.com/challenges/append-and-delete/problem
# Difficulty : Easy
# Score : 20

import os

def appendAndDelete(s, t, k):
    sameCount = 0
    lenS = len(s)
    lenT = len(t)

    if lenS+lenT < k:
        return "Yes"

    while sameCount < lenS and sameCount < lenT:
        if s[sameCount] == t[sameCount]:
            sameCount += 1
        else:
            break

    minOperation = lenS - sameCount + lenT - sameCount

    if minOperation <= k and (k-minOperation) % 2 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result)
    fptr.close()
