# Problem: https://www.hackerrank.com/challenges/making-candies/problem
# Difficulty : Hard
# Score : 45

import math
import os

def minimumPasses(m, w, p, n):
    if n <= p: return math.ceil(n / (m * w))

    curr = candy = 0
    ans = float('inf')

    while candy < n:
        if candy < p:
            i = math.ceil((p - candy) / (m * w))
            curr += i
            candy += m * w * i
            continue

        buy,candy = divmod(candy , p)
        total = m + w + buy
        half = total // 2

        if m > w :
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w

        curr += 1
        candy += m * w
        ans = min(ans, curr + math.ceil((n - candy) / (m * w)))

    return min(ans, curr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])
    w = int(mwpn[1])
    p = int(mwpn[2])
    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result))
    fptr.close()
