class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        def bin_search_left_most_gte(potions, target):
            lo = 0
            hi = len(potions) - 1
            result = -1
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                if potions[mid] >= target:
                    result = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return result

        minPotions = [(success + spell -1)/spell for spell in spells]
        potions.sort()
        out = []
        n = len(potions)
        for target in minPotions:
            result = bin_search_left_most_gte(potions, target)
            if result == -1:
                out.append(0)
            else:
                out.append(n - result)
        return out