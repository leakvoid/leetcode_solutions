from collections import deque

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        return self.kthSmallest(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def partition(self, arr, l, r):
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i

    def kthSmallest(self, arr, l, r, k):
        if (k > 0 and k <= r - l + 1):
            index = self.partition(arr, l, r)

            if (index - l == k - 1):
                return arr[index]

            if (index - l > k - 1):
                return self.kthSmallest(arr, l, index - 1, k)

            return self.kthSmallest(arr, index + 1, r, 
                               k - index + l - 1)

s = Solution()
print(s.findKthLargest([10, 4, 5, 8, 6, 11, 26], 3))
print(s.findKthLargest([26, 10, 4, 5, 26, 8, 6, 11, 26], 3))
print(s.findKthLargest([26, 10, 4, 5, 8, 6, 11, 26], 3))
