# Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# Difficulty : Easy
# Score : 30

n = 100
mean = 500
std = 80
z = 1.96

error = z * std / (n ** 0.5)

print(mean - error)
print(mean + error)
