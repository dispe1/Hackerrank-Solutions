# Problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem
# Difficulty : Easy
# Score :20

import os

def circularArrayRotation(a, k, queries):
    n = len(a)
    r = a[n-(k%n):n] + a[0:n-(k%n)]
    answer = []
    for q in queries:
        answer.append(r[q])

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
