class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_buy_price = prices[0]

        for price in prices:
            if price < min_buy_price:
                min_buy_price = price
            else:
                current_profit = price - min_buy_price
                if current_profit > maxProfit:
                    maxProfit = current_profit
        return maxProfit