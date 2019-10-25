# Problem: https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
        print("Weird")
    elif 6 <= N <= 20:
        print("Weird")
    else:
        print("Not Weird")
