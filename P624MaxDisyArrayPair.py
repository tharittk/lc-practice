class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        def is_in_top2_min (top2, val):
            for pair in top2:
                if val < pair[0]:
                    return True
            return False

        def is_in_top2_max (top2, val):
            for pair in top2:
                if val > pair[0]:
                    return True
            return False

        def insert_to_top2_min (top2, val, i):

            if val < top2[0][0]:
                tmp = top2[0]
                top2[0] = (val, i)
                top2[1] = tmp
            elif val < top2[1][0]:
                top2[1] = (val, i)
            
            return top2
        def insert_to_top2_max (top2, val, i):
            if val > top2[0][0]:
                tmp = top2[0]
                top2[0] = (val, i)
                top2[1] = tmp
            elif val > top2[1][0]:
                top2[1] = (val, i)
            return top2

        top2_min = [(1e4, -1), (1e4, -1)]
        top2_max = [(-1e4, -1), (-1e4, -1)]

        for i, arr in enumerate(arrays):
            candid_min = arr[0]
            candid_max = arr[-1]
            if is_in_top2_min (top2_min, candid_min):
                top2_min = insert_to_top2_min (top2_min, candid_min, i)
            if is_in_top2_max (top2_max, candid_max):
                top2_max = insert_to_top2_max (top2_max, candid_max, i) 

        if top2_min[0][1] == top2_max[0][1]:
            return max (abs (top2_min[0][0] - top2_max[1][0]), abs(top2_min[1][0] - top2_max[0][0]))
        else:
            return abs(top2_min[0][0] - top2_max[0][0])

