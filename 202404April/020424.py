# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

# Two strings are considered isomorphic by iterating through both simultaneously and mapping 
# each character from one string to its corresponding character in the other string

def isIsomorphic(s, t):
    d = {}
    for i in range(0, len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                return False
        elif t[i] in d.values():
            return False
        else:
            d[s[i]] = t[i]
    return True

s = "egg" #"foo", "paper"
t = "add" #"bar", "title"

print(isIsomorphic(s,t))
