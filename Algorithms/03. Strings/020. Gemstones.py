# Problem: https://www.hackerrank.com/challenges/gem-stones/problem
# Difficulty : Easy
# Score : 20

import os
from collections import Counter
from functools import reduce

def gemstones(arr):
    return len(reduce(lambda x, y: x & y, [set(Counter(i)) for i in arr]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result))
    fptr.close()
