# Problem: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Difficulty : Easy
# Score : 30

n = int(input())

x = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

m = [x[i] * w[i] for i in range(n)]

print(round(sum(m) / sum(w),1))
