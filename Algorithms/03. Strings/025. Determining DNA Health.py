# Problem: https://www.hackerrank.com/challenges/determining-dna-health/problem
# Difficulty : Hard
# Score : 50

from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict

def getHealth(seq, first, last, largest):
    h, ls = 0, len(seq)

    for f in range(ls):
        for j in range(1, largest+1):
            if f+j > ls:
                break
            sub = seq[f:f+j]
            if sub not in subs:
                break
            if sub not in gMap:
                continue
            ids, hs = gMap[sub]
            h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
    return h

if __name__ == '__main__':

    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))

    gMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for i, gene in enumerate(genes):
        gMap[gene][0].append(i)
        for j in range(1, min(len(gene), 500)+1):
            subs.add(gene[:j])

    for v in gMap.values():
        for i, ix in enumerate(v[0]):
            v[1].append(v[1][i]+health[ix])

    largest = max(list(map(len, genes)))
    hMin, hMax = inf, 0

    s = int(input())
    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        h = getHealth(d, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)

    print(hMin, hMax)
