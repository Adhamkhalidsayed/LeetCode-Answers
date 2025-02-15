class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase_price = prices[0]

        profit = 0

        for sell_price in prices[1:]:
            if purchase_price > sell_price:
                purchase_price = sell_price
            else:
                profit = max(profit, sell_price-purchase_price)

        return profit