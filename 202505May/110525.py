class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        length = 3
        subarrays = []
        consecutive_odds = 0

        for i in range(len(arr) - length + 1):
            subarrays.append(arr[i:i+length])


        for num in subarrays:
            if all(x % 2 == 1 for x in num):
                consecutive_odds = consecutive_odds + 1


        if consecutive_odds > 0:
            return True 
        else:
            return False
                
