# Problem: https://www.hackerrank.com/challenges/the-time-in-words/problem
# Difficulty : Medium
# Score : 25

import os

def timeInWords(h, m):
    hour = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    minutes = ["o' clock", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes", "twenty eight minutes", "twenty nine minutes", "half"]

    if m == 0:
        return hour[h-1] + " " + minutes[m]
    elif m <= 30:
        return minutes[m] + " past " + hour[h-1]
    else:
        return minutes[29-m] + " to " + hour[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())
    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result)
    fptr.close()
