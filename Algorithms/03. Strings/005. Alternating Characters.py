# Problem: https://www.hackerrank.com/challenges/alternating-characters/problem
# Difficulty : Easy
# Score : 20

import os

def alternatingCharacters(s):
    alternateCount = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            alternateCount += 1
    return alternateCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
