# Problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Difficulty : Easy
# Score : 25

import collections

def checkMagazine(magazine, note):
    m = collections.Counter()
    n = collections.Counter()

    for i in magazine:
        if i in m:
            m[i] +=1
        else:
            m[i] = 1

    for i in note:
        if i in n:
            n[i] +=1
        else:
            n[i] = 1

    for i in n:
        if n[i] > m[i]:
            return "No"
    return "Yes"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
