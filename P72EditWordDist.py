class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # word 1 always shorter
        if len(word2) < len(word1):
            tmp = word1
            word1 = word2
            word2 = tmp
        memo = {}
        def aux(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo.keys():
                return memo[(i,j)]
            if word1[i] == word2[j]:
                res = aux(i+1, j+1)
                memo[(i+1, j+1)] = res
                return res
            else:
                res = 1 + min(min(aux(i+1, j+1), aux(i+1, j)), aux(i, j+1))
                memo[(i, j)] = res
                return res

        return aux(0,0)
                

        
        
