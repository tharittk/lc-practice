class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])
        mid_val = (matrix[0][0] + matrix[-1][0]) / 2
        lo = 0
        hi = nrow - 1
        nearest_greater = 0

        if nrow != 1:
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_val = matrix[mid][0]
                if mid_val < target:
                    lo = mid + 1
                elif mid_val > target:
                    hi = mid - 1
                    nearest_greater = mid
                else:
                    return True
        else:
            nearest_greater = 1
        
        search_row = nearest_greater - 1
        lo = 0
        hi = ncol - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = matrix[search_row][mid]
            if mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
            else:
                return True
        return False