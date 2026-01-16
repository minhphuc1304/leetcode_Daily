class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int],
                                 vFences: List[int]) -> int:

        deltas, mxDelta = set(), 0
        hFences = sorted(chain(hFences, [1, m]))
        vFences = sorted(chain(vFences, [1, n]))

        for i, top in enumerate(hFences):
            for bot in hFences[i+1:]:
                deltas.add(bot - top)
    
        for i, lft in enumerate(vFences):
            for rgt in vFences[i+1:][::-1]:   #  <-- * 
                delta = rgt - lft
                if delta <= mxDelta or delta not in deltas: continue
                mxDelta = delta
                break

        if mxDelta == 0: return -1
        return pow(mxDelta, 2, 1_000_000_007)
