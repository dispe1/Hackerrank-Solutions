# Problem: https://www.hackerrank.com/challenges/crush/problem
# Difficulty : Hard
# Score : 60

import os

def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    r = 0
    x = 0

    for q in queries:
        arr[q[0]-1] += q[2]
        if q[1] < n:
            arr[q[1]] -= q[2]

    for i in arr:
        x += i
        if r < x:
            r = x

    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
