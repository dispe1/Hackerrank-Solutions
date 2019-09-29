# Problem: https://www.hackerrank.com/challenges/3d-surface-area/problem
# Difficulty : Medium
# Score : 30

import os

def surfaceArea(A):
    ret = 2*len(A)*len(A[0]);
    neighs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            for n in neighs:
                y, x = i + n[0], j + n[1]

                if 0 <= y < len(A) and 0 <= x < len(A[0]):
                    ret += max(0, A[i][j]-A[y][x])
                else:
                    ret += A[i][j]

    return ret;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result))
    fptr.close()
