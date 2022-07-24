class Solution:
    def binary_search(self, nums, start, end, target):
        if start > end:
            return None
        
        mid = (end + start) // 2
        
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.binary_search(nums, mid + 1, end, target)
        else:
            return self.binary_search(nums, start, mid - 1, target)

    def binary_search_loop(self, nums, start, end, target):
        while start <= end:
            mid = (end + start) // 2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return None
    
    def twoSum(self, numbers: [int], target: int) -> [int]:
        n1_i = 0
        while n1_i < len(numbers):
            n1 = numbers[n1_i]
            n2 = target - n1
            
            if numbers[n1_i] == numbers[n1_i + 1]:
                if n1 == n2:
                    return [n1_i + 1, n1_i + 2]
                n1_i += 1
                while numbers[n1_i] == numbers[n1_i + 1]:
                    n1_i += 1
                n1_i += 1
                continue
            
            n2_i = self.binary_search(numbers, n1_i + 1, len(numbers) - 1, n2)
            if n2_i:
                return [n1_i + 1, n2_i + 1]
            n1_i += 1

s = Solution()
print("[2,7,11,15] add to 9:", s.twoSum([2,7,11,15], 9))
