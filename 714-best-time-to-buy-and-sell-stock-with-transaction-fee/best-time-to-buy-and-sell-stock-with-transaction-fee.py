class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        ahead = [0, 0]
        curr = [0, 0]
        if n== 0:
            return 0    
        profit=0
        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j == 0:  # Can buy (skip, buy today)
                    profit = max(ahead[0], -prices[i] + ahead[1])
                else:  # Can sell(skip, sell today)
                    profit = max(ahead[1], prices[i] - fee + ahead[0])
                curr[j] = profit
            ahead = curr[:] #ahead ← curr

        return curr[0] # max profit we buy

        # max=max(0,-1+i-fee)