# Problem: https://www.hackerrank.com/challenges/utopian-tree/problem
# Difficulty : Easy
# Score : 20

import os

d = {0:1}

def utopianTree(n):
    if n in d:
        return d[n]

    answer = 0
    if n % 2 == 0:
        answer = utopianTree(n-1) + 1
    else:
        answer = utopianTree(n-1) * 2

    d[n] = answer

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
