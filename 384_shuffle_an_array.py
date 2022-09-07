import random

class Solution:

    def __init__(self, nums: List[int]):
        self.initial = nums
        self.nums = self.initial.copy()

    def reset(self) -> List[int]:
        self.nums = self.initial.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        n_len = len(self.nums)
        for i in range(n_len):
            swap = random.randint(0, n_len - 1)
            self.nums[i], self.nums[swap] = self.nums[swap], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
