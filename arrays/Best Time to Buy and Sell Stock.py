#leetcode 121
def maxProfit(prices):
    buy, sell = 0, 1
    maxP = 0

    while sell < len(prices):

        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxP = max(maxP, profit)
        else:
            buy = sell

        sell += 1

    return maxP


print(maxProfit([7,1,5,3,6,4]))