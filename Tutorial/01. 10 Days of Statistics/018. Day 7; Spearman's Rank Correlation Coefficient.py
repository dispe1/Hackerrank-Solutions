# Problem: https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
# Difficulty : Easy
# Score : 30

n = int(input())

x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

rx = [dict((j, i+1) for i, j in enumerate(sorted(set(x))))[i] for i in x]
ry = [dict((j, i+1) for i, j in enumerate(sorted(set(y))))[i] for i in y]

d = [(rx[i] - ry[i]) ** 2 for i in range(n)]

rxy = 1 - (6 * sum(d)) / (n * (n**2 - 1 ))


print(round(rxy,3))
