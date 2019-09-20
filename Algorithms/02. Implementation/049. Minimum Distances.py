# Problem: https://www.hackerrank.com/challenges/minimum-distances/problem
# Difficulty : Easy
# Score : 20

import os
import sys
def minimumDistances(a):
    dic1 = {}
    dic2 = {}

    for i in range(len(a)):
        if a[i] not in dic1:
            dic1[a[i]] =[i]
        elif a[i] not in dic2:
            dic1[a[i]].append(i)
            dic2[a[i]] = dic1[a[i]]
        else:
            dic2[a[i]].append(i)

    ret = sys.maxsize
    for i in dic2:
        ret = min(ret, max(dic2[i]) - min(dic2[i]))

    return ret if ret != sys.maxsize else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result))
    fptr.close()
