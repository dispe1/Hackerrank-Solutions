# Problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem
# Difficulty : Medium
# Score : 20

def extraLongFactorials(n):
    if n == 1 or n == 0:
        return 1

    return extraLongFactorials(n-1) * n

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
