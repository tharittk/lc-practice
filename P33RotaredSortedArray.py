class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the index of the origin
        def find_index_origin(nums):
            if len(nums) == 2:
                return 0 if nums[0] < nums[1] else 1
            lo = 0
            hi = len(nums) - 1
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                front = mid - 1 if mid - 1 > 0 else len(nums) - 1
                back = (mid+1) % (len(nums) - 1)
                if nums[front] > nums[mid] and nums[mid] < nums[back]:
                    return mid
                
                if nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        def bin_search(nums, target):
            lo = 0
            hi = len(nums) - 1
            while (lo <= hi):
                mid = lo + (hi - lo) // 1
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        o = find_index_origin(nums)
        #print(o)
        # standard binary search
        if target == nums[o]:
            return o

        elif target > nums[o] and target <= nums[-1]:
            use = nums[o:]
            i = bin_search(use, target)
            return (i + o) if i != -1 else -1
        else:
            use = nums[:o]
            i = bin_search(use, target)
            return i

