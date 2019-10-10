# Problem: https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
# Difficulty : Easy
# Score : 30

i = input().split()

p = int(i[0]) / int(i[1])

n = int(input())

r = 1
d = 0
for i in range(n):
    if i < d:
        r *= p
    else:
        r *= (1-p)

print(1-round(r,3))
