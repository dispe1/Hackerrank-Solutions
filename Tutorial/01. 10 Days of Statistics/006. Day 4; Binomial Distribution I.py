# Problem: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# Difficulty : Easy
# Score : 30

def factorial(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * factorial(i-1)

i = input().split()
b = float(i[0])
g = float(i[1])

boy_p = b / (b+g)
girl_p = g / (b+g)

n = 6
boy = 3
r = 0

for i in range(boy,n+1):
    r += (factorial(n) / (factorial(i) * factorial(n-i))) * (boy_p ** i) * (girl_p ** (n-i))
print(round(r,3))
