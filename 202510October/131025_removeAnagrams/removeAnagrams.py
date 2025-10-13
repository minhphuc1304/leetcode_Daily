class Solution(object):
    def removeAnagrams(self, words):
        """
        Remove consecutive anagram words using greedy single-pass approach
        
        Strategy: Keep first occurrence, skip consecutive anagrams
        
        :type words: List[str] - array of lowercase English letter strings
        :rtype: List[str] - filtered array with consecutive anagrams removed
        """
        
        def isAna(s1, s2):
            """
            Check if two strings are anagrams
            
            Anagrams have the same characters in different order
            Key insight: Sorted versions of anagrams are identical!
            
            :param s1: first string
            :param s2: second string
            :return: True if s1 and s2 are anagrams, False otherwise
            
            Example: "abc" and "bca" → sorted: "abc" == "abc" → True
            Example: "abc" and "def" → sorted: "abc" != "def" → False
            """
            return sorted(s1) == sorted(s2)
        
        # 📋 Result list to store non-anagram words
        r = []
        
        # 🔄 Process each word in input array
        for i in words:
            # 🎯 Decision Logic:
            # If result has words AND current word is anagram of last kept word
            if r and isAna(r[-1], i):
                # 🚫 Skip this word (it's a consecutive anagram)
                continue
            
            # ✅ Keep this word (not an anagram of previous, or first word)
            r.append(i)
        
        # 🎉 Return filtered result
        return r


# 🎓 Algorithm Walkthrough Example:
#
# Input: words = ["abba", "baba", "bbaa", "cd", "cd"]
#
# Step-by-step execution:
#
# 1. word = "abba"
#    r = [] (empty)
#    → Append "abba"
#    r = ["abba"]
#
# 2. word = "baba"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("baba")
#    "aabb" == "aabb" → True (anagram!)
#    → Skip "baba"
#    r = ["abba"]
#
# 3. word = "bbaa"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("bbaa")
#    "aabb" == "aabb" → True (anagram!)
#    → Skip "bbaa"
#    r = ["abba"]
#
# 4. word = "cd"
#    r = ["abba"]
#    Compare: sorted("abba") vs sorted("cd")
#    "aabb" != "cd" → False (not anagram)
#    → Append "cd"
#    r = ["abba", "cd"]
#
# 5. word = "cd"
#    r = ["abba", "cd"]
#    Compare: sorted("cd") vs sorted("cd")
#    "cd" == "cd" → True (anagram - identical!)
#    → Skip "cd"
#    r = ["abba", "cd"]
#
# Final result: ["abba", "cd"] ✅
#
# 🔑 Why This Works:
#
# 1. **Greedy Approach**: We keep the first word in each anagram group
# 2. **Consecutive Check**: Only comparing with last kept word is sufficient
# 3. **Sorting Magic**: Anagrams have identical sorted forms
# 4. **Single Pass**: No need for multiple iterations or complex tracking
#
# 🎯 Edge Cases Handled:
# - Empty input: Returns empty list
# - No anagrams: Returns original list
# - All anagrams: Returns first word only
# - Chain of anagrams: Correctly keeps only first
