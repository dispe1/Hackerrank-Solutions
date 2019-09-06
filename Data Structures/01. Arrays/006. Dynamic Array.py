# Problem: https://www.hackerrank.com/challenges/dynamic-array/problem
# Difficulty : Easy
# Score : 15

import os

def dynamicArray(n, queries):
    l = [[] for _ in range(n)]
    result = []
    lastanswer = 0

    for i in queries:
        a = (lastanswer ^ i[1]) % n

        if i[0] == 1:
            l[a].append(i[2])
        elif i[0] == 2:
            a = (lastanswer ^ i[1]) % n
            lastanswer = l[a][i[2] % len(l[a])]
            result.append(lastanswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()
    n = int(nq[0])
    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
