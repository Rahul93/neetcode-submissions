class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        ans = 0

        for price in prices:
            lowest = min(lowest, price)
            ans = max(ans, price - lowest)

        return ans