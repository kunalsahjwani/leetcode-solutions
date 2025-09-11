class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[7,1,5,3,6,4]
        max_profit = 0
        min_profit = float('inf')

        # for i in len price
        # if price[i]<min_profit:
        #   min profit = price [i]
        #profit = price[i] - min_profit
        #max_profit = max(p,m)

        for i in range(len(prices)):
            if prices[i]<min_profit:
                min_profit = prices[i]
            profit = prices[i] - min_profit

            #max_profit = max(profit, max_profit)
            if profit>max_profit:
                max_profit = profit

        return max_profit



        