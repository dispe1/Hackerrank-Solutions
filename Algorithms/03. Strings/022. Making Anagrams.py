# Problem: https://www.hackerrank.com/challenges/making-anagrams/problem
# Difficulty : Easy
# Score : 30

import os
import collections

def makingAnagrams(s1, s2):
    aDelete = 0
    bDelete = 0
    aCounter = collections.Counter(s1)
    bCounter = collections.Counter(s2)

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

    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result))
    fptr.close()
