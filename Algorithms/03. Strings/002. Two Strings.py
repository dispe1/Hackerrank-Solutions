# Problem: https://www.hackerrank.com/challenges/two-strings/problem
# Difficulty : Easy
# Score : 25

import os
import collections

def twoStrings(s1, s2):
    c1 = collections.Counter()
    c2 = collections.Counter()

    for i in s1:
        if i in c1:
            c1[i] += 1
        else:
            c1[i] = 1

    for i in s2:
        if i in c2:
            c2[i] += 1
        else:
            c2[i] = 1

    for i in c1:
        if i in c2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
