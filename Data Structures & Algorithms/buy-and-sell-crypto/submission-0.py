class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=prices[0]

        for i in prices:
            maxprofit=max(maxprofit,i-minprice)
            minprice=min(minprice,i)#sell
        return maxprofit
        
        