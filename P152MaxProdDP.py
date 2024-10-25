class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = {0: (nums[0], nums[0])}
        maxProd = nums[0]
        for i in range(1,len(nums)):
            p1 = nums[i] * cache[i-1][0]
            p2 = nums[i] * cache[i-1][1]
            take = max(p1, p2)
            not_take = nums[i]
            if take > not_take:
                cache[i] = (take, min(min(p1,p2), not_take))
            else:
                cache[i] = (not_take, min(p1,p2))
            
            if max(take, not_take) > maxProd:
                maxProd = max(take, not_take)
        return maxProd
        
