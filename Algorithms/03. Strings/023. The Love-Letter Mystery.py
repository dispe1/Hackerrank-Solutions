# Problem: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# Difficulty : Easy
# Score : 20

import os

def theLoveLetterMystery(s):
    ret = 0
    n = len(s)

    for i in range(n // 2):
        ret += abs(ord(s[i]) - ord(s[n-1-i]))

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
