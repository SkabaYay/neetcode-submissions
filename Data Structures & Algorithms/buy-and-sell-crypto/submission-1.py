class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                total = prices[r] - prices[l]
                maxPrice = max(maxPrice, total)
            else:
                l = r
            r += 1
        return maxPrice