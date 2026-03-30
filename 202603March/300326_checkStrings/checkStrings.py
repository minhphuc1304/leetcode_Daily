class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        d1_even={}
        d1_odd={}

        d2_even={}
        d2_odd={}

        for i in range(len(s1)):
            if i %2==0:
                d1_even[s1[i]]=d1_even.get(s1[i],0)+1
            else:
                d1_odd[s1[i]]=d1_odd.get(s1[i],0)+1
            
        for i in range(len(s2)):
            if i %2==0:
                d2_even[s2[i]]=d2_even.get(s2[i],0)+1
            else:
                d2_odd[s2[i]]=d2_odd.get(s2[i],0)+1
        return d1_even == d2_even and d1_odd == d2_odd

        
