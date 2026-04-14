class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_profit=0
        while r<len(prices) and l < r:
            profit=prices[r]-prices[l]
            if profit > 0 :
                max_profit=max(max_profit,profit)
            else :
                l=r
            r+=1
        return max_profit


        