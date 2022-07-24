
class Solution:
    def maxProfit_alternative(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit
    
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        
        max_profit = 0
        ascending_flag = False
        while right < len(prices):
            if prices[right - 1] < prices[right]:
                ascending_flag = True
            else:
                if ascending_flag:
                    max_profit += prices[right - 1] - prices[left]
                    ascending_flag = False
                left = right
            right += 1
        if ascending_flag:
            max_profit += prices[right - 1] - prices[left]
        return max_profit
