class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        visited = [[False for j in range(ncol)] for i in range(nrow)]


        def validate_row_col(i, j):
            return (i >= 0  and i < nrow) and (j >= 0 and j < ncol)

        def dfs(i, j, s, v):
            if not s:
                return True
            if not validate_row_col(i, j):
                return False
            if (not v[i][j]) and board[i][j] == s[0]:
                v[i][j] = True
                for dx, dy in [[-1,0], [1,0],[0,1], [0,-1]]:
                    if dfs(i + dx, j + dy, s[1:], v):
                        return True

                v[i][j] = False
            else:
                return False

        # search first node
        collect = []
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    collect.append((i,j))
        #print(collect)
        for i, j in collect:
            if dfs(i, j, word, visited[:]):
                return True
        return False 
