class Solution:
    def __init__(self):
        self.cache = {}
        self.nums = []
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        def rob_and_next(self, i):
            if i >= len(self.nums):
                return 0
            if i == len(self.nums) - 1:
                return self.nums[i]

            if i in self.cache.keys():
                return self.cache[i]
            else:
                total = max( rob_and_next(self, i+1) ,self.nums[i] + rob_and_next(self, i + 2))
                self.cache[i] = total
                return total
        
        out = rob_and_next(self, 0)
        return out
