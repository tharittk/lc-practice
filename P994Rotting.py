class Solution(object):
    def orangesRotting(self, grid):
        self.rotten = []
        self.fresh = {}
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def spread_rot (rotten_q):
            tmp = []
            for rot in rotten_q:
                row  = rot[0]
                col = rot[1]
                if (row - 1, col) in self.fresh.keys():
                    self.fresh.pop((row - 1, col))
                    tmp.append((row-1, col))
                if (row + 1, col) in self.fresh.keys():
                    self.fresh.pop((row + 1, col))
                    tmp.append((row+1, col))
                if (row, col - 1) in self.fresh.keys():
                    self.fresh.pop((row, col - 1))
                    tmp.append((row, col-1))
                if (row, col + 1) in self.fresh.keys():
                    self.fresh.pop((row, col + 1))
                    tmp.append((row, col+1))
            return tmp
        
        # intialize
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    self.rotten.append((row,col))
                elif grid[row][col] == 1:
                    self.fresh[(row, col)] = 1
    
        count = 0
        while self.rotten:
            if not self.fresh.keys():
                return count

            q = spread_rot(self.rotten)
            self.rotten = q

            count += 1
        
        if self.fresh.keys():
            return -1
        else:
            return count


