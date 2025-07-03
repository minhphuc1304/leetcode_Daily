class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        return max(0, upper - lower - max((s := 0, *[s := s + x for x in differences])) + min((s := 0, *[s := s + x for x in differences])) + 1)