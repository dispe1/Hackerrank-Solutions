# Problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    n = int(input())
    b = str(bin(n))

    r = 0
    t = 0

    for i in b:
        if i == '1':
            t += 1
        else:
            r = max(r, t)
            t = 0

    r = max(r, t)

    print(r)
