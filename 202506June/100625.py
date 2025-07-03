class Solution:
    def maxDifference(self, s: str) -> int:
        d=Counter(list(s)) # taking count of all elements  by using Counter
        o=[] # list for odds
        e=[] # list for evens
        for i in d.values():
            if i%2==0:
                e.append(i) # storing even in e list 
            else:
                o.append(i) # storing odd in o list 

# my logic works here 
# to get max difference  no need to check overall list 
# for that this logic is working
# maximum  in difference  of max of o - min of e and min of o - max(e)
        return max((-max(e)+min(o)),(max(o)-min(e)))
        
            # maximum  of that two difference will be the max difference 
        
