class Solution:
    def maxProfit(self, prices):
        buy1, sell1 = float('inf'), 0
        buy2, sell2 = float('inf'), 0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        return sell2