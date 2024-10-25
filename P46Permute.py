class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        collect = [] # enclosing scope - aux will see it
        def aux(taken, available):
            if not available:
                collect.append(taken)
                return
            else:
                for i in range(len(available)):
                    # this cose O(1) amortized
                    taken.append(available[i]) # faster than taken + available[i] - this cose O (n))
                    aux(taken[:], available[:i] + available[i+1:])
                    taken = taken[:-1]

        aux([], nums)

        return collect



        
