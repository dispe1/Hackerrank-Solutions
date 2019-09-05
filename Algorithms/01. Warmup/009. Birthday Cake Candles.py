# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Difficulty : Easy
# Score : 10

import os

def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result))
    fptr.close()
