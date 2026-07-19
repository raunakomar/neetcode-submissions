class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        j = len(prices)-1
        max_r = prices[j]
        while(j>=0):
            if(prices[j]>max_r):
                max_r = prices[j]
                print("j->",j,max_r)
            if(max_profit<max_r-prices[j]):
                max_profit = max_r-prices[j]
                print("max_profit->",max_profit)
            j=j-1
        return max_profit
