# Problem: https://www.hackerrank.com/challenges/the-grid-search/problem
# Difficulty : Medium
# Score : 30

import os

def gridSearch(G, P):
    ret = "NO"

    for i in range(len(G)-len(P)+1):
        for j in range(len(G[0])):
            for k in range(0,len(P)):
                if G[i+k][j:].find(P[k]) != 0:
                    break
                if k == len(P)-1:
                    return "YES"

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
