# Problem: https://www.hackerrank.com/challenges/mark-and-toys/problem
# Difficulty : Easy
# Score : 35

import os

def maximumToys(prices, k):
    result = 0
    price = 0
    prices.sort()

    while price < k:
        for p in prices:
            if price + p < k:
                result += 1
                price += p
            else:
                return result

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result))
    fptr.close()
