# Problem: https://www.hackerrank.com/challenges/service-lane/problem
# Difficulty : Easy
# Score : 20

import os

def serviceLane(n, cases, width):
    ret = []

    for case in cases:
        w = width[case[0]:case[1]+1]
        m = min(w)
        if w[0] >= m and w[-1] >= m:
            ret.append(m)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
