# Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
# Difficulty : Easy
# Score : 10

import os
import collections
from functools import reduce

def migratoryBirds(arr):
    count = collections.Counter(arr)
    ar = list(count.items())
    ar.sort()
    result = reduce(lambda a,b: a if a[1] >= b[1] else b, ar)

    return  result[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result))
    fptr.close()
