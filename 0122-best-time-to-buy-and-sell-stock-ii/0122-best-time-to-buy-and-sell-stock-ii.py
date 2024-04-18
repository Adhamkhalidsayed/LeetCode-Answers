class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        lst = []
        while i + 1 < len(prices):
            if prices[i] >= prices[i+1]:
                i += 1
            elif prices[i] < prices[i+1]:
                profit = prices[i+1] - prices[i]
                i += 1
                lst.append(profit)

        x = sum(i for i in lst)

        return x
            