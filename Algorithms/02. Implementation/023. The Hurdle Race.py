# Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Difficulty : Easy
# Score : 15

import os

def hurdleRace(k, height):
    return max(max(height)-k,0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result))
    fptr.close()
