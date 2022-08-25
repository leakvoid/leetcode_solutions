class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) % 2:
            mid = len(s) // 2 + 1
        else:
            mid = len(s) // 2
        last = len(s) - 1
        for i in range(mid):
            s[i], s[last - i] = s[last - i], s[i]
        return s
