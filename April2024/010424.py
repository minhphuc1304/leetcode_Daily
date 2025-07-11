# https://leetcode.com/problems/length-of-last-word/description/

# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

def length_of_last_word(s):
    words = s.split()
    return len(words[-1])

print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))