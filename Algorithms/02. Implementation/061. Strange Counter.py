# Problem: https://www.hackerrank.com/challenges/strange-code/problem
# Difficulty : Easy
# Score : 30

import os

def strangeCounter(t):
    initNum = 3
    cycleTime = 3

    while t > cycleTime:
        initNum *=2
        cycleTime += initNum

    return cycleTime - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result))
    fptr.close()
