class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float("inf")
        res = 0
        for price in prices:
            if min_prices > price:
                min_prices = price
            res = max(price-min_prices, res)
        return res

# Time complexity : O(n)
# Space complexity : O(1)