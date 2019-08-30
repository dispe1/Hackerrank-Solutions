# Problem: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# Difficulty : Easy
# Score : 25

import os
import collections

def makeAnagram(a, b):
    aDelete = 0
    bDelete = 0
    aCounter = collections.Counter(a)
    bCounter = collections.Counter(b)

    for i in aCounter:
        if i not in bCounter:
            aDelete += aCounter[i]
        else:
            if aCounter[i] > bCounter[i]:
                aDelete += (aCounter[i] - bCounter[i])

    for i in bCounter:
        if i not in aCounter:
            bDelete += bCounter[i]
        else:
            if bCounter[i] > aCounter[i]:
                bDelete += (bCounter[i] - aCounter[i])


    return aDelete + bDelete

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res))
    fptr.close()
