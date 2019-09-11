# Problem: https://www.hackerrank.com/challenges/permutation-equation/problem
# Difficulty : Easy
# Score : 20

import os

def permutationEquation(p):
    d = {}
    answer = []

    for i in range(len(p)):
        d[p[i]] = i+1

    for i in range(len(p)):
        answer.append(d[d[i+1]])

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
