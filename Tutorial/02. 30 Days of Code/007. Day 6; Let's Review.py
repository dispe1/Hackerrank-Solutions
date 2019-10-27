# Problem: https://www.hackerrank.com/challenges/30-review-loop/problem
# Difficulty : Easy
# Score : 30

n = int(input())

for i in range(n):
    s = input()
    right = []
    left = []

    for k in range(len(s)):
        if k % 2 == 0:
            right.append(s[k])
        else:
            left.append(s[k])
    print('{} {}'.format(''.join(right), ''.join(left)))
