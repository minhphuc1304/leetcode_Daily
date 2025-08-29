class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        on=math.ceil(n/2)
        en=n//2
        om=math.ceil(m/2)
        em=m//2
        return (on*em)+(en*om)
