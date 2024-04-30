def maxProfit(prices):

    left = 0
    maxMoney = 0

    for right in range(1, len(prices)):
        if prices[left] >= prices[right]:
            left = right
        else:
            maxMoney = max(maxMoney, prices[right] - prices[left])

    return maxMoney


print(maxProfit([7, 6, 4, 3, 1]))
