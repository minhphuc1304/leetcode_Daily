class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordCount = Counter(words)
        length = 0
        hasMiddle = False
        
        for word in wordCount:
            reverseWord = word[::-1]
            
            if word == reverseWord:
                pairs = wordCount[word] // 2
                length += pairs * 4
                
                if wordCount[word] % 2 == 1 and not hasMiddle:
                    hasMiddle = True
                    length += 2
            
            elif word < reverseWord and reverseWord in wordCount:
                pairs = min(wordCount[word], wordCount[reverseWord])
                length += pairs * 4
        
        return length        
