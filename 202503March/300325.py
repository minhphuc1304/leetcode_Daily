class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                intervals.append([i, s.rindex(s[i])])
                seen.add(s[i])
        
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        answer = []
        for interval in res:
            answer.append(interval[1] - interval[0] + 1)

        return answer

        