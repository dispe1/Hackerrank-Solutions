# Problem: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# Difficulty : Easy
# Score : 30

S = input().strip()

try:
    print(int(S))
except:
    print('Bad String')
