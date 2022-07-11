class Solution:
    def getRow(self, rowIndex: int) -> [int]:        
        row = [1]
        cur_idx = 0
        while cur_idx < rowIndex:
            prev = 1
            for i in range(1, len(row)):
                cur = row[i]
                row[i] = prev + row[i]
                prev = cur
            row.append(1)
            cur_idx += 1
        return row

s = Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
