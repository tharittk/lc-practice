class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if 0 not in nums:
            return True
        #print("Checking if can reach: ", nums[-1])
        if len(nums) <= 1:
            return nums[0] > 0
        for i in range(len(nums)-2, -1, -1):
            #print("-----if jump from possible: ", nums[i])
            to_jump = len(nums) - i - 1
            if nums[i] >= to_jump:
                return True and self.canJump(nums[:(i+1)])
        return False

    