# Problem: https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem
# Difficulty : Advanced
# Score : 50

import os
from collections import Counter

def reverseShuffleMerge(s):
        char_freq = Counter(s)
        used_chars = Counter()
        remain_chars = Counter(s)

        res = []

        def can_use(char):
                return (char_freq[char] // 2 - used_chars[char]) > 0

        def can_pop(char):
                needed_chars = char_freq[char] // 2 - used_chars[char]
                return remain_chars[char] > needed_chars

        for char in reversed(s):
                if can_use(char):
                        while res and res[-1] > char and can_pop(res[-1]):
                                removed_char = res.pop()
                                used_chars[removed_char] -= 1
                        used_chars[char] += 1
                        res.append(char)

                remain_chars[char] -= 1

        return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result)
    fptr.close()
