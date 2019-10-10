# Problem: https://www.hackerrank.com/challenges/separate-the-numbers/problem
# Difficulty : Easy
# Score : 20

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        n, m = i, i
        j = i
        while j < len(s):
            n = len(s[j-m:j])
            m = len(str(int(s[j-n:j])+1))
            if int(s[j-n:j])+1 != int(s[j:j+m]):
                break

            if j+m == len(s):
                print("YES {}".format(s[:i]))
                return

            j += m

    print("NO")



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
