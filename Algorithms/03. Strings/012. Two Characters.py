# Problem: https://www.hackerrank.com/challenges/two-characters/problem
# Difficulty : Easy
# Score : 20

import os
from itertools import combinations

def alternate(s):
    st = list(set(s))

    if len(st) < 2:
        return 0

    combination = list(combinations(st, len(st)-2))

    ret = 0
    for com in combination:
        tmp = s

        for i in com:
            tmp = tmp.replace(i, "")

        canMake = True

        for i in range(len(tmp)-1):
            if tmp[i] == tmp[i+1]:
                canMake = False
                break

        if canMake and len(tmp) > ret:
            ret = len(tmp)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input()

    result = alternate(s)

    fptr.write(str(result))
    fptr.close()
