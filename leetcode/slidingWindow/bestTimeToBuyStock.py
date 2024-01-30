class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = 0
        right = 1
        maxProfit = 0  # initial Profit

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
                right += 1
            else:
                left = right
                right += 1

        return maxProfit
