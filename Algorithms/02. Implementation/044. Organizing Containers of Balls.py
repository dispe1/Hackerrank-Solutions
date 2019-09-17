# Problem: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
# Difficulty : Medium
# Score : 30

import os

def organizingContainers(container):
    n = len(container)
    c = [0 for i in range(n)]
    t = [0 for i in range(n)]

    for i in range(n):
        c[i] = sum(container[i])
        for j in range(n):
            t[i] += container[j][i]

    c.sort()
    t.sort()

    if c == t:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
