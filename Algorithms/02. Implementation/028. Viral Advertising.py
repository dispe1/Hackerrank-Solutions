# Problem: https://www.hackerrank.com/challenges/strange-advertising/problem
# Difficulty : Easy
# Score : 15

import os

def viralAdvertising(n):
    day = 0
    shared = 5
    cum = 0

    for day in range(n):
        linked = shared // 2
        cum += linked
        shared = linked * 3

    return cum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result))
    fptr.close()
