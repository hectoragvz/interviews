def maxprofit(prices):
    left = 0
    maxProfit = 0

    for right in range(len(prices)):
        maxProfit = max(maxProfit, prices[right] - prices[left])
        while prices[left] > prices[right]:
            left = right
    return maxProfit


print(maxprofit(prices=[7, 1, 5, 3, 6, 4]))
