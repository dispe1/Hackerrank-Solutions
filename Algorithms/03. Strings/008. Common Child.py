# Problem: https://www.hackerrank.com/challenges/common-child/problem
# Difficulty : Medium
# Score : 60

import os

def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i+1][j], c[i][j+1])

    return c[m][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result))
    fptr.close()
