# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Difficulty : Easy
# Score : 10

def miniMaxSum(arr):
    arr.sort()

    print(sum(arr[:4]), sum(arr[-4:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
