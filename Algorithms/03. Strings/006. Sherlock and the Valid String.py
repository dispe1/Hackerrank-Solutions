# Problem: https://www.hackerrank.com/challenges/alternating-characters/problem
# Difficulty : Medium
# Score : 35

import os
import collections

def isValid(s):
    c = collections.Counter(s)
    c = list(c.values())
    c.sort()
    r = 'YES' if c.count(c[0]) == len(c) or (c.count(c[0]) == len(c) - 1 and c[-1] - c[-2] == 1) or (c.count(c[-1]) == len(c) - 1 and c[0] == 1) else 'NO'
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result)
    fptr.close()
