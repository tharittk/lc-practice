class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {} # key is how many step left
        memo[0] = cost[-1]
        memo[1] = cost[-2]
        for i in range(2, len(cost)):
            memo[i] = cost[-i -1] + min (memo[i - 1], memo[i - 2])
        return min(memo[len(cost) - 1], memo[len(cost) - 2])
        
