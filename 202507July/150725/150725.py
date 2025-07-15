class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3: 
            return False

        vowels = set("aeiouAEIOU")
        hasVowels = False
        hasConsonant = False 

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasVowels = True
                else:
                    hasConsonant = True

        return hasVowels and hasConsonant
