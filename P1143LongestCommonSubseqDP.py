class Solution:
    def __init__(self):
        self.nrow = 0
        self.ncol = 0
        self.text1 = ""
        self.text2 = ""
        self.cache = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        nrow = len(text1)
        ncol = len(text2)
        self.text1 = text1
        self.text2 = text2

        self.nrow = nrow
        self.ncol = ncol

        def sweep_col(self, c, j):
            for col in range(j, self.ncol):
                if self.text2[col] == c:
                    return 1
            return 0
        def sweep_row(self, c, i):
            for row in range(i, self.nrow):
                if self.text1[row] == c:
                    return 1
            return 0

        def aux(self, i,j):
            if (i, j) in self.cache.keys():
                return self.cache[(i,j)]
            elif i == nrow - 1 and j == ncol - 1:
                return 1 if self.text1[i] == self.text2[j] else 0
            elif i == nrow - 1:
                return sweep_col(self, self.text1[i], j)
            elif j == ncol - 1:
                return sweep_row(self, self.text2[j], i)
            else:
                if self.text1[i] == self.text2[j]:
                    take = 1 + aux(self, i + 1, j + 1)
                    down = aux(self, i + 1, j)
                    right = aux(self, i, j + 1)
                    self.cache[(i,j)] = max(take, down, right)
                else:
                    down = aux(self, i + 1, j)
                    right = aux(self, i, j + 1)
                    self.cache[(i,j)] = max(down, right)
                return self.cache[(i,j)]

        return aux(self, 0, 0)






