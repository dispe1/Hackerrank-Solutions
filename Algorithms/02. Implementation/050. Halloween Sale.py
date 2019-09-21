# Problem: https://www.hackerrank.com/challenges/halloween-sale/problem
# Difficulty : Easy
# Score : 20

import os

def howManyGames(p, d, m, s):
    ret = 0

    while s >= p:
        ret += 1
        s -= p
        p = max(p-d, m)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer))
    fptr.close()
