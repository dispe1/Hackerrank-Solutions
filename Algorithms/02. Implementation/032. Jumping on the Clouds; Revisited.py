# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Difficulty : Easy
# Score : 15

import os

def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0
    while True:
        energy -= 1
        i = (i+ k) %n
        if c[i] == 1:
            energy -= 2
        if i == 0:
            break

    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result))
    fptr.close()
