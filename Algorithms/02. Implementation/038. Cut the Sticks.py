# Problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem
# Difficulty : Easy
# Score : 25

import os

def cutTheSticks(arr):
    answer = []

    while len(arr) > 0:
        answer.append(len(arr))
        arr = [i - min(arr) for i in arr if i != min(arr)]

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
