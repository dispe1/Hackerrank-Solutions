# Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
# Difficulty : Easy
# Score : 10

import os
import collections
def sockMerchant(n, ar):
    c = collections.Counter()
    result = 0
    for i in ar:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1

    for i in c:
        result += (c[i]//2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result))

    fptr.close()
