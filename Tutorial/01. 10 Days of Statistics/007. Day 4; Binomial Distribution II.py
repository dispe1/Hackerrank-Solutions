# Problem: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# Difficulty : Easy
# Score : 30

def factorial(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * factorial(i-1)

i = input().split()
f = float(i[0]) * 0.01

n = int(i[1])
reject = 2
r = 0

for i in range(reject+1):
    r += (factorial(n) / (factorial(i) * factorial(n-i))) * (f ** i) * ((1-f) ** (n-i))
print(round(r,3))

r = 0
for i in range(reject,n+1):
    r += (factorial(n) / (factorial(i) * factorial(n-i))) * (f ** i) * ((1-f) ** (n-i))

print(round(r,3))
