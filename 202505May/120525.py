class Solution:
    def findEvenNumbers(self, dig: List[int]) -> List[int]:
        arr = []
        for i in range(100, 999):
            flag = True
            seen = Counter(dig)
            for s in str(i):
                if int(s) not in seen:
                    flag = False
                    break
                else:
                    seen[int(s)] -= 1
                    if seen[int(s)] == 0:
                        del seen[int(s)]
            if flag and i % 2 == 0:
                arr.append(i)
        
        return arr


        
