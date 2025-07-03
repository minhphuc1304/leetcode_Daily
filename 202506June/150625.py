class Solution:
    def maxDiff(self, n: int) -> int:
        list1_max, temp = [], n
        list2_min = []

        
        while temp > 0:
            list1_max.append(temp % 10)
            temp //= 10

        list1_max.reverse()
        N = len(list1_max)
        list2_min = list1_max[:]  

       
        for i in range(N):
            if list1_max[i] < 9:
                to_replace = list1_max[i]
                break
        else:
            to_replace = -1 

        if to_replace != -1:
            for i in range(N):
                if list1_max[i] == to_replace:
                    list1_max[i] = 9

        
        if list2_min[0] != 1:
            to_replace = list2_min[0]
            for i in range(N):
                if list2_min[i] == to_replace:
                    list2_min[i] = 1
        else:
            for i in range(1, N):
                if list2_min[i] not in [0, 1]:
                    to_replace = list2_min[i]
                    for j in range(1, N):
                        if list2_min[j] == to_replace:
                            list2_min[j] = 0
                    break

       
        max_val = 0
        min_val = 0
        for i in range(N):
            max_val = max_val * 10 + list1_max[i]
            min_val = min_val * 10 + list2_min[i]

        return max_val - min_val
