# Problem: https://www.hackerrank.com/challenges/30-loops/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
        print(str(n) + " x " + str(i) + " = " + str(n * i))
