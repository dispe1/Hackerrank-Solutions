# Problem: https://www.hackerrank.com/challenges/fair-rations/problem
# Difficulty : Easy
# Score : 25

import os

def fairRations(B):
    ret = 0

    for i in range(len(B)-1, 0, -1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i-1] += 1
            ret += 2

    if B[0] % 2 == 1:
        return "NO"

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result))
    fptr.close()
