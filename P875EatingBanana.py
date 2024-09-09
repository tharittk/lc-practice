class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def hour_use_for_speed_k (piles, k):
            h = 0
            for pile in piles:
                whole = pile // k
                rem = pile % k
                if rem != 0:
                    h += (whole + 1)
                else:
                    h += whole
            return h
        max_k = max(piles)
        min_k = 1

        k = (max_k + min_k) // 2
        best_k = max_k
        old_k = max_k + 1
        while (old_k != k):
            curr_h = hour_use_for_speed_k (piles, k)
            if curr_h <= h and k < best_k:
                best_k = k

            if curr_h > h: # must increase
                min_k = k
                old_k = k
                k = (min_k + max_k) // 2
            
            elif curr_h <= h: # try decrease
                max_k = k
                old_k = k
                k = (min_k + max_k) // 2

        return best_k