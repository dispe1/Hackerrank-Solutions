# Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
# Difficulty : Easy
# Score : 15

import os

def getMoneySpent(keyboards, drives, b):
    arr = [x + y if x+y <=b else -1 for x in keyboards for y in drives]
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent))
    fptr.close()
