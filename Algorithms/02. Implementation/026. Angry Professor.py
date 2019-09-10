# Problem: https://www.hackerrank.com/challenges/angry-professor/problem
# Difficulty : Easy
# Score : 20

import os

def angryProfessor(k, a):
    student = 0

    for t in a:
        if t <= 0:
            student += 1

    if student < k:
        return "YES"
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
