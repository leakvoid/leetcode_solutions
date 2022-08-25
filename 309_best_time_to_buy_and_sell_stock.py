class Solution:
    def max_profit_rec(self, buy_price, idx, prices):
        if idx >= len(prices):
            return 0
        
        if buy_price in self.memory[idx]:
            return self.memory[idx][buy_price]
        
        while idx < len(prices) and buy_price >= prices[idx]:
            buy_price = prices[idx]
            idx += 1
        if idx == len(prices):
            return 0
        
        profit1 = prices[idx] - buy_price
        if idx + 2 < len(prices):
            profit1 += self.max_profit_rec(prices[idx + 2], idx + 3, prices)
        
        profit2 = self.max_profit_rec(buy_price, idx + 1, prices)
        
        self.memory[idx][buy_price] = max(profit1, profit2)
        return self.memory[idx][buy_price]
    
    def maxProfit(self, prices: [int]) -> int:
        self.memory = []
        for i in range(len(prices)):
            self.memory.append({})

        return self.max_profit_rec(prices[0], 1, prices)

arr = []
for i in range(100):
    arr.append(i)

s = Solution()
print(s.maxProfit(arr))
