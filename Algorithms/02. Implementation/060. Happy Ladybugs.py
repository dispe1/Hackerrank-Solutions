# Problem: https://www.hackerrank.com/challenges/happy-ladybugs/problem
# Difficulty : Easy
# Score : 30

import os
from collections import Counter
def happyLadybugs(b):
    c = Counter(b)

    for a in set(b):
        if a != "_" and c[a] == 1:
            return "NO"

    if c["_"] == 0:
        for i in range(1, n-1):
            if b[i-1] != b[i] and b[i+1] != b[i]:
                return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())
        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
