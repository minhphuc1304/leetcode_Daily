# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
# 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s):
    key = 0 
    count = 0
    for x in s:
        if x == '(':
            count += 1
            key = max(key,count)
        elif x == ')':
            count -= 1

    return key

# s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
print(maxDepth(s))