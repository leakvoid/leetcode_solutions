class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_hash = set()
        
        for n in nums:
            if n in nums_hash:
                return True
            else:
                nums_hash.add(n)
        return False
