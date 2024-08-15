class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy
        #nums = [2]
        pos = 0
        count = 0
        while pos < len(nums) - 1:
            if pos + nums[pos] >= len(nums) - 1:
                return count + 1
            max_jump = nums[pos]
            max_gain = 0
            for jump in range(min(max_jump + 1, len(nums) - pos )):
                gain = jump + nums[pos + jump]
                if gain > max_gain:
                    max_gain = gain
                    opt_jump = jump
            if (opt_jump == 0):
                pos = pos + nums[pos]
            else:
                pos = pos + opt_jump
            print("after jump ", pos)
            count += 1
        #print(count)
        return count
        