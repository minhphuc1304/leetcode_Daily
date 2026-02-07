class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_before_a , deletion = 0,0

        for i in range(len(s)):
            if s[i] == 'b': 
                b_before_a += 1
            elif b_before_a > 0: 
                b_before_a -= 1
                deletion += 1
        
        return deletion
