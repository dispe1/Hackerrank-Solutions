# Problem: https://www.hackerrank.com/challenges/luck-balance/problem
# Difficulty : Easy
# Score : 20

import os

def luckBalance(k, contests):
    l = []
    r = 0

    for i in contests:
        if i[1] == 0:
            r += i[0]
        else:
            l.append(i[0])

    l.sort()

    if len(l) >k:
        r += sum(l[len(l)-k:]) - sum(l[:len(l)-k])
    else:
        r += sum(l)

    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result))
    fptr.close()
