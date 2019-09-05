# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Difficulty : Easy
# Score : 10

def staircase(n):
    for i in range(n):
        r = ""
        for j in range(n-1-i):
            r += " "
        for j in range(i+1):
            r += "#"
        print(r)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
