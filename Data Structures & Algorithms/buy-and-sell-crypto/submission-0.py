class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest =prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            res = max(res, prices[i] - lowest) #要循环找到lowest之后，才能
        return res
