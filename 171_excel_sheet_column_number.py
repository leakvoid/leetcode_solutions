import string

letter_to_number = {}
for i in range(26):
    letter_to_number[string.ascii_uppercase[i]] = i + 1

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        p = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            res += letter_to_number[columnTitle[i]] * p
            p *= 26
        return res
