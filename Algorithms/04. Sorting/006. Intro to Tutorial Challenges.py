# Problem: https://www.hackerrank.com/challenges/tutorial-intro/problem
# Difficulty : Easy
# Score : 30

import os

def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result))
    fptr.close()
