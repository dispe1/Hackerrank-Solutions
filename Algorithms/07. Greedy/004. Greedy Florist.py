# Problem: https://www.hackerrank.com/challenges/greedy-florist/problem
# Difficulty : Medium
# Score : 35

import os

def getMinimumCost(k, c):
    if k ==  len(c):
        return sum(c)

    c.sort()
    totalCost = 0
    num = 0
    purchased = 0

    for idx in range(len(c)-1, -1, -1):
        totalCost += (purchased+1) * c[idx]
        num += 1
        if num % k == 0:
            purchased += 1

    return totalCost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost))
    fptr.close()
