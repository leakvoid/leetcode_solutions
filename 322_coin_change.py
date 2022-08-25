OVER_MAX_AMOUNT = 10001

class Solution:
    def count_coin_rec(self, coins, amount):
        if amount == 0:
            return 0
        
        if amount in self.memory:
            return self.memory[amount]
        
        min_count = OVER_MAX_AMOUNT
        for i in range(len(coins)):
            if coins[i] > amount:
                continue
            
            rem = amount - coins[i]
            count = 1 + self.count_coin_rec(coins, rem)
            
            if count < min_count:
                min_count = count
        
        self.memory[amount] = min_count
        return self.memory[amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memory = {}
        
        min_count = self.count_coin_rec(coins, OVER_MAX_AMOUNT, amount)
        if min_count >= OVER_MAX_AMOUNT:
            return -1
        return min_count
