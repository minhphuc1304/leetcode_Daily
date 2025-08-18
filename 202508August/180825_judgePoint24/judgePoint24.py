class Solution(object):
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in [nums[i]+nums[j], nums[i]-nums[j], nums[j]-nums[i], nums[i]*nums[j]]:
                            if solve(next_nums + [op]):
                                return True
                        if abs(nums[j]) > 1e-6:
                            if solve(next_nums + [nums[i]/nums[j]]):
                                return True
                        if abs(nums[i]) > 1e-6:
                            if solve(next_nums + [nums[j]/nums[i]]):
                                return True
            return False
        return solve(list(map(float, cards)))
