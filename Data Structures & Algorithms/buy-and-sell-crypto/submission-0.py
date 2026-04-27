class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b , s = 0 , 1
        res =0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                res = max(res , profit)
            else:
                b = s
            s +=1
        return res
        