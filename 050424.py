# https://leetcode.com/problems/make-the-string-great/description/
# 1544. Make The String Great

def make_Good(s):
    stack = []
    for c in s:
        if not stack: 
            stack.append(c)
        else:
            if abs(ord(c) - ord(stack[-1])) == 32: stack.pop()
            else: stack.append(c)
    return ''.join(stack)

s = "hellLllooooo"

print(make_Good(s))
    