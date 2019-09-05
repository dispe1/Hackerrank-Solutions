# Problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Difficulty : Easy
# Score : 10

import os

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result))
    fptr.close()
