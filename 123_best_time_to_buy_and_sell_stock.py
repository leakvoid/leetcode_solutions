# max profit for two best ranges, starting one after another ends
class Solution:
    def left_max_profit(self, ascending_ranges, right_bound):
        if right_bound in self.left_memory:
            return self.left_memory[right_bound]
        
        if right_bound == 0:
            return (ascending_ranges[0], ascending_ranges[0][0])
        
        current_range = ascending_ranges[right_bound]
        (left_best_range, left_minimum) = self.left_max_profit(ascending_ranges, right_bound - 1)
        
        new_minimum = min(current_range[0], left_minimum)
        current_profit = current_range[1] - new_minimum
        new_maximum = max(current_range[1], left_best_range[1])
        left_profit = new_maximum - left_best_range[0]
        if current_profit > left_profit:
            new_best_range = [new_minimum, current_range[1]]
        else:
            new_best_range = [left_best_range[0], new_maximum]
        
        self.left_memory[right_bound] = (new_best_range, new_minimum)
        return self.left_memory[right_bound]
    
    def right_max_profit(self, ascending_ranges, left_bound):
        if left_bound in self.right_memory:
            return self.right_memory[left_bound]
        
        if left_bound == len(ascending_ranges) - 1:
            return (ascending_ranges[left_bound], ascending_ranges[left_bound][1])
        
        current_range = ascending_ranges[left_bound]
        (right_best_range, right_maximum) = self.right_max_profit(ascending_ranges, left_bound + 1)
        
        new_maximum = max(current_range[1], right_maximum)
        current_profit = new_maximum - current_range[0]
        new_minimum = min(current_range[0], right_best_range[0])
        right_profit = right_best_range[1] - new_minimum
        if current_profit > right_profit:
            new_best_range = [current_range[0], new_maximum]
        else:
            new_best_range = [new_minimum, right_best_range[1]]
        
        self.right_memory[left_bound] = (new_best_range, new_maximum)
        return self.right_memory[left_bound]
    
    def maxProfit(self, prices: [int]) -> int:
        ascending_ranges = []
        ascending_flag = False
        left = 0
        right = 1
        while right < len(prices):
            if prices[right - 1] < prices[right]:
                ascending_flag = True
            else:
                if ascending_flag:
                    ascending_ranges.append([prices[left], prices[right - 1]])
                    ascending_flag = False
                left = right
            right += 1
        if ascending_flag:
            ascending_ranges.append([prices[left], prices[right - 1]])
        
        if len(ascending_ranges) == 0:
            return 0
        if len(ascending_ranges) == 1:
            return ascending_ranges[0][1] - ascending_ranges[0][0]
        
        self.left_memory = {}
        self.right_memory = {}
        max_profit = 0
        for i in range(len(ascending_ranges) - 1):
            (left_best_range, minimum) = self.left_max_profit(ascending_ranges, i)
            (right_best_range, maximum) = self.right_max_profit(ascending_ranges, i + 1)
            profit = left_best_range[1] - left_best_range[0] + right_best_range[1] - right_best_range[0]
            if profit > max_profit:
                max_profit = profit
        return max_profit

s = Solution()
print("[3,3,5,0,0,3,1,4]:", s.maxProfit([3,3,5,0,0,3,1,4]))
print("[1,2,3,4,5]:", s.maxProfit([1,2,3,4,5]))
print("[7,6,4,3,1]:", s.maxProfit([7,6,4,3,1]))
