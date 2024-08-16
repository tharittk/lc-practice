class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
 
        def binarySearchIndex(nums, target, lo, hi):
            print("Calling with lo hi", lo, hi)

            if hi >= lo:
                mid = int((lo + hi) / 2)
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    return binarySearchIndex(nums, target, lo, mid-1)
                else:
                    return binarySearchIndex(nums, target, mid + 1, hi)
            else:
                return -1

        lo = 0
        hi = len(nums) - 1
        exist = binarySearchIndex(nums, target, lo, hi)
        #print(exist)
        if exist == -1:
            return [-1, -1]
        else:
            # lower
            if exist == 0:
                low_bound = exist
            else:
                lo_exist = exist
                result = binarySearchIndex (nums, target, lo, lo_exist - 1)
                while (result != -1):
                    lo_exist = result
                    result = binarySearchIndex (nums, target, lo, lo_exist-1)
                low_bound = lo_exist # last to be found
                #print(low_bound)
 
            # upper
            if exist == hi:
                hi_bound = exist
            else:
                hi_exist = exist
                result = binarySearchIndex (nums, target, hi_exist + 1, hi)
                while (result != -1):
                    hi_exist = result
                    result = binarySearchIndex(nums, target, hi_exist+1, hi)
                hi_bound = hi_exist
                #print(hi_bound)

            return [low_bound, hi_bound]
 
