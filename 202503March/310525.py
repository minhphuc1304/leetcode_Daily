class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0

        # Cost of splits aka partition edges sum. 
        split_costs = []
        for i in range(len(weights) - 1):
            split_costs.append(weights[i] + weights[i + 1])
        
        split_costs.sort() # Helps us get highest/lowest costs. 
        smallest_split_cost = sum(split_costs[:k-1])
        largest_split_cost = sum(split_costs[-(k-1):])
      
        # First and last weight is guaranteed to be in sum. 
        # Just need the smallest/largest inner partition edges sum. 
        min_sum = weights[0] + weights[-1] + smallest_split_cost
        max_sum = weights[0] + weights[-1] + largest_split_cost
        
        return max_sum - min_sum


