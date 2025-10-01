class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = 0
        empty = 0
        while numBottles > 0:
            totalDrank += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return totalDrank
