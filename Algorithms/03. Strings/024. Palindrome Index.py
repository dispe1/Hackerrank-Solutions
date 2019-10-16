# Problem: https://www.hackerrank.com/challenges/palindrome-index/problem
# Difficulty : Easy
# Score : 25

import os

def palindromeIndex(s):

    n = len(s)
    for i in range(n // 2 + 1):
        if s[i] != s[n-1-i]:
            if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
                return n-1-i
            else:
                return i

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
