# Problem: https://www.hackerrank.com/challenges/larrys-array/problem
# Difficulty : Medium
# Score : 40

import os

def larrysArray(A):
    inverseConut = sum([sum([1 if A[i] > A[j] else 0 for j in range(i+1, len(A))]) for i in range(len(A))])

    if inverseConut % 2:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
