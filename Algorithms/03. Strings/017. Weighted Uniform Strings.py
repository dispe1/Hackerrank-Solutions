# Problem: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# Difficulty : Easy
# Score : 20

import os

def weightedUniformStrings(s, queries):
    ret = []
    prev = ''
    count = 0
    dic = {}

    for c in s:
        if c == prev:
            count += 1
        else:
            prev = c
            count = 1
        dic[(ord(c) - ord('a') + 1) * count] = None

    for q in queries:
        if q in dic:
            ret.append("Yes")
        else:
            ret.append("No")

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.close()
