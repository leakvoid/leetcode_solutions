class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        res = []
        intervals.sort()

        if len(intervals) < 2:
            return intervals

        i = 0
        d_len = len(intervals)
        while i < d_len - 1:
            li = intervals[i]
            ri = intervals[i + 1]
            if li[1] > ri[1]:
                intervals.pop(i + 1)
                d_len -= 1
            elif li[1] >= ri[0]:
                li[1] = ri[1]
                intervals.pop(i + 1)
                d_len -= 1
            else:
                i += 1
        return intervals

s = Solution()
s.merge([[1,3],[15,18],[2,6],[8,10]])
