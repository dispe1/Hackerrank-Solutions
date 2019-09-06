# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Difficulty : Easy
# Score : 10

import os

def breakingRecords(scores):
    maxscore = scores[0]
    minscore = scores[0]
    mincount = 0
    maxcount = 0

    for i in range(1,len(scores)):
        if scores[i] > maxscore:
            maxscore = scores[i]
            maxcount += 1
        if scores[i] < minscore:
            minscore = scores[i]
            mincount += 1

    return [maxcount, mincount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.close()
