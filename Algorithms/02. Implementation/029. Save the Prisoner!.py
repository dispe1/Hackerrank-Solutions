# Problem: https://www.hackerrank.com/challenges/save-the-prisoner/problem
# Difficulty : Easy
# Score : 15

import os

def saveThePrisoner(n, m, s):
    answer = s + (m-1) % n
    if answer > n:
        answer -=n
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
