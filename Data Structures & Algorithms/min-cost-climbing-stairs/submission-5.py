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
        prev1 = cost[0]
        prev2 = cost[1]
        for i in (2,n):
            cur = cost[i] + min(perv1,prev2)
            perv1 = perv2
            perv2 = cur
        return min(perv1, perv2)
        


        