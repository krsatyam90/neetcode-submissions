class Solution:
    def minCostClimbingStairs(self, cost):
        # base case
        n = len(cost)
        dp = [0] * n 
        # base case
        dp[0] = 0
        dp[1] = 1
        # filling the Dp 
        for i in range(n):
            dp[i] = cost[i]+ min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])


        