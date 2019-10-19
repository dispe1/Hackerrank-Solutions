# Problem: https://www.hackerrank.com/challenges/anagram/problem
# Difficulty : Easy
# Score : 25

import os
from collections import Counter

def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    l = Counter(s[:n//2])
    r = Counter(s[n//2:])

    return len(list((l - r).elements()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
