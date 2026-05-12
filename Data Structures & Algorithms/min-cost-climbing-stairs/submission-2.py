class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] *n
        # base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        # filling Dp array 
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])

        