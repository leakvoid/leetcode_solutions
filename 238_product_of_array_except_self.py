class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_prefix_prod = []
        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            prod *= nums[i]
            right_prefix_prod.append(prod)
            
        left_prefix_prod = []
        left_prefix_prod.append(right_prefix_prod[-1])
        prod = 1
        for i in range(len(nums) - 1):
            prod *= nums[i]
            left_prefix_prod.append(prod)
        
        for i in range(1, len(nums) - 1):
            left_prefix_prod[i] *= right_prefix_prod[len(right_prefix_prod) - i - 1]
        return left_prefix_prod
