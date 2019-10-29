# Problem: https://www.hackerrank.com/challenges/30-arrays/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()

    print(' '.join(map(str, arr)))
